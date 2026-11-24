FILENAME = "merci.html"

HTML = head(
  "Demande envoyée | " + NAME,
  "Votre demande de devis a bien été envoyée.",
  "merci.html") + '  <meta name="robots" content="noindex">\n' + header("") + f'''
<main id="main">
<section class="section">
  <div class="container" style="max-width:640px;text-align:center">
    <div class="feature" style="padding:56px 32px;display:flex;flex-direction:column;align-items:center">
      <span class="ico">{I["check"]}</span>
      <h1 style="font-size:2rem">Merci, votre demande est bien envoyée</h1>
      <p>Un technicien vous rappelle rapidement pour discuter de votre projet et fixer une visite gratuite.</p>
      <p>Besoin urgent ? Appelez-nous directement :</p>
      <a class="btn btn-red" href="tel:{PHONE_TEL}">{I["phone"]} {PHONE}</a>
      <p style="margin-top:24px"><a href="/">← Retour à l'accueil</a></p>
    </div>
  </div>
</section>
</main>
''' + footer()

INDEX = False
