# Nepoužité fotky

Fotky, na které se v `src/` nikdo neodkazuje. Leží mimo `src/`, takže je
Eleventy nekopíruje do `_site/` a nenasazují se – v repu ale zůstávají,
kdyby se hodily.

**Chceš některou použít?** Přesuň ji zpátky do `web/src/assets/images/`
a odkaž se na ni ze šablony.

Pozor na to, že odkaz na obrázek může být i **relativní `url()` v CSS**
(např. `url("images/areal-venku.jpeg")` v `styles.css`), ne jen absolutní
cesta `/assets/images/…` v šabloně. Při dalším úklidu je potřeba projít obojí.
