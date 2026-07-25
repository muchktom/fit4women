/* Odvozeno ze schedule.js pro strukturovaná data (openingHoursSpecification) v base.njk. */
const schedule = require("./schedule.js");

module.exports = schedule.map((s) => ({
  "@type": "OpeningHoursSpecification",
  dayOfWeek: s.dayOfWeek,
  opens: s.opens,
  closes: s.closes,
}));
