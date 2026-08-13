# Logo a ikony FIT4WOMEN

Tahle složka je **zdroj pravdy pro logo**. Nenasazuje se – leží mimo `src/`,
takže ji Eleventy vůbec nevidí.

```
web/brand/                        ← zdroj (nenasazuje se)
  logo-master.png                 originál 1536×1024, průhledné pozadí
  generate.py                     vygeneruje všechno odvozené
  README.md

web/src/assets/brand/             ← odvozené, nasazuje se
  logo-wordmark.png               hlavička (světlé pozadí)
  favicon.svg .ico -16 -32 -48 -512
  apple-touch-icon.png
```

`web/src/assets/images/` je teď **jen na fotky**, žádné logo tam nepatří.

## Změna loga

Přepiš `logo-master.png` a spusť:

```sh
cd web/brand
python3 generate.py          # potřebuje Pillow a numpy
python3 generate.py --light  # navíc varianta pro tmavé pozadí
```

Soubory v `src/assets/brand/` se **needitují ručně** – při dalším spuštění se
přepíšou. Když se změní rozložení loga, je potřeba v `generate.py` upravit
souřadnice nahoře (`CONTENT`, `FOUR_BAND`, `WOMEN_BOX`) – jsou odvozené
z toho, kde v předloze leží tmavý inkoust.

## Dvě pasti, na které se dá snadno naletět

**1. "4" není bílá – je to průhledný výsek.** V kresbě není bílá barva, ale
díra prosekaná akvarelem. Bílá vypadá jen proto, že za ní svítí bílá stránka.
Na tmavém pozadí zčerná. Proto:

- `logo-wordmark.png` (hlavička) – výsek se nechává průhledný, na světlém
  pozadí se přizpůsobí stránce lépe než natvrdo bílá
- favicony – výsek se vyplní, prohlížeč může mít v tmavém režimu tmavý panel
- `logo-wordmark-light.png` (`--light`) – výsek se vyplní; tuhle variantu
  teď nic nepoužívá, patička je bez loga

**2. "WOMEN" leží přes akvarel.** Pro čtvercové favicony se nedá jen odříznout,
protože by se rozřízla i kresba. `generate.py` ho domaluje (inpaint) z okolí
a siluetu kresby obnoví uzavřením obrysu.

## Proč jsou ikony jinak než logo

Logo je vodorovné (~1,57:1), favicon je čtverec. Kdyby se celé logo vložilo
doprostřed čtverce, zůstane přes třetinu plochy prázdná a pod ~48 px je
"WOMEN" nečitelné. Favicony proto ukazují jen akvarel + „Fit" + „4" – čitelné
zůstává i ve 32 px.

`apple-touch-icon.png` je jako jediný **neprůhledný**, s pozadím `--sand-50`
(`#faf6f1`). iOS průhlednost sráží na černou, což by spolklo černé „Fit".

## Kde se to používá

| Soubor | Šablona |
| --- | --- |
| `logo-wordmark.png` | `src/_includes/header.njk` |
| favicony, `apple-touch-icon.png` | `src/_includes/base.njk` |

Patička logo nemá – jen jméno, kontakt a lokality.

Starší kulatý znak (`logo-mark.png`, `logo.png`) se už nikde nepoužívá.
Kdyby byl potřeba, je v historii gitu před commitem, který tohle zavedl.
