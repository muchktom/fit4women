# FIT4WOMEN – copy a tone of voice

Tento dokument popisuje jazyk webu FIT4WOMEN: tón hlasu, oslovení, opakující se
copy vzorce a mikrocopy. Slouží jako referenční příručka, aby nový i upravovaný
text zněl stejně jako zbytek webu. Vychází z reálného textu na stránkách
(`web/src/*.njk`) k datu vzniku dokumentu.

> Vizuální styl (barvy, typografie, tvarosloví) popisuje [`design.md`](design.md).
> Tento dokument řeší jen slova.

---

## Tone of voice ve třech bodech

1. **Tykání, přímé oslovení „ty".** Web mluví k jedné konkrétní ženě, ne
   k anonymnímu publiku. „Tvoje cesta k síle začíná tady", „Cítíš se silná",
   „Přijď si vyzkoušet". Nikdy „vy" ani neosobní infinitivy typu „přihlásit se
   zde" bez adresáta.

2. **Osobní, ne korporátní.** Autorkou textu je Petra, ne značka. Sekce
   „Kdo jsem" a citace v `finalCta` mluví v první osobě ("Ráda tě provedu
   prvními kroky", "budu tě podporovat na každém metru tvojí cesty"). I obecné
   pasáže znějí jako od člověka, ne z manuálu – krátké věty, běžná slova,
   žádný marketingový žargon ("synergie", "komplexní řešení", "maximalizuj").

3. **Pečující, ale věcný.** Vřelost se projevuje tématem (komunita, děti,
   žádný tlak na výkon), ne přehnanou expresivitou. Text nepoužívá vykřičníky
   nadbytečně, emoji jen jako funkční značky (viz níže), a věty jsou krátké
   a jasné – žádné dlouhé souvětí ani ozdobná adjektiva navíc.

---

## Co web říká (a co neříká)

Ústřední poselství, které se vrací napříč stránkami – při psaní nového textu
se od něj neodchylovat:

- **„Cvičíš pro sebe, ne pro váhu."** Cíl je síla, energie, tělo bez bolesti
  a psychická pohoda – ne číslo na váze, ne vzhled jako primární motivace.
  Vzhled smí být zmíněn jen jako vtipný bonus, nikdy jako hlavní důvod
  ("A ono to pak i dobře vypadá. :)", "Přidanou hodnotou je, že to pak dobře
  i vypadá.").
- **Žádný tlak, žádná vina.** Necvičí se z povinnosti ani ze studu. Klíčová
  slova: radost, ne povinnost; „bez limitů"; „obtížnost snadno regulujeme";
  „kdykoliv si můžeš odpočinout". Nikdy nepoužívat vinu, srovnávání s ostatními
  ani „no excuses" rétoriku.
- **Komunita především.** Opakující se motiv je parta žen, které se
  nestydí, že jsou nové/osamělé/na mateřské. „Nikoho jsem tu neznala" je
  legitimní a časté – řešení, ne ostuda. Reference i „Kdo jsem" text to
  potvrzují vlastními slovy klientek.
- **S dětmi i bez dětí – obojí je v pohodě.** Nikdy nerámovat cvičení s dětmi
  jako kompromis nebo cvičení bez dětí jako "sobecké". Obě varianty jsou
  rovnocenná nabídka, ne náhradní řešení.
- **Nízký práh vstupu.** „První lekce zdarma", „nezávazně vyzkoušet", „žádná
  složitá logistika" – opakovaně se snižuje bariéra prvního kroku dřív, než
  se mluví o ceně nebo závazku.

---

## Struktura copy na stránce

Většina sekcí sleduje stejný vzorec (viz `components.njk` → `sectionHead`,
`pageHero`, `finalCta`):

- **Eyebrow** (malý nadnadpis, verzálky): 1–3 slova, pojmenovává sekci
  věcně – "Proč FIT4WOMEN", "Kde cvičíme", "Než přijdeš", "Průběh lekce".
  Ne úplná věta, ne call-to-action.
- **H1/H2**: krátká, silná, často v podobě tvrzení nebo výzvy – "Cvičíš pro
  sebe, ne pro váhu", "Máma cvičí, děti si hrají", "Ahoj, jsem Petra Váňová".
  Serifové nadpisy nesou hlavní myšlenku sekce, ne popis obsahu pod ním.
- **Lead / popisek pod nadpisem**: 1–2 věty, rozvíjí nadpis, končí buď
  konkrétním benefitem, nebo měkkým emočním obratem.
- **Finální CTA sekce** (`finalCta`) na konci každé stránky: krátká osobní
  citace/výzva + dvě tlačítka – jedno nízkoprahové (první lekce zdarma),
  jedno alternativní (kontakt/konzultace). Vzor:
  > "Ten první krok bývá nejtěžší. Ale nejsi na to sama. Provedu tě jím
  > a budu tě podporovat na každém metru tvojí cesty."

---

## Mikrocopy: tlačítka a odkazy

Tlačítka jsou vždy akce z pohledu uživatelky (1. osoba touhy/rozhodnutí), ne
neosobní infinitiv:

- „Chci začít" / „Chci individuální lekci" (ne "Přihlásit se zde")
- „Zjistit více"
- „Přijď na první lekci zdarma"
- „Domluvit si konzultaci" / "Napiš mi"
- „Rezervovat první lekci zdarma"
- „Přidat se do skupiny" (WhatsApp)
- „Přidat se" (primární CTA v hlavičce – nejkratší možná verze)

Vzorec: sloveso v 1. osobě přítomném/infinitivu jasně pojmenovává výsledek
akce, ne mechaniku formuláře. Když je bariéra vstupu klíčová, tlačítko to
připomíná („zdarma").

### Badge / tag mikrocopy

- Badge s tečkou v hero sekci: „První lekce zdarma" (dot + krátký text,
  ne celá věta).
- Tag „Kids-friendly" – anglicismus záměrně, je to zavedený termín cílovky.
- Ceníkové karty: krátké popisky bez sloves – „skupinová lekce venku, Újezd
  nad Lesy", ne "Toto je skupinová lekce, která probíhá venku...".

---

## Emoji – používat jako značky, ne dekoraci

Emoji na webu nikdy nezdobí větu, vždy nahrazují vizuální bullet nebo značí
kategorii:

- 🌳 venkovní / 🏠 vnitřní (opakovaně používané dvojice napříč stránkami)
- 💪 seznam přínosů cvičení
- ❤️🧡💛💚🩵 odlišení jednotlivých kurzů ve vzdělání (barevná řada, ne náhodná)
- ❗️ upozornění na důležitou zdravotní informaci (diastáza)
- Smajlík „:)" na konci věty jen když jde o odlehčení vážnějšího tématu
  (vzhled, humor) – ne jako obecné zakončení each odstavce.

Nepoužívat emoji v nadpisech, v CTA tlačítkách ani v eyebrow textu.

---

## FAQ a informační bloky

- Otázky ve FAQ jsou formulované tak, jak by je řekla váhající zákaznice,
  v 1. osobě: „Musím být fit, abych mohla přijít?", „Co když tam nikoho
  neznám?" – ne technické/obecné otázky.
- Odpověď začíná přímou reakcí na obavu („Vůbec ne.", „To je úplně běžné,…"),
  teprve pak vysvětlení.
- Praktické seznamy (co s sebou, rozvrh) jsou věcné, telegrafické, bez sloves
  v celé větě – ne prozaický popis.
- Drobné upozornění na vedlejší náklady/podmínky (doprava, storno, pronájem)
  jde vždy do menšího, ztlumeného textu (`font-size:.9rem;color:var(--muted)`),
  odděleného od hlavní ceny/nabídky – nikdy schované do hlavní věty.

---

## Reference / testimonials

Citace klientek se ponechávají v jejich vlastních slovech a délce (i delší
souvětí), na rozdíl od zbytku webu, kde je text úsporný. Nekrátit ani
nevyhlazovat je do firemního tónu – autenticita je zde záměrně cennější než
stručnost. Podpis vždy jméno + křestní iniciála příjmení + lokalita
("Gabča Č.", "Újezd nad Lesy").

---

## Petra vs. Péťa

Na webu se dnes objevují obě podoby jména, ale v odlišných rolích:

- **„Petra Váňová" – formální identita.** Titulky stránek, meta popisy,
  `kdo-jsem.njk`, patička, `site.js` (`contact.name`). Používá se všude, kde
  web mluví o ní jako o instruktorce/firmě navenek (SEO, kontakt, fakturační
  údaje).
- **„Péťa" / „Peťo" – dosud jen v ústech klientek.** Objevuje se výhradně
  uvnitř citací v referencích na hlavní stránce („Cvičení s Péťou mohu jen
  doporučit.", „…díky, Peťo."). Sama sebe takto v copy webu zatím nikde
  neoslovuje.

**Doporučení:** „Péťa" už je autentická, zavedená přezdívka, která přesně
sedí k tomu, čím se web odlišuje – osobní vztah, ne korporátní služba. Dává
smysl ji začít vědomě používat i v jejím vlastním hlase, ale jen tam, kde už
teď mluví přímo a osobně (podpisy zpráv, potvrzovací e-maily, uvítání na
„Kdo jsem") – **ne** ve formálních/oficiálních místech (titulek stránky,
meta popis, kontaktní údaje, patička, faktury), kde má zůstat „Petra Váňová".

Ukázka v praxi – podpis potvrzovací zprávy formuláře „Přihlášení na trénink":

> Díky za přihlášení! Ozvu se ti co nejdřív – pokud jsi uvedla termín,
> potvrdím ti ho, jinak se domluvíme, co ti bude vyhovovat. Mezitím se
> můžeš přidat do naší WhatsApp skupiny, tam najdeš rozvrh i partu holek,
> se kterými budeš cvičit. Těším se na tebe! **Péťa**

Kompromis: čím víc se brand sváže s neformálním „Péťa", tím osobnější
a odlišitelnější působí teď, ale tím těžší by bylo později škálovat (další
trenérky, byznys nezávislý na jedné osobě) nebo působit důvěryhodně
u dražších nabídek jako víkendový camp – tam bych se přiklonil spíš
k „Petra" i v podpisu.

---

## Slovník – používat vs. nepoužívat

| Používat | Nepoužívat |
|---|---|
| cvičení, lekce, trénink | „workout", „fitness program" |
| parta, komunita, holky/ženy | „klientela", „cílová skupina" |
| síla, energie, tělo bez bolesti | „hubnutí", „spalování tuků" jako hlavní rámec |
| nezávazně vyzkoušet | „bez rizika", „no-brainer" |
| s dětmi i bez dětí | „i s dětma" jako omluva/kompromis |
| tykání, „ty" | vykání, „vy", neosobní 3. osoba |

---

## Shrnutí v jedné větě

Web mluví jako Petra sama ke konkrétní ženě: tyká, nikam netlačí, mluví o síle
a komunitě místo o váze a výkonu, a každé CTA nejdřív připomene, že první krok
je zdarma a bez závazku.
