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

/* ---- Karusel recenzí (posun po jedné kartě, tečky + šipky) ---- */
document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll("[data-carousel]").forEach(function (carousel) {
    var track = carousel.querySelector(".ref-carousel-track");
    var slides = Array.prototype.slice.call(track.children);
    var dotsWrap = carousel.querySelector("[data-carousel-dots]");
    var prevBtn = carousel.querySelector("[data-carousel-prev]");
    var nextBtn = carousel.querySelector("[data-carousel-next]");
    if (!track || !slides.length) return;

    var perView = 0;
    var dots = [];

    function computePerView() {
      var slideWidth = slides[0].getBoundingClientRect().width;
      if (!slideWidth) return perView || 1; // skryté – nepřepočítávat na 0 šířku
      var styles = getComputedStyle(track);
      var gap = parseFloat(styles.columnGap || styles.gap || "0") || 0;
      return Math.max(1, Math.round((track.clientWidth + gap) / (slideWidth + gap)));
    }
    function pageCount() {
      return Math.max(1, Math.ceil(slides.length / perView));
    }
    function currentPage() {
      var page = Math.round(track.scrollLeft / track.clientWidth);
      return Math.max(0, Math.min(pageCount() - 1, page));
    }
    function goToPage(i) {
      i = Math.max(0, Math.min(pageCount() - 1, i));
      track.scrollTo({ left: i * track.clientWidth, behavior: "smooth" });
    }
    function updateDots() {
      var idx = currentPage();
      dots.forEach(function (dot, i) {
        dot.classList.toggle("active", i === idx);
      });
    }
    function buildDots() {
      dotsWrap.innerHTML = "";
      dots = [];
      var pages = pageCount();
      for (var i = 0; i < pages; i++) {
        (function (page) {
          var dot = document.createElement("button");
          dot.type = "button";
          dot.setAttribute("aria-label", "Skupina recenzí " + (page + 1));
          dot.addEventListener("click", function () { goToPage(page); });
          dotsWrap.appendChild(dot);
          dots.push(dot);
        })(i);
      }
      updateDots();
    }
    function refresh() {
      var next = computePerView();
      if (next !== perView) {
        perView = next;
        buildDots();
      } else {
        updateDots();
      }
    }

    prevBtn.addEventListener("click", function () { goToPage(currentPage() - 1); });
    nextBtn.addEventListener("click", function () { goToPage(currentPage() + 1); });
    track.addEventListener("scroll", function () {
      clearTimeout(track._scrollTimer);
      track._scrollTimer = setTimeout(updateDots, 80);
    });
    // ResizeObserver zachytí i změnu šířky okna.
    if (window.ResizeObserver) {
      var ro = new ResizeObserver(function () { refresh(); });
      ro.observe(track);
    } else {
      perView = computePerView();
      buildDots();
      window.addEventListener("resize", function () {
        clearTimeout(window._refCarouselResizeTimer);
        window._refCarouselResizeTimer = setTimeout(refresh, 150);
      });
    }
  });
});
