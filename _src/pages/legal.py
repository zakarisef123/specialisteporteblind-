FILENAME = "mentions-legales.html"

def ph(t, key=None):
    if key and LEGAL.get(key):
        return E(LEGAL[key])
    return f'<span class="placeholder">{t}</span>'

HTML = head(
  "Mentions légales & confidentialité | " + NAME,
  "Mentions légales et politique de confidentialité du site " + NAME + ".",
  "mentions-legales.html") + '  <meta name="robots" content="noindex">\n' + header("") + page_hero(
  "Mentions légales", "Mentions légales", "Informations légales et politique de confidentialité.", "serrurier-ouverture-porte") + f'''
<main id="main">
<section class="section">
  <div class="container prose">
    <h2>Éditeur du site</h2>
    <p>{NAME}<br>
    Forme juridique : {ph("[SARL / SAS / EI…]", "forme")} — Capital : {ph("[montant]", "capital")} €<br>
    Siège social : {ADDRESS}<br>
    SIRET : {ph("[numéro SIRET]", "siret")} — RCS : {ph("[ville]", "rcs")}<br>
    N° TVA intracommunautaire : {ph("[numéro]", "tva")}<br>
    Téléphone : {PHONE} — E-mail : {EMAIL}<br>
    Directeur de la publication : {ph("[nom du gérant]", "directeur")}</p>

    <h2>Assurance professionnelle</h2>
    <p>Assurance responsabilité civile professionnelle et décennale : {ph("[nom de l'assureur]", "assureur")}, contrat n° {ph("[numéro]", "contrat")}, couverture géographique : {ph("[France / région]")}.</p>

    <h2>Hébergement</h2>
    <p>{ph("[Nom de l'hébergeur, adresse et téléphone]", "hebergeur")}</p>

    <h2>Propriété intellectuelle</h2>
    <p>L'ensemble des contenus de ce site (textes, visuels, logo) est protégé. Toute reproduction sans autorisation est interdite. Les marques et noms de fabricants cités (Fichet, Picard Serrures, Bricard, Héraclès, Mul-T-Lock, Vachette, etc.) appartiennent à leurs propriétaires respectifs et sont mentionnés uniquement pour désigner les produits que nous installons. {NAME} est un installateur indépendant.</p>

    <h2>Médiation de la consommation</h2>
    <p>Conformément à l'article L.612-1 du Code de la consommation, le client peut recourir gratuitement au médiateur : {ph("[nom et coordonnées du médiateur]", "mediateur")}.</p>

    <h2 id="confidentialite">Politique de confidentialité</h2>
    <p>Les données transmises via le formulaire de devis (nom, téléphone, e-mail, code postal, message) sont utilisées uniquement pour répondre à votre demande et établir un devis. Elles ne sont ni vendues ni cédées à des tiers.</p>
    <p>Durée de conservation : 3 ans à compter du dernier contact. Conformément au RGPD, vous disposez d'un droit d'accès, de rectification, d'effacement et d'opposition en écrivant à {EMAIL}. Vous pouvez introduire une réclamation auprès de la CNIL.</p>
    <p>Ce site n'utilise pas de cookies publicitaires.</p>
  </div>
</section>
</main>
''' + footer()

INDEX = False
