# Logo a ikony FIT4WOMEN

`logo-master.png` je zdrojová fotografie loga. Odvozené soubory v
`web/src/assets/brand/` nasazuje Eleventy; neupravují se ručně.

Po změně zdrojového loga vygeneruj soubory znovu:

```sh
cd web/brand
python generate.py
```

Skript potřebuje Pillow. Vytvoří průhledné vodorovné logo do záhlaví,
čtvercové ikony pro prohlížeč (PNG, ICO a SVG) a ikonu pro zařízení Apple.
Odstraní bílé pozadí fotografie; čtvercové ikony používají znak „Fit4“,
aby zůstal čitelný i v malé velikosti.

| Soubor | Použití |
| --- | --- |
| `logo-wordmark.png` | `../src/_includes/header.njk` |
| `favicon.svg`, `favicon-16.png`, `favicon-32.png`, `favicon-48.png`, `favicon.ico` | `../src/_includes/base.njk` |
| `apple-touch-icon.png` | `../src/_includes/base.njk` |

There is no logo in the footer.
