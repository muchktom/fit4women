# FIT4WOMEN – design a barvy

Tento dokument popisuje vizuální jazyk webu FIT4WOMEN: barevnou paletu, typografii,
tvarosloví a designovou filosofii. Slouží jako referenční příručka, aby všechny
stránky a budoucí úpravy zůstaly vizuálně konzistentní.

> **Jediný zdroj pravdy pro barvy je** [`web/src/assets/styles.css`](web/src/assets/styles.css)
> v bloku `:root{ … }`. Tento dokument barvy vysvětluje, nedefinuje je znovu.

---

## Designová filosofie

Web cílí na ženy hledající kondiční cvičení ve skupině (Újezd nad Lesy, Koloděje),
včetně variant *kids-friendly*. Vizuální styl proto stojí na třech pilířích:

1. **Ženskost bez klišé.** Základem je fialová (švestková) paleta doplněná o teplé
   pískové a šedo-hnědé (taupe) tóny. Působí energicky a pečující zároveň – žádná
   pastelová „cukrárna", ale ani chladná korporátní modř.

2. **Teplo a přívětivost.** Pozadí stránky není čistě bílé, ale teple bílé
   (`--sand-50` `#faf6f1`). Kulaté tvary – kruhové fotky, plně zaoblená tlačítka
   (pill), měkké stíny – budují dojem osobního, lidského přístupu.

3. **Čitelnost a klid.** Velkorysé mezery mezi sekcemi (`74px`), řádkování `1.65`,
   zvýrazněné akce a jasná hierarchie. Text má vždy dostatečný kontrast; sytá
   fialová a švestková slouží jako „kotvy" pozornosti (nadpisy, tlačítka, pruhy).

Vizuálním leitmotivem jsou **kruhy**: portrétní fotky, ikony hodnot, avatary
referencí i číslované kroky. Kruh = kompletnost, komunita, pohyb.

---

## Barevná paleta

Všechny barvy jsou v CSS definované jako custom properties (proměnné) na `:root`,
takže se dají měnit na jednom místě.

### Fialová / švestková (primární značková rodina)

| Proměnná        | HEX       | Použití |
|-----------------|-----------|---------|
| `--plum-900`    | `#3a1f3d` | Skoro černá švestková – footer, tmavé nadpisy, konce gradientů |
| `--purple-700`  | `#774bad` | Hluboká fialová – tmavé pruhy, gradienty |
| `--purple-600`  | `#8d54cc` | Aktivní odkazy, hover tlačítek, akcenty v textu |
| `--purple-500`  | `#9755d1` | **Primární tlačítka**, eyebrow, hvězdičky, focus outline |
| `--purple-400`  | `#be8ce9` | Světlejší akcent – okraje, dekorativní záře |
| `--lav-100`     | `#f2ebf6` | Jemné fialové pozadí – tagy, ikony, note-boxy |

Fialová nese identitu značky. Je záměrně vedená jako **světlá, sytá ametystová**
– živá, ne pastelová: současně vysoká světlost i sytost (pastel by měl světlost
vysokou, ale sytost nízkou). Sytější/tmavší odstíny (`700`–`900`) tvoří tmavé
plochy a gradienty, střední (`500`–`600`) jsou pro interaktivní prvky, `lav-100`
je nejsvětlejší „nádech" pro jemná zvýraznění na bílém pozadí.

### Šedo-hnědá / taupe (neutrální doprovod)

| Proměnná        | HEX       | Použití |
|-----------------|-----------|---------|
| `--taupe-700`   | `#6f6154` | Šedo-hnědá – sekundární text, ceny, ikony |
| `--taupe-300`   | `#c9bcae` | Ztlumený text ve footeru |
| `--taupe-200`   | `#e7ddd1` | Světle hnědé okraje karet, oddělovače |

Taupe uzemňuje fialovou – dává jí teplo a „přírodní" charakter. Používá se pro
okraje karet, jemné linky a doplňkový text tam, kde by fialová byla příliš.

### Neutrály a pozadí

| Proměnná        | HEX       | Použití |
|-----------------|-----------|---------|
| `--sand-50`     | `#faf6f1` | Teple bílé pozadí celé stránky |
| `--white`       | `#ffffff` | Karty, formuláře, čisté plochy |
| `--ink`         | `#2c2632` | Základní barva textu (téměř černá s nádechem fialové) |
| `--muted`       | `#6b6470` | Ztlumený text – popisky, sekundární informace |

Pozadí stránky je záměrně **teple bílé**, nikoli čistě bílé – to je jeden
z klíčových prvků „tepla" celého webu. Bílé (`--white`) jsou pak karty, které
tak jemně vystupují z pozadí.

### Stavová barva

| Proměnná        | HEX       | Použití |
|-----------------|-----------|---------|
| `--ok`          | `#3f7d4e` | Zelená – potvrzení („kids-friendly ano" badge) |

---

## Gradienty

Sytost paletě dodávají fialové/švestkové gradienty na velkých plochách:

- **Hero (úvod):** `radial-gradient` z `--purple-600` → `--purple-700` → `--plum-900`
  s jemnou dekorativní září (`::before`).
- **Pruh hodnot (band), rozvrh, finální CTA:** lineární gradienty mezi
  `--purple-700`, `--purple-500` a `--plum-900` (`linear-gradient(140deg, …)`).
- **Camp hero:** tmavý fialový overlay přes fotografii areálu pro čitelnost textu.

Text na tmavých plochách je bílý, doplňkové odstavce v jemně nafialovělé bílé
(`#efe3f5`) pro měkčí kontrast.

---

## Typografie

| Proměnná   | Písmo | Použití |
|------------|-------|---------|
| `--serif`  | **DM Serif Display** (fallback Georgia) | Nadpisy, brand, ceny, citace, avatary – elegantní, ženský charakter |
| `--sans`   | **Manrope** (fallback system UI) | Běžný text, tlačítka, menu, popisky – čitelné, moderní |

Charakteristické prvky:

- **Hero H1** je výjimka – používá `--sans` v tučném (800) verzálkovém provedení
  pro razantní, „fitness" dojem. Ostatní nadpisy jsou serifové.
- **Eyebrow** (nadnadpis): verzálky, velké prostrkání (`letter-spacing: .18em`),
  fialová – uvádí sekce.
- Nadpisy mají `line-height: 1.12` a `text-wrap: balance` pro vyvážené zalomení.
- Tělo textu: `line-height: 1.65`, `text-wrap: pretty`.

---

## Tvarosloví a komponenty

- **Zaoblení:** základní rádius `--radius: 14px` pro karty; tlačítka a tagy jsou
  plně zaoblené (pill, `border-radius: 999px`); fotky a ikony často kruhové (50 %).
- **Stíny:** dvě úrovně – `--shadow-sm` (klidový stav karet) a `--shadow`
  (hover / zvýraznění). Barva stínu je fialová (`rgba(58,31,61,…)`), ne šedá –
  ladí s paletou.
- **Tlačítka:** varianty `btn-primary` (fialová plná), `btn-outline`, `btn-ghost`
  (na tmavém pozadí), `btn-light` (bílé na tmavém). Verzálky, hover posun nahoru
  (`translateY(-2px)`).
- **Karty** (`.track`, `.loc`, `.pc`, `.cc`, …): bílé pozadí, taupe okraj,
  malý stín, hover se zvednou o `4px`.
- **Mikrointerakce:** jemné přechody (0,15–0,18 s), zvětšení fotek při hoveru,
  „šipka odjede" u odkazů (`gap` roste).

---

## Přístupnost

- `:focus-visible` má viditelný fialový outline (`2px`, offset `3px`).
- Kontrast textu: tmavý `--ink` / `--plum-900` na světlém pozadí, bílá na tmavém.
- `scroll-behavior: smooth`, antialiasing a `text-rendering: optimizeLegibility`.
- Responsivita: nad `860px` desktopové mřížky, pod ní se vše skládá do jednoho
  sloupce a menu se mění na „burger".

---

## Rozvržení

- **Šířka obsahu:** `--wrap: 1140px`, boční padding `22px`.
- **Vertikální rytmus:** sekce `74px` (mobil `56px`), oddělovací mezery štědré.
- **Střídání pozadí:** `bg-white`, `bg-sand`, `bg-lav` a tmavé gradientové pruhy
  se střídají, aby web měl rytmus a sekce se vizuálně oddělovaly.

---

## Shrnutí v jedné větě

Fialová jako značka, teplá bílá a taupe jako klidné zázemí, serif pro eleganci
a kruhy pro lidskost – vše s velkorysým prostorem a čitelností na prvním místě.
