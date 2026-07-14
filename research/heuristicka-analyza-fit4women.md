# Heuristická analýza webu fit4women.cz

> **Metoda:** heuristická analýza všech 6 stránek ověřená živě v prohlížeči (DOM + vizuální kontrola), zkřížená s doporučeními z [vyzkum-fitness-trenerky-cr.md](vyzkum-fitness-trenerky-cr.md).
> **Datum:** 13. 7. 2026
> **Rozsah:** Úvod (/), Kdo jsem (/o-nas/), Služby (/sluzby/), Ceník (/cenik2/), Víkend s FIT4WOMEN (/reference/), Kontakt (/kontakt/).

---

## Co web dělá dobře (a výzkum to potvrzuje — zachovat!)

Reálné silné stránky, které sedí přímo na to, co výzkum označil za nejúčinnější:

- **Tón mluví jazykem klientky, ne výkonu.** Web říká *„vyčistíš si hlavu", „tělo bez bolesti", „energie do běžného dne", „poznáš fajn holky"* — ne kalorie a kila. Přesně princip z výzkumu (§2, §6), který řada trenérek nezvládá.
- **Autentický osobní příběh** (stavební inženýrka → mateřská → Strollering → FIT4WOMEN) + **komunita** („scházíme se i mimo cvičení"). Výzkum §4 to řadí mezi nejsilnější spouštěče („z členky pravidelnou účastnicí").
- **Kids-friendly jako jasné odlišení** — silný, konkrétní benefit hned v H1.
- **Konkrétnost rozvrhu** na Službách („STŘEDA 17:00, SportsField, Polesná") — výzkum §6 přesně tohle chválí.
- **Formuláře i mapy fungují** — na Službách i Víkendu je přihlašovací/rezervační formulář vč. výběru lekce a data.

---

## Ověřené technické nálezy (platí napříč webem — Webnode šablona)

| Nález | Stav | Dopad |
|---|---|---|
| **Title tagy** | ✅ jsou (`Stránka :: FIT4WOMEN`) | OK, ale bez lokality/klíčových slov |
| **Meta descriptions** | ⚠️ jsou, ale auto-výcuc | Nesmyslné pro vyhledávání — Ceník: *„cena za lekci – 2,5 měsíční plán"*; Kontakt má překlep *„neunikde"* |
| **Více H1 na stránce** | ❌ o-nas 3×, Služby 4×, Kontakt 3× | SEO chyba, má být 1 H1 + H2 |
| **Alt texty obrázků** | ❌ chybí u všech (Úvod 5/5, Služby 4/4, o-nas 1/1, Kontakt 1/1) | SEO + přístupnost |
| **Klikatelný telefon/e-mail** | ❌ žádný `tel:`/`mailto:` odkaz | Tření na mobilu (většina žen přijde z mobilu — výzkum §6) |
| **Odkazy na Instagram/Facebook** | ❌ žádné | Chybí hlavní kanál dle výzkumu §2 (zvlášť FB pro lokální komunitu) |
| Mapy (2× Google Maps na Kontaktu), cookie lišta | ✅ funkční | OK |

Drobné překlepy v textu: „TRÉNIK", „mítnější", „abysme".

---

## Hlavní mezery proti výzkumu (seřazeno dle síly dopadu)

### 1. Chybí nízkoprahový první krok — „první lekce zdarma" ⭐ nejsilnější a nejlevnější
Výzkum (§4.1, §6) to označuje za **nejúčinnější a nejsnáz nasaditelný** spouštěč. Web dnes nabízí nejlevnější vstup 140 Kč — pořád je to bariéra a závazek. Není žádná zkušební nabídka pro nové.
→ **Přidat „Přijď na první lekci zdarma" jako primární, opakované CTA.**

### 2. Nulový sociální důkaz — přitom stránka se jmenuje „reference" ⭐
Výzkum (§4.2, §4.4) řadí transformační příběhy a citace žen mezi **nejsilnější spouštěče vůbec**. Na celém webu **není jediná citace, recenze, foto z lekcí ani číslo**. Ironicky URL je `/reference/`, ale obsahuje jen camp.
→ **Sekce 3–6 krátkých citací žen (jméno, věk, foto se svolením)** + číslo typu *„už s námi pravidelně cvičí 30+ žen z okolí"*. Máš komunitu — je to marketing zdarma.

### 3. Slabá a nekonzistentní hierarchie CTA ⭐
Výzkum (§6) chce **jeden zřetelný krok, opakovaný vícekrát, vedoucí rovnou na rezervaci**. Realita:
- Úvod: jediné CTA „Kontakt na mě" až dole → vede na Kontakt, ne na rezervaci.
- **Ceník: žádné CTA.**
- Přihlašovací formulář je jen na Službách, z ostatních stránek na něj nic nevede.

→ Sticky tlačítko v hlavičce + závěrečné CTA na každé stránce, vždy → přihlášení na lekci.

### 4. Homepage nedrží doporučenou strukturu
Výzkum §6 dává ověřenou kostru: **Hero+CTA → benefity (pocitem) → jak to probíhá → sociální důkaz → ceník → o mně → FAQ → závěrečné CTA.** Web má obsah roztříštěný (rozvrh a „jak to probíhá" jen na Službách), hero je **vizuálně prázdný bez obrázku a bez tlačítka**, chybí FAQ a sociální důkaz.
→ Přeskládat úvod do této sekvence; hero doplnit fotkou + primárním CTA.

### 5. Chybí self-service rezervace + QR
Výzkum §3 doporučuje **Reservio/REENIO zdarma** (24/7 rezervace bez domlouvání) a rezervační odkaz/QR do IG bio a na letáky. Dnes je to e-mailový formulář + WhatsApp skupina (ta je fajn a částečně to řeší, ale není to samoobsluha s kapacitou/připomínkami).

### 6. Chybí konverzní „urychlovače"
Z výzkumu §4–5 zcela chybí: **doporučovací sleva** („přiveď kamarádku, obě lekci zdarma"), **časově omezená akce jen pro nové**, **sezónní výzva/challenge**, případně **FAQ** odbourávající bariéry („Musím být fit? Co když nikoho neznám?"). Část „co s sebou" na Službách je dobrý základ pro FAQ.

---

## Priorizovaný akční seznam

### Teď hned (vysoký dopad, nízká práce)
1. Zavést a všude opakovat CTA **„Přijď na první lekci zdarma →"** vedoucí na přihlašovací formulář.
2. Doplnit **sociální důkaz** — 3–6 citací žen + foto z lekcí + číslo komunity.
3. Přidat CTA na **Ceník** a sjednotit ceny/rozvrh napříč webem.
4. Přeskládat **homepage** dle struktury z výzkumu (hero s fotkou + CTA, benefity, jak to probíhá, reference, FAQ).
5. Udělat **telefon a e-mail klikatelné** (`tel:`/`mailto:`) a přidat **odkazy na Instagram/Facebook**.

### Brzy (střední dopad)
6. Nasadit **Reservio/REENIO zdarma** + QR kód (IG bio, letáky do MŠ/kaváren).
7. **Doporučovací sleva** + **časově omezená nabídka pro nové** na web.
8. Přepsat **meta descriptions** (popisné, s lokalitou) a **opravit na 1 H1** na stránku.
9. Doplnit **alt texty** obrázků, opravit překlepy.

### Průběžně
10. Sekce/rubrika **FAQ** (rozšířit „co s sebou" o „musím být fit / neznám tu nikoho / po porodu").
11. Sezónní **challenge** jako opakovaný konverzní tah.

---

## Shrnutí

Web má nadprůměrně dobrý **tón a příběh** (to nejtěžší), ale ztrácí na **konverzní mechanice** — chybí bezrizikový první krok, sociální důkaz a jasné opakované CTA. To jsou přesně tři páky, které výzkum označuje za nejúčinnější, a všechny tři jdou doplnit bez rozpočtu.

---

## Příloha: stav jednotlivých stránek (ověřeno v prohlížeči)

| Stránka | H1 | Formulář | CTA | Pozn. |
|---|---|---|---|---|
| Úvod `/` | 1 | ne | jen „Kontakt na mě" dole | prázdný hero bez obrázku; silný text, kids-friendly sekce |
| Kdo jsem `/o-nas/` | 3 | ne | žádné | osobní příběh + komunita + vzdělání (silné, autentické) |
| Služby `/sluzby/` | 4 | ano (jméno, e-mail, výběr lekce, datum) | „Odeslat" | nejbohatší obsah: rozvrh, „jak probíhá", „co s sebou", zdravotní pozn. |
| Ceník `/cenik2/` | 2 | ne | žádné | přehledné cenové tabulky; bez odkazu na přihlášení |
| Víkend `/reference/` | 1 | ano (jméno, e-mail, tel, datum, pozn.) | „Rezervovat" | camp 20.–22. 11. 2026, 5 990 Kč; bez fotek/recenzí z minula |
| Kontakt `/kontakt/` | 3 | ano (jméno, e-mail, zpráva) | „Odeslat" | 2× Google Mapy, WhatsApp skupina (kanál pro přihlašování) |
