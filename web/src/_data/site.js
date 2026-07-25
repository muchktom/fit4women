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
    ico: "29665353",
    email: "fit4womenujezd@gmail.com",
    phone: "+420 724 179 352",
    phoneHref: "tel:+420724179352",
    instagram: "https://www.instagram.com/fit4women_ujezd_nad_lesy/",
    facebook: "https://www.facebook.com/groups/1038345606504632/",
    googleMaps: "https://www.google.com/maps/place/FIT4WOMEN/@49.490399,11.8290176,8z/data=!4m12!1m2!2m1!1sfit4women!3m8!1s0x470b8d5b71f2999b:0xe035f19b61512a3a!8m2!3d50.0778829!4d14.653548!9m1!1b1!15sCglmaXQ0d29tZW5aCyIJZml0NHdvbWVukgEXd29tZW5zX3BlcnNvbmFsX3RyYWluZXKaAURDaTlEUVVsUlFVTnZaRU5vZEhsalJqbHZUMjFTV0ZkRmNGZE9WMlJXVkd0Vk0xVldSbE5UYlhRMFlUSTFUR0ZIWXhBQuABAPoBBAgAEDk!16s%2Fg%2F11z7d12vmw",
    whatsapp: "https://chat.whatsapp.com/HD25aLuCJSO6bPWJ5kEDDp", // ⚠️ ověřit platnost
    locations: [
      { name: "Újezd nad Lesy", detail: "hřiště ul. Polesná" },
      { name: "Koloděje", detail: "tělocvična TJ Slavoj, V Lipách 135" },
    ],
  },
};
