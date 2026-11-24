FILENAME = "serrures.html"

def cb(name, value, label):
    return f'<label><input type="checkbox" name="{name}" value="{value}"> {label}</label>'

HTML = head(
  "Serrures blindées & cylindres haute sécurité A2P | " + NAME,
  "Installation et changement de serrure blindée : serrures multipoints A2P, cylindres haute sécurité Fichet, Mul-T-Lock, Vachette, Bricard, Abus, Thirard, serrures connectées Nuki, Yale, Somfy… Devis gratuit.",
  "serrures.html") + header("serrures") + page_hero(
  "Serrures",
  "Serrures blindées &amp; cylindres haute sécurité.",
  "Serrures multipoints, changement de cylindre et serrures connectées. Nous posons les grandes marques du marché français, certifiées A2P★ à A2P★★★.",
  "changement-cylindre",
  logos=["point-fort-fichet", "mul-t-lock", "vachette", "bricard", "abus", "thirard", "mottura", "nuki"]
) + f'''
<main id="main">
<section class="section">
  <div class="container" id="catalogue-serrures">
    <div class="catalog-layout">
      <aside class="filters" id="filters-serrures" aria-label="Filtres">
        <div class="filters-head"><h2>Filtrer</h2><button type="button" data-reset>Réinitialiser</button></div>
        <div class="fgroup">
          <span class="label">Marque</span>
          <select name="brand" aria-label="Marque"><option value="">Toutes les marques</option></select>
        </div>
        <div class="fgroup">
          <span class="label">Type</span>
          {cb("kind","multipoints","Serrure multipoints")}
          {cb("kind","cylindre","Cylindre")}
          {cb("kind","verrou","Verrou")}
          {cb("kind","connectee","Serrure connectée")}
        </div>
        <div class="fgroup">
          <span class="label">Certification</span>
          {cb("cert","A2P1","A2P★")}
          {cb("cert","A2P2","A2P★★")}
          {cb("cert","A2P3","A2P★★★")}
          {cb("cert","hs","Haute sécurité (autre)")}
        </div>
        <div class="fgroup">
          <span class="label">Pose</span>
          {cb("pose","applique","En applique")}
          {cb("pose","encastree","Encastrée")}
          {cb("pose","cylindre","Remplacement de cylindre")}
          {cb("pose","electronique","Électronique")}
        </div>
      </aside>
      <div>
        <div class="catalog-bar">
          <span class="count" aria-live="polite"></span>
          <button class="btn btn-line btn-sm filters-toggle" type="button" aria-controls="filters-serrures" aria-expanded="false">{I["filter"]} Filtres</button>
          <div class="search">{I["search"]}<input type="search" placeholder="Rechercher : Fichet, cylindre, 5 points…" aria-label="Rechercher une serrure"></div>
        </div>
        <div class="products"></div>
        <p class="fine">Visuels non contractuels. Les niveaux de certification varient selon les versions de chaque gamme : la certification exacte figure sur le devis.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section-sand">
  <div class="container">
    <div class="head">
      <div><span class="kicker">Guide</span><h2>Quelle serrure pour votre porte ?</h2></div>
      <p>Trois solutions selon l'état de votre porte et le niveau de sécurité recherché.</p>
    </div>
    <div class="feature-row three">
      <div class="feature"><span class="ico">{I["key"]}</span><h3>Changer le cylindre</h3><p>Suffisant après une perte de clés ou un déménagement si la serrure est en bon état. Rapide et économique.</p></div>
      <div class="feature"><span class="ico">{I["lock"]}</span><h3>Serrure en applique</h3><p>Fixée côté intérieur, elle sécurise efficacement une porte en bois sans la remplacer.</p></div>
      <div class="feature"><span class="ico">{I["door"]}</span><h3>Serrure encastrée</h3><p>Intégrée dans l'épaisseur de la porte : discrète, elle équipe la plupart des portes blindées.</p></div>
    </div>
  </div>
</section>
''' + cta_block() + '''
</main>
''' + footer()
