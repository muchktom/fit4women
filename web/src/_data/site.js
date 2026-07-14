/* ==========================================================================
   FIT4WOMEN – centrální data webu (JEDINÝ ZDROJ PRAVDY)
   Dostupné ve všech šablonách jako proměnná `site`.
   Přidání položky menu / změna kontaktu = úprava jen zde.
   ========================================================================== */
module.exports = {
  // Kanonická doména webu (bez koncového lomítka) – pro sitemap, robots, canonical.
  // ⚠️ Uprav, pokud web poběží na jiné doméně.
  url: "https://www.fit4women.cz",

  // Primární akce (nízkoprahový první krok) – kam míří hlavní CTA v hlavičce
  primaryCta: { href: "/sluzby/#prihlaseni", label: "Přidat se" },

  nav: [
    { href: "/",           label: "Úvod",               key: "uvod" },
    { href: "/kdo-jsem/",  label: "Kdo jsem",           key: "kdo-jsem" },
    { href: "/sluzby/",    label: "Služby",             key: "sluzby" },
    { href: "/cenik/",     label: "Ceník",              key: "cenik" },
    { href: "/vikend/",    label: "Víkend s FIT4WOMEN", key: "vikend" },
    { href: "/kontakt/",   label: "Kontakt",            key: "kontakt" },
  ],

  contact: {
    name: "Petra Váňová",
    role: "Instruktorka fitness – osobní a kondiční trenérka",
    email: "fit4womenujezd@gmail.com",
    phone: "+420 724 179 352",
    phoneHref: "tel:+420724179352",
    instagram: "https://www.instagram.com/fit4women_ujezd_nad_lesy/",
    facebook: "https://www.facebook.com/groups/1038345606504632/",
    whatsapp: "https://chat.whatsapp.com/HD25aLuCJSO6bPWJ5kEDDp", // ⚠️ ověřit platnost
    locations: [
      { name: "Újezd nad Lesy", detail: "hřiště SportsField, ul. Polesná" },
      { name: "Koloděje", detail: "tělocvična TJ Slavoj, V Lipách 135" },
    ],
  },
};
