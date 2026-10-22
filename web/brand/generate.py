#!/usr/bin/env python3
"""Generate the deployed FIT4WOMEN logo and browser icons from logo-master.png."""
import base64
import io
import os

from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
MASTER = os.path.join(HERE, "logo-master.png")
OUT = os.path.abspath(os.path.join(HERE, "..", "src", "assets", "brand"))

WORDMARK_BOX = (160, 104, 1774, 835)
MARK_BOX = (120, 40, 920, 840)
FOUR_BOX = (670, 300, 920, 680)
WORDMARK_WIDTH = 600
SAND = (250, 246, 241, 255)


def remove_white_background(image):
    pixels = image.convert("RGB")
    result = Image.new("RGBA", pixels.size)
    source = pixels.load()
    target = result.load()

    for y in range(image.height):
        for x in range(image.width):
            red, green, blue = source[x, y]
            brightness = min(red, green, blue)
            if (
                FOUR_BOX[0] <= x < FOUR_BOX[2]
                and FOUR_BOX[1] <= y < FOUR_BOX[3]
                and brightness > 220
            ):
                alpha = round((brightness - 220) * 255 / 35)
                target[x, y] = (255, 255, 255, alpha)
                continue

            alpha = 255 - brightness
            if alpha < 4:
                target[x, y] = (255, 255, 255, 0)
                continue

            # Recover the logo color from its white matte while retaining
            # anti-aliased edges as transparency.
            matte = 255 - alpha
            target[x, y] = tuple(
                max(0, min(255, round((channel - matte) * 255 / alpha)))
                for channel in (red, green, blue)
            ) + (alpha,)

    return result


def save_png(image, path):
    image.save(path, "PNG", optimize=True)


def main():
    os.makedirs(OUT, exist_ok=True)
    logo = remove_white_background(Image.open(MASTER))

    wordmark = logo.crop(WORDMARK_BOX)
    wordmark_height = round(wordmark.height * WORDMARK_WIDTH / wordmark.width)
    save_png(
        wordmark.resize((WORDMARK_WIDTH, wordmark_height), Image.Resampling.LANCZOS),
        os.path.join(OUT, "logo-wordmark.png"),
    )

    mark = logo.crop(MARK_BOX)
    for size in (16, 32, 48, 512):
        save_png(
            mark.resize((size, size), Image.Resampling.LANCZOS),
            os.path.join(OUT, f"favicon-{size}.png"),
        )

    mark.resize((256, 256), Image.Resampling.LANCZOS).save(
        os.path.join(OUT, "favicon.ico"),
        format="ICO",
        sizes=[(16, 16), (32, 32), (48, 48)],
    )

    svg_png = io.BytesIO()
    mark.resize((256, 256), Image.Resampling.LANCZOS).save(svg_png, "PNG")
    encoded = base64.b64encode(svg_png.getvalue()).decode("ascii")
    with open(os.path.join(OUT, "favicon.svg"), "w", encoding="utf-8") as svg:
        svg.write(
            '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" '
            'role="img" aria-label="FIT4WOMEN">'
            f'<image href="data:image/png;base64,{encoded}" width="128" height="128"/>'
            "</svg>"
        )

    touch_icon = Image.new("RGBA", (180, 180), SAND)
    touch_icon.alpha_composite(
        mark.resize((160, 160), Image.Resampling.LANCZOS), (10, 10)
    )
    touch_icon.convert("RGB").save(
        os.path.join(OUT, "apple-touch-icon.png"), "PNG", optimize=True
    )

    print(f"Generated logo and icons in {OUT}")


if __name__ == "__main__":
    main()
