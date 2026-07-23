module.exports = function (eleventyConfig) {
  // Statické soubory (CSS, JS, obrázky) kopírujeme 1:1 do výstupu
  eleventyConfig.addPassthroughCopy({ "src/assets": "assets" });
  eleventyConfig.addPassthroughCopy("src/CNAME");

  // Datum ve formátu YYYY-MM-DD (pro <lastmod> v sitemap.xml)
  eleventyConfig.addFilter("isoDate", (d) =>
    new Date(d).toISOString().slice(0, 10)
  );

  // Aktuální rok (pro copyright v patičce) – vyhodnotí se při buildu
  eleventyConfig.addGlobalData("year", () => new Date().getFullYear());

  return {
    // Web běží na vlastní doméně (www.fit4women.cz), proto kořenový prefix.
    // Odkazy a assety proto používají v šablonách filtr `| url`.
    pathPrefix: "/",
    dir: {
      input: "src",
      includes: "_includes",
      data: "_data",
      output: "_site",
    },
    htmlTemplateEngine: "njk",
    markdownTemplateEngine: "njk",
    templateFormats: ["njk", "html", "md"],
  };
};
