module.exports = function (eleventyConfig) {
  // Statické soubory (CSS, JS, obrázky) kopírujeme 1:1 do výstupu
  eleventyConfig.addPassthroughCopy({ "src/assets": "assets" });

  // Datum ve formátu YYYY-MM-DD (pro <lastmod> v sitemap.xml)
  eleventyConfig.addFilter("isoDate", (d) =>
    new Date(d).toISOString().slice(0, 10)
  );

  return {
    // Web běží na GitHub Pages jako projektový web (podadresář /fit4women/).
    // Až se přejde na vlastní doménu (fit4women.cz), změň na "/".
    // Odkazy a assety proto používají v šablonách filtr `| url`.
    pathPrefix: "/fit4women/",
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
