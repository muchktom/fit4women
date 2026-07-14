# FIT4WOMEN — web

Web postavený nad **[Eleventy](https://www.11ty.dev/)** (statický generátor). Píšeš reálné HTML
partialy, hlavička/patička i kontakty jsou na jednom místě, a `npm run build` vygeneruje
**čisté statické HTML** — ideální pro rychlost i SEO. Žádný framework, žádný runtime.

## Struktura

```
web/
├── package.json          # závislost: @11ty/eleventy
├── .eleventy.js          # konfigurace (vstup src/, výstup _site/)
├── src/
│   ├── _data/
│   │   └── site.js       # ⭐ JEDINÝ ZDROJ PRAVDY: menu, kontakty, CTA
│   ├── _includes/
│   │   ├── base.njk      # kostra stránky (head + hlavička + obsah + patička)
│   │   ├── header.njk    # hlavička – píše se JEN JEDNOU
│   │   ├── footer.njk    # patička – píše se JEN JEDNOU
│   │   └── components.njk # znovupoužitelné bloky jako makra (karty, rozvrh, ceny, FAQ…)
│   ├── assets/
│   │   ├── styles.css    # všechny styly
│   │   └── site.js       # mobilní menu + odesílání formulářů
│   ├── index.njk         # Úvod
│   ├── kdo-jsem.njk      # Kdo jsem
│   ├── sluzby.njk        # Služby + rozvrh + přihlašovací formulář
│   ├── cenik.njk         # Ceník
│   ├── vikend.njk        # Víkend s FIT4WOMEN (camp) + rezervace
│   └── kontakt.njk       # Kontakt + mapy + formulář
└── _site/                # ← vygenerovaný web (tohle se nasazuje; není v gitu)
```

## Práce s webem

```bash
npm install            # jednorázově
npm start              # lokální náhled s auto-reloadem → http://localhost:8080
npm run build          # vygeneruje _site/ k nasazení
```

## Nasazení na hosting

- **Netlify / Vercel / GitHub Pages:** nastav build command `npm run build` a publish adresář `_site`.
  Hosting si build spustí sám při každém pushnutí.
- **FTP / Webnode / jiný „přetáhni soubory":** spusť lokálně `npm run build` a nahraj **obsah složky `_site/`**.

## Jak je to škálovatelné (žádná duplikace)

- **Hlavička a patička** se píšou jen jednou v `src/_includes/header.njk` a `footer.njk`.
  Každá stránka je jen svůj obsah + v hlavičce (front matter) `active:` pro zvýraznění položky menu.
- **Menu, kontakty a hlavní CTA** jsou v `src/_data/site.js`. Změníš telefon, Instagram nebo
  přidáš položku menu na **jednom místě** → promítne se na celý web.
- **Styly** jen v `src/assets/styles.css`.
- **Opakující se bloky** (karty, hodnoty, rozvrh, reference, ceny, FAQ) jsou **makra**
  v `src/_includes/components.njk`. Na stránce se importují `{% import "components.njk" as c %}`
  a volají jako `{{ c.track(...) }}` / `{% call c.faq("Otázka") %}Odpověď{% endcall %}`.
  Změna vzhledu bloku = jedno místo.

### Přidání nové stránky (2 kroky)
1. Vytvoř `src/nazev.njk` s front matter:
   ```
   ---
   layout: base.njk
   active: nazev
   title: "Titulek stránky | FIT4WOMEN"
   description: "Popis pro vyhledávače."
   ---
   <section>…obsah…</section>
   ```
2. Přidej položku do pole `nav` v `src/_data/site.js`.

## Formuláře

Formuláře (přihláška, rezervace, dotaz) fungují i **bez serveru**: po odeslání složí e-mail
a otevřou poštovního klienta (`data-mailform` v `src/assets/site.js`).

➡️ **Doporučené vylepšení:** napojit na rezervační systém **Reservio** nebo **REENIO**
(zdarma, 24/7 samoobsluha), nebo formulářovou službu (Formspree). Stačí formuláři nastavit
`action` + `method` a e-mailový fallback se přeskočí.

## Co doplnit před ostrým spuštěním

- [ ] **Fotky** — v kódu jsou placeholdery `[ FOTO: … ]`. Nahradit reálnými.
- [ ] **Reference** (Úvod) — placeholder citace → doplnit reálné (jméno, věk, foto se svolením).
- [ ] **Počet žen v komunitě** — „30+", upravit dle reality.
- [ ] **WhatsApp odkaz** — v `src/_data/site.js` ověřit platnost.
- [ ] **„První lekce zdarma"** — potvrdit, že nabídka platí (jinak upravit texty a CTA).
- [ ] Napojení formulářů na rezervační systém (viz výše).
