#!/usr/bin/env python3
"""Vygeneruje všechny odvozené logo/ikony z jednoho zdroje: logo-master.png.

Spuštění (potřebuje Pillow + numpy):

    cd web/brand && python3 generate.py          # vše, co web používá
    cd web/brand && python3 generate.py --light  # + varianta pro tmavé pozadí

Výstup jde do ../src/assets/brand/ a přepíše se celý – zdroj pravdy je
vždycky logo-master.png, odvozené soubory se ručně needitují.

Co se generuje
--------------
logo-wordmark.png        vodorovné logo pro světlé pozadí (hlavička)
logo-wordmark-light.png  varianta pro tmavé pozadí – jen s `--light`,
                         nic ji teď nepoužívá (patička je bez loga)
favicon-{16,32,48,512}.png, favicon.ico, favicon.svg
apple-touch-icon.png

Dvě věci, které v předloze nejsou vidět a na kterých to jinak vždycky spadne
---------------------------------------------------------------------------
1. "4" není bílá barva, ale průhledný výsek v akvarelové kresbě. Bílá je jen
   proto, že za ní svítí bílá stránka. Na tmavém pozadí zčerná, takže se u
   tmavé varianty i u faviconů vyplňuje skutečnou bílou.
2. "WOMEN" leží *přes* akvarel. Pro čtvercovou ikonu se nedá odříznout –
   rozřízlo by to i kresbu – takže se domalovává (inpaint) z okolí.
"""
import base64
import io
import os
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
MASTER = os.path.join(HERE, "logo-master.png")
OUT = os.path.abspath(os.path.join(HERE, "..", "src", "assets", "brand"))

SAND = (250, 246, 241)          # --sand-50, pozadí webu

# Souřadnice v předloze (1536x1024). Zjištěné z rozložení tmavého inkoustu:
# "Fit" 270-593, "4" 593-768, "WOMEN" 768-1292, akvarel končí na x=1096.
CONTENT = (270, 135, 1293, 788)     # celé logo včetně "WOMEN"
FOUR_BAND = (580, 770)              # sloupce, kde leží "4"
WOMEN_BOX = (430, 600, 740, 1330)   # top, bottom, left, right
WORDMARK_W = 600                    # šířka exportu vodorovného loga


def blur(img, r):
    """Separabilní box blur (3 průchody ~= Gauss), jen numpy."""
    out = img.astype(np.float32)
    for _ in range(3):
        for axis in (0, 1):
            n = out.shape[axis]
            k = min(r, max(1, n // 2))
            pad = [(0, 0)] * out.ndim
            pad[axis] = (k, k)
            p = np.pad(out, pad, mode="edge")
            c = np.cumsum(p, axis=axis)
            c = np.concatenate([np.zeros_like(np.take(c, [0], axis=axis)), c], axis=axis)
            hi = np.take(c, np.arange(2 * k + 1, n + 2 * k + 1), axis=axis)
            lo = np.take(c, np.arange(0, n), axis=axis)
            out = (hi - lo) / (2 * k + 1)
    return out


def load_master():
    a = np.asarray(Image.open(MASTER).convert("RGBA")).astype(np.float32)
    return a[..., :3].copy(), a[..., 3] / 255.0


def luminance(rgb):
    return 0.299 * rgb[..., 0] + 0.587 * rgb[..., 1] + 0.114 * rgb[..., 2]


def enclosed_mask(alpha, close=9):
    """Vnitřek kresby včetně děr – uzavření + zaplavení od okraje."""
    img = Image.fromarray(((alpha > 0.5) * 255).astype(np.uint8))
    img = img.filter(ImageFilter.MaxFilter(close)).filter(ImageFilter.MinFilter(close))
    ImageDraw.floodfill(img, (0, 0), 128)
    return np.asarray(img) != 128


def four_knockout(alpha, exclude=None):
    """Průhledný výsek "4". Omezeno na jeho sloupce, aby to nezaplnilo
    vnitřní dírky v písmenech "WOMEN", kterými má prosvítat pozadí."""
    band = np.zeros(alpha.shape, dtype=bool)
    band[:, FOUR_BAND[0]:FOUR_BAND[1]] = True
    knock = (alpha < 0.5) & enclosed_mask(alpha) & band
    if exclude is not None:
        knock &= ~exclude
    return knock


def export(rgb, alpha, path, size=None, box=CONTENT, quantize=True):
    arr = np.dstack([np.clip(rgb, 0, 255), np.clip(alpha, 0, 1) * 255]).astype(np.uint8)
    img = Image.fromarray(arr)
    if box:
        img = img.crop(box)
    if size:
        img = img.resize(size, Image.LANCZOS)
    if quantize:
        img = img.quantize(colors=256, method=Image.FASTOCTREE)
    img.save(path, optimize=True)
    return img


def wordmark_size(box):
    w, h = box[2] - box[0], box[3] - box[1]
    return (WORDMARK_W, round(h * WORDMARK_W / w))


# --------------------------------------------------------------------------
# 1. Vodorovné logo pro světlé pozadí – jen výřez a zmenšení.
#    "4" tu zůstává průhledná záměrně: přizpůsobí se pozadí stránky lépe,
#    než by to udělala natvrdo bílá.
# --------------------------------------------------------------------------
def build_wordmark():
    rgb, alpha = load_master()
    img = export(rgb, alpha, f"{OUT}/logo-wordmark.png", size=wordmark_size(CONTENT))
    print(f"  logo-wordmark.png        {img.size}")


# --------------------------------------------------------------------------
# 2. Varianta pro tmavé pozadí – černý inkoust na bílý, "4" vyplnit.
#    Inkoust a akvarel jdou čistě oddělit jasem (inkoust <= 4, akvarel od
#    ~130), takže plynulá rampa zachová i antialiasing okrajů písmen.
# --------------------------------------------------------------------------
def build_wordmark_light():
    rgb, alpha = load_master()

    t = np.clip((120.0 - luminance(rgb)) / 110.0, 0.0, 1.0)[..., None]
    rgb = rgb * (1.0 - t) + 255.0 * t

    knock = four_knockout(alpha)
    rgb[knock] = 255.0
    alpha = alpha.copy()
    alpha[knock] = 1.0

    img = export(rgb, alpha, f"{OUT}/logo-wordmark-light.png", size=wordmark_size(CONTENT))
    print(f"  logo-wordmark-light.png  {img.size}  ({int(knock.sum())} px '4' vyplněno)")


# --------------------------------------------------------------------------
# 3. Čtvercový znak pro favicony – akvarel + "Fit" + "4", bez "WOMEN".
# --------------------------------------------------------------------------
def build_square_mark():
    rgb, alpha = load_master()

    # maska "WOMEN": volný práh + štědrá dilatace, jinak zůstanou po
    # antialiasovaných okrajích písmen oranžové duchy na žluté části kresby
    ink = (alpha > 0.15) & (rgb.max(axis=2) < 150)
    region = np.zeros_like(ink)
    top, bottom, left, right = WOMEN_BOX
    region[top:bottom, left:right] = True
    m = Image.fromarray(((ink & region) * 255).astype(np.uint8))
    need = np.asarray(m.filter(ImageFilter.MaxFilter(21))) > 127

    # barvu domalovat z okolí (jen z původních, důvěryhodných pixelů)
    known = np.where(need, 0.0, alpha)
    R = 40                                    # > šířka tahu písmen
    fill = blur(rgb * known[..., None], R) / np.maximum(blur(known, R)[..., None], 1e-6)

    # Průhlednost se takhle rozmazat nedá – za pravým okrajem kresby by se
    # rozlila ven a nechala tam bledý flek po "N". Silueta se místo toho
    # obnoví uzavřením obrysu, který známe.
    support = blur(enclosed_mask(np.where(need, 0.0, alpha), close=61).astype(np.float32), 2)

    out_rgb, out_a = rgb.copy(), alpha.copy()
    out_rgb[need] = fill[need]
    out_a[need] = np.clip(support, 0, 1)[need]

    knock = four_knockout(alpha, exclude=need)
    out_rgb[knock] = 255.0
    out_a[knock] = 1.0

    arr = np.dstack([np.clip(out_rgb, 0, 255), np.clip(out_a, 0, 1) * 255]).astype(np.uint8)
    mark = Image.fromarray(arr)
    box = mark.getchannel("A").point(lambda v: 255 if v > 10 else 0).getbbox()
    mark = mark.crop(box)

    w, h = mark.size
    side = int(max(w, h) * 1.05)
    sq = Image.new("RGBA", (side, side), (0, 0, 0, 0))
    sq.alpha_composite(mark, ((side - w) // 2, (side - h) // 2))
    print(f"  čtvercový znak           {sq.size}  (výřez {box})")
    return sq


# --------------------------------------------------------------------------
# 4. Favicony + apple-touch-icon z čtvercového znaku.
# --------------------------------------------------------------------------
def build_icons(mark):
    for n in (16, 32, 48, 512):
        img = mark.resize((n, n), Image.LANCZOS)
        if n >= 48:                      # malé velikosti kvantizace nezlepší
            img = img.quantize(colors=256, method=Image.FASTOCTREE)
        img.save(f"{OUT}/favicon-{n}.png", optimize=True)

    mark.resize((256, 256), Image.LANCZOS).save(
        f"{OUT}/favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)]
    )

    buf = io.BytesIO()
    mark.resize((256, 256), Image.LANCZOS).quantize(
        colors=256, method=Image.FASTOCTREE
    ).save(buf, "PNG", optimize=True)
    b64 = base64.b64encode(buf.getvalue()).decode()
    with open(f"{OUT}/favicon.svg", "w") as fh:
        fh.write(
            '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" '
            'role="img" aria-label="FIT4WOMEN">'
            f'<image href="data:image/png;base64,{b64}" width="128" height="128"/>'
            "</svg>"
        )

    # iOS průhlednost sráží na černou, což by spolklo černé "Fit",
    # proto tady jako jediné natvrdo pozadí webu.
    ati = Image.new("RGBA", (180, 180), SAND + (255,))
    ati.alpha_composite(mark.resize((160, 160), Image.LANCZOS), (10, 10))
    ati.convert("RGB").quantize(colors=256, method=Image.FASTOCTREE).save(
        f"{OUT}/apple-touch-icon.png", optimize=True
    )


def main():
    os.makedirs(OUT, exist_ok=True)
    print(f"zdroj:  {os.path.relpath(MASTER, HERE)}")
    print(f"výstup: {os.path.relpath(OUT, HERE)}\n")
    build_wordmark()
    # Tmavou variantu teď nic nepoužívá (patička je bez loga), takže se
    # negeneruje – jinak by se nasazoval soubor, na který nevede odkaz.
    # Až bude potřeba logo na tmavém pozadí, spusť s `--light`.
    if "--light" in sys.argv:
        build_wordmark_light()
    build_icons(build_square_mark())
    print()
    for f in sorted(os.listdir(OUT)):
        print(f"  {f:26s} {os.path.getsize(os.path.join(OUT, f)):>7,d} B")


if __name__ == "__main__":
    main()
