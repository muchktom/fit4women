/* ==========================================================================
   FIT4WOMEN – drobná klientská logika
   Hlavička i patička jsou teď statické HTML (generuje Eleventy z partialů),
   takže tady zbývá jen mobilní menu a odesílání formulářů.
   ========================================================================== */

/* ---- Mobilní menu (burger) ---- */
document.addEventListener("DOMContentLoaded", function () {
  var burger = document.getElementById("f4w-burger");
  var menu = document.getElementById("f4w-menu");
  if (burger && menu) {
    burger.addEventListener("click", function () {
      var open = menu.classList.toggle("open");
      burger.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }
});

/* ---- Formuláře bez backendu: fallback přes e-mail ----
   <form data-mailform data-subject="..." data-to="mail@..."> po odeslání složí
   e-mail a otevře poštovního klienta. Až bude k dispozici rezervační systém
   (Reservio/REENIO) nebo formulářová služba (Formspree, formulář Webnode),
   stačí formuláři nastavit action + method a tento skript se pro něj přeskočí. */
document.addEventListener("submit", function (e) {
  var form = e.target;
  if (!form.matches("form[data-mailform]")) return;
  e.preventDefault();
  var to = form.getAttribute("data-to") || "fit4womenujezd@gmail.com";
  var subject = form.getAttribute("data-subject") || "Zpráva z webu FIT4WOMEN";
  var lines = [];
  form.querySelectorAll("input, select, textarea").forEach(function (f) {
    if (!f.name || f.type === "submit") return;
    var label = f.getAttribute("data-label") || f.name;
    lines.push(label + ": " + (f.value || "–"));
  });
  var body = encodeURIComponent(lines.join("\n"));
  window.location.href =
    "mailto:" + to + "?subject=" + encodeURIComponent(subject) + "&body=" + body;
});
