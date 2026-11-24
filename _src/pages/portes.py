FILENAME = "portes-blindees.html"

def cb(name, value, label):
    return f'<label><input type="checkbox" name="{name}" value="{value}"> {label}</label>'

HTML = head(
  "Portes blindées – Toutes les marques du marché français | " + NAME,
  "Portes blindées certifiées A2P BP1, BP2, BP3 et EN 1627 : Fichet, Picard, Bricard, Héraclès, Tordjman, Zilten, Dierre, Gardesa… Fourniture et pose, devis gratuit.",
  "portes-blindees.html") + header("portes") + page_hero(
  "Portes blindées",
  "Portes blindées : toutes les marques du marché français.",
  "Blocs-portes certifiés A2P, portes italiennes classées EN 1627 et blindages de portes existantes. Filtrez par niveau de sécurité, logement ou marque, puis demandez votre devis gratuit.",
  "cle-serrure-porte-blindee",
  logos=["point-fort-fichet", "picard", "bricard", "heracles", "tordjman", "zilten", "dierre", "gardesa"]
) + f'''
<main id="main">
<section class="section">
  <div class="container" id="catalogue-portes">
    <div class="catalog-layout">
      <aside class="filters" id="filters-portes" aria-label="Filtres">
        <div class="filters-head"><h2>Filtrer</h2><button type="button" data-reset>Réinitialiser</button></div>
        <div class="fgroup">
          <span class="label">Marque</span>
          <select name="brand" aria-label="Marque"><option value="">Toutes les marques</option></select>
        </div>
        <div class="fgroup">
          <span class="label">Certification</span>
          {cb("cert","BP1","A2P BP1 · 5 min")}
          {cb("cert","BP2","A2P BP2 · 10 min")}
          {cb("cert","BP3","A2P BP3 · 15 min")}
          {cb("cert","RC3","EN 1627 classe 3")}
          {cb("cert","RC4","EN 1627 classe 4")}
          {cb("cert","none","Non certifiée")}
        </div>
        <div class="fgroup">
          <span class="label">Logement</span>
          {cb("usage","appartement","Appartement")}
          {cb("usage","maison","Maison")}
          {cb("usage","immeuble","Immeuble / copropriété")}
        </div>
        <div class="fgroup">
          <span class="label">Solution</span>
          {cb("type","bloc-porte","Bloc-porte complet")}
          {cb("type","blindage","Blindage de porte existante")}
        </div>
      </aside>
      <div>
        <div class="catalog-bar">
          <span class="count" aria-live="polite"></span>
          <button class="btn btn-line btn-sm filters-toggle" type="button" aria-controls="filters-portes" aria-expanded="false">{I["filter"]} Filtres</button>
          <div class="search">{I["search"]}<input type="search" placeholder="Rechercher : marque, BP2, isolation…" aria-label="Rechercher une porte"></div>
        </div>
        <div class="products"></div>
        <p class="fine">Visuels non contractuels. Chaque fabricant propose de nombreuses finitions, dimensions et options : les budgets sont indicatifs, seul le devis après visite fait foi.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section-sand">
  <div class="container">
    <div class="head">
      <div><span class="kicker">Bien choisir</span><h2>Les critères d'une bonne porte blindée.</h2></div>
      <p>Au-delà de la marque, quatre points font la différence au quotidien.</p>
    </div>
    <div class="feature-row">
      <div class="feature"><span class="ico">{I["shield"]}</span><h3>Certification</h3><p>A2P BP1 à BP3 ou EN 1627 : une résistance testée en laboratoire.</p></div>
      <div class="feature"><span class="ico">{I["lock"]}</span><h3>Serrure</h3><p>Multipoints, cylindre haute sécurité et carte de propriété des clés.</p></div>
      <div class="feature"><span class="ico">{I["volume"]}</span><h3>Acoustique</h3><p>Un bon bloc-porte réduit nettement les bruits des parties communes.</p></div>
      <div class="feature"><span class="ico">{I["thermo"]}</span><h3>Isolation</h3><p>Indispensable pour une porte donnant sur l'extérieur.</p></div>
    </div>
  </div>
</section>
''' + cta_block() + '''
</main>
''' + footer()
