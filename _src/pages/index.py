FILENAME = "index.html"

FAQ = [
  ("Quelle est la différence entre une porte blindée et un blindage de porte ?",
   "<p>Une <strong>porte blindée</strong> (ou bloc-porte blindé) remplace intégralement votre porte : le vantail <em>et</em> le bâti (huisserie) sont neufs, conçus et testés ensemble. C'est la seule solution qui peut obtenir la certification A2P BP1, BP2 ou BP3.</p><p>Le <strong>blindage</strong> consiste à renforcer votre porte actuelle (tôle d'acier, cornières anti-pince, paumelles renforcées, serrure multipoints). C'est plus économique, mais le niveau de résistance reste limité par l'huisserie existante.</p>"),
  ("Que signifient les certifications A2P BP1, BP2 et BP3 ?",
   "<p>La certification A2P est délivrée par le CNPP. Pour les blocs-portes, elle indique le temps de résistance face à une tentative d'effraction : <strong>5 minutes pour BP1</strong>, <strong>10 minutes pour BP2</strong> et <strong>15 minutes pour BP3</strong>. Pour les serrures, les niveaux vont de A2P★ à A2P★★★.</p>"),
  ("Mon assurance exige-t-elle une porte certifiée ?",
   "<p>Certains contrats d'assurance habitation imposent un niveau minimum (souvent une serrure A2P★★ ou un bloc-porte A2P BP1), notamment à Paris, en rez-de-chaussée ou pour des biens de valeur. Vérifiez votre contrat : nous vous remettons le certificat et la facture nécessaires pour votre assureur.</p>"),
  ("Combien de temps dure la pose d'une porte blindée ?",
   "<p>Le remplacement d'une porte blindée palière se fait généralement <strong>en une journée</strong>, avec dépose de l'ancienne porte, pose du bloc-porte, réglages et évacuation des gravats. La fabrication sur mesure demande en moyenne 3 à 6 semaines selon la marque.</p>"),
  ("Faut-il l'accord de la copropriété pour changer ma porte palière ?",
   "<p>La porte palière est souvent une partie privative, mais son aspect extérieur peut être encadré par le règlement de copropriété. Nous proposons des habillages extérieurs identiques à l'existant afin de respecter l'harmonie des parties communes.</p>"),
  ("Pouvez-vous installer une marque qui n'est pas dans votre catalogue ?",
   "<p>Oui. Nous travaillons avec l'ensemble des fabricants de portes blindées et de serrures du marché français. Si vous avez déjà choisi un modèle, indiquez-le dans votre demande de devis.</p>"),
  ("Proposez-vous un dépannage après une effraction ?",
   "<p>Oui, nous intervenons pour la mise en sécurité provisoire de votre logement (fermeture, remplacement de cylindre), puis nous vous établissons un devis de remplacement définitif à transmettre à votre assurance.</p>"),
]

faq_html = "\n".join(f'''      <details>
        <summary>{q}</summary>
        <div class="answer">{a}</div>
      </details>''' for q, a in FAQ)

import json, re
faq_ld = {
  "@context": "https://schema.org", "@type": "FAQPage",
  "mainEntity": [{"@type": "Question", "name": q,
                   "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", a)}} for q, a in FAQ]
}
biz_ld = {
  "@context": "https://schema.org", "@type": "Locksmith",
  "name": NAME, "url": DOMAIN + "/", "telephone": PHONE_TEL, "email": EMAIL,
  "address": {"@type": "PostalAddress", "streetAddress": ADDRESS.split(",")[0],
              "addressLocality": ADDRESS.split(",")[1].strip(), "addressCountry": "FR"},
  "areaServed": ZONE, "openingHours": "Mo-Sa 08:00-20:00",
  "description": "Remplacement de portes blindées, blindage de portes et installation de serrures haute sécurité certifiées A2P."
}
LD = ('<script type="application/ld+json">' + json.dumps(biz_ld, ensure_ascii=False) + '</script>\n'
      '<script type="application/ld+json">' + json.dumps(faq_ld, ensure_ascii=False) + '</script>\n')


# ---------- Bande logos ----------
marquee_imgs = "".join(logo_img(s, n, lazy=False) for s, n, c in BRANDS)
marquee = f'<div class="marquee" aria-label="Marques installées"><div class="marquee-track">{marquee_imgs}</div><div class="marquee-track" aria-hidden="true">{marquee_imgs}</div></div>'

# ---------- Mur de marques ----------
cat_label = {"portes": "Porte blindée", "serrures": "Serrure", "connectees": "Connectée"}
def brand_href(slug, name, cats):
    return "/marques/" + BRAND_SLUG[name] + ".html"
wall = "".join(
    f'<a class="brand-cell" href="{brand_href(s, n, c)}" data-cats="{" ".join(c)}">{logo_img(s, n)}<span>{n}</span></a>'
    for s, n, c in BRANDS)
n_portes = sum(1 for b in BRANDS if "portes" in b[2])
n_serr = sum(1 for b in BRANDS if "serrures" in b[2])
n_conn = sum(1 for b in BRANDS if "connectees" in b[2])

HTML = head(
  "Porte blindée & serrure haute sécurité – Remplacement et installation | " + NAME,
  "Remplacement de porte blindée, blindage de porte et changement de serrure A2P. Plus de 35 marques : Fichet, Picard, Bricard, Héraclès, Tordjman, Mul-T-Lock, Vachette… Devis gratuit.",
  "", LD) + header("") + f'''
<main id="main">

<!-- ================= HERO ================= -->
<section class="hero">
  <div class="container hero-grid">
    <div>
      <span class="kicker">Spécialiste porte blindée &amp; serrurerie</span>
      <h1>La porte blindée certifiée, <em>posée en une journée.</em></h1>
      <p class="lead">Remplacement de porte blindée, blindage de porte existante et serrures haute sécurité A2P. Nous installons toutes les grandes marques du marché français, avec un devis clair et gratuit.</p>
      <div class="hero-actions">
        <a class="btn btn-red" href="#devis">Demander mon devis gratuit {I["arrow"]}</a>
        <a class="btn btn-line" href="/portes-blindees.html">Voir les portes blindées</a>
      </div>
      <div class="hero-facts">
        <div><strong>{len(BRANDS)}+</strong><span>marques installées</span></div>
        <div><strong>A2P</strong><span>BP1 · BP2 · BP3</span></div>
        <div><strong>0 €</strong><span>visite &amp; devis</span></div>
      </div>
    </div>
    <div class="hero-media">
      <figure class="hero-photo">
        <img src="/assets/img/photos/serrure-multipoints-porte-blindee.webp" alt="Porte blindée équipée d'une serrure multipoints haute sécurité" width="903" height="1200" fetchpriority="high">
        <figcaption>{I["shield"]} Serrure multipoints sur porte blindée</figcaption>
      </figure>
      <div class="float-card float-a"><span class="badge">{I["shield"]}</span><div><strong>Certifiées A2P</strong><small>Résistance testée par le CNPP</small><div class="bars"><i></i><i></i><i></i></div></div></div>
      <div class="float-card float-b"><span class="badge">{I["clock"]}</span><div><strong>Pose en 1 journée</strong><small>Chantier propre, gravats évacués</small></div></div>
    </div>
  </div>
</section>

<!-- ================= LOGOS ================= -->
<section class="logo-band">
  <p>Nous installons les marques de référence</p>
  {marquee}
</section>

<!-- ================= SERVICES ================= -->
<section class="section" id="services">
  <div class="container">
    <div class="head reveal">
      <div><span class="kicker">Nos prestations</span><h2>Tout pour sécuriser votre porte d'entrée.</h2></div>
      <p>Du simple cylindre au bloc-porte certifié BP3, nous vous conseillons la solution adaptée à votre logement, à votre budget et aux exigences de votre assurance.</p>
    </div>
    <div class="bento">
      <a class="tile tile-photo t-7 reveal" href="/portes-blindees.html">
        <img src="/assets/img/photos/pose-serrure-porte-blindee.webp" alt="" loading="lazy">
        <div class="tile-body">
          <span class="num">01 — NOTRE SPÉCIALITÉ</span>
          <h3>Remplacement de porte blindée</h3>
          <p>Dépose de l'ancienne porte et pose d'un bloc-porte blindé neuf (porte + bâti), certifié A2P BP1, BP2 ou BP3.</p>
          <div class="chip-row"><span>Appartement</span><span>Maison</span><span>Immeuble</span><span>Sur mesure</span></div>
          <span class="go">Voir les portes blindées {I["arrow"]}</span>
        </div>
      </a>
      <a class="tile tile-photo t-5 tall reveal" href="/serrures.html">
        <img src="/assets/img/photos/changement-cylindre.webp" alt="" loading="lazy">
        <div class="tile-body">
          <span class="num">02</span>
          <h3>Serrure &amp; cylindre</h3>
          <p>Serrures multipoints A2P★ à ★★★, cylindres anti-crochetage, anti-perçage et anti-arrachement.</p>
          <span class="go">Voir les serrures {I["arrow"]}</span>
        </div>
      </a>
      <a class="tile t-4 reveal" href="/?prestation=blindage#devis">
        <span class="ico">{I["shield"]}</span>
        <div class="tile-body">
          <span class="num">03</span>
          <h3>Blindage de porte</h3>
          <p>Renforcez votre porte actuelle : tôle d'acier, cornières anti-pince, serrure multipoints.</p>
          <span class="go">Demander un devis {I["arrow"]}</span>
        </div>
      </a>
      <a class="tile tile-photo t-4 reveal" href="/?prestation=effraction#devis">
        <img src="/assets/img/photos/porte-effraction.webp" alt="" loading="lazy">
        <div class="tile-body">
          <span class="num">04</span>
          <h3>Après effraction</h3>
          <p>Mise en sécurité, rapport pour l'assurance et remplacement définitif.</p>
          <span class="go">Nous appeler {I["arrow"]}</span>
        </div>
      </a>
      <a class="tile t-4 reveal" href="/marques/nuki.html">
        <span class="ico">{I["smart"]}</span>
        <div class="tile-body">
          <span class="num">05</span>
          <h3>Serrures connectées</h3>
          <p>Ouverture par code, badge ou smartphone : Nuki, Yale, Somfy, Netatmo…</p>
          <span class="go">Découvrir {I["arrow"]}</span>
        </div>
      </a>
    </div>
  </div>
</section>

<!-- ================= MARQUES ================= -->
<section class="section section-sand" id="marques">
  <div class="container">
    <div class="head reveal">
      <div><span class="kicker">{len(BRANDS)} marques</span><h2>Toutes les marques du marché français.</h2></div>
      <p>Installateur indépendant, nous ne sommes liés à aucun fabricant : nous comparons objectivement les modèles pour vous et installons les grandes marques françaises et européennes.</p>
    </div>
    <div class="tabs reveal" role="tablist" aria-label="Filtrer les marques">
      <button type="button" role="tab" aria-selected="true" data-filter="all">Toutes ({len(BRANDS)})</button>
      <button type="button" role="tab" aria-selected="false" data-filter="portes">Portes ({n_portes})</button>
      <button type="button" role="tab" aria-selected="false" data-filter="serrures">Serrures &amp; cylindres ({n_serr})</button>
      <button type="button" role="tab" aria-selected="false" data-filter="connectees">Connectées ({n_conn})</button>
    </div>
    <div class="brand-wall reveal" id="brand-wall">{wall}</div>
    <div class="wall-foot"><span>Votre marque n'apparaît pas ? Nous intervenons aussi sur les autres fabricants.</span><a class="arrow-link" href="#devis">Demander un devis {I["arrow"]}</a></div>
  </div>
</section>

<!-- ================= CERTIFICATIONS ================= -->
<section class="section section-ink on-dark" id="certifications">
  <div class="container">
    <div class="head reveal">
      <div><span class="kicker">La certification A2P</span><h2>Quel niveau de sécurité choisir ?</h2></div>
      <p>Délivrée par le CNPP, la certification A2P garantit qu'une porte a résisté à de vraies tentatives d'effraction en laboratoire. Plus le niveau est élevé, plus la porte tient longtemps.</p>
    </div>
    <div class="cert-grid">
      <div class="cert reveal">
        <span class="lvl">Niveau 1</span>
        <h3>A2P BP1</h3>
        <div class="meter"><i style="width:33%"></i></div>
        <div class="mins"><span>Résistance</span><strong>5 minutes</strong></div>
        <p>Le standard recommandé pour un appartement en étage, en remplacement d'une porte palière.</p>
        <ul><li>{I["check"]} Appartement en étage</li><li>{I["check"]} Exigé par de nombreux assureurs</li><li>{I["check"]} Meilleur rapport prix / sécurité</li></ul>
      </div>
      <div class="cert pop reveal">
        <span class="flag">Le plus choisi</span>
        <span class="lvl">Niveau 2</span>
        <h3>A2P BP2</h3>
        <div class="meter"><i style="width:66%"></i></div>
        <div class="mins"><span>Résistance</span><strong>10 minutes</strong></div>
        <p>Pour les rez-de-chaussée, les maisons et les logements contenant des biens de valeur.</p>
        <ul><li>{I["check"]} Rez-de-chaussée &amp; maison</li><li>{I["check"]} Logement exposé</li><li>{I["check"]} Résistance doublée</li></ul>
      </div>
      <div class="cert reveal">
        <span class="lvl">Niveau 3</span>
        <h3>A2P BP3</h3>
        <div class="meter"><i style="width:100%"></i></div>
        <div class="mins"><span>Résistance</span><strong>15 minutes</strong></div>
        <p>Le plus haut niveau de la certification, pour les biens très exposés ou les exigences d'assurance élevées.</p>
        <ul><li>{I["check"]} Biens de grande valeur</li><li>{I["check"]} Exigence assurance élevée</li><li>{I["check"]} Protection maximale</li></ul>
      </div>
    </div>
    <div class="notice reveal">{I["info"]}<div><strong>Bon à savoir :</strong> seule une porte livrée et posée complète (bloc-porte) peut être certifiée A2P BP. Un blindage de porte existante n'est pas certifiable, même avec une serrure A2P★★★. Les portes italiennes sont généralement classées selon la norme européenne <strong>EN 1627</strong> (classes RC1 à RC6).</div></div>
  </div>
</section>

<!-- ================= POURQUOI NOUS ================= -->
<section class="section">
  <div class="container split">
    <div class="split-photo reveal">
      <img src="/assets/img/photos/serrurier-conseil-clients.webp" alt="Technicien conseillant un couple sur le choix de leur porte" loading="lazy">
      <div class="stamp">
        <div><strong>BP1→3</strong><span>Tous niveaux A2P</span></div>
        <div><strong>1 jour</strong><span>Durée de pose</span></div>
        <div><strong>0 €</strong><span>Visite &amp; devis</span></div>
      </div>
    </div>
    <div class="reveal">
      <span class="kicker">Pourquoi nous choisir</span>
      <h2>Un spécialiste de la porte, pas un dépanneur généraliste.</h2>
      <p class="muted">La porte d'entrée est le premier rempart de votre logement. Nous en avons fait notre métier : conseil, prise de mesures, pose et service après-vente.</p>
      <ul class="points">
        <li><span class="n">{I["file"]}</span><div><strong>Visite technique et devis gratuits</strong><span>Prise de mesures sur place, devis écrit et détaillé avant tout engagement.</span></div></li>
        <li><span class="n">{I["award"]}</span><div><strong>Conseil indépendant</strong><span>Aucune marque imposée : nous comparons pour vous les modèles du marché.</span></div></li>
        <li><span class="n">{I["tool"]}</span><div><strong>Pose soignée par nos techniciens</strong><span>Protection des sols, évacuation de l'ancienne porte, chantier laissé propre.</span></div></li>
        <li><span class="n">{I["shield"]}</span><div><strong>Documents pour votre assurance</strong><span>Facture détaillée et certificat A2P remis en fin de chantier.</span></div></li>
      </ul>
      <a class="btn btn-ink" href="#devis">Planifier ma visite gratuite {I["arrow"]}</a>
    </div>
  </div>
</section>

<!-- ================= PROCESS ================= -->
<section class="section section-sand">
  <div class="container">
    <div class="head reveal">
      <div><span class="kicker">Comment ça se passe</span><h2>Votre nouvelle porte en 4 étapes.</h2></div>
      <p>Un interlocuteur unique du premier appel jusqu'à la remise des clés.</p>
    </div>
    <div class="process">
      <div class="pstep reveal"><span class="dot">01</span><h3>Prise de contact</h3><p>Par téléphone ou via le formulaire. Nous vous rappelons pour comprendre votre besoin.</p></div>
      <div class="pstep reveal"><span class="dot">02</span><h3>Visite &amp; devis</h3><p>Un technicien prend les mesures et vous présente les modèles adaptés. Devis écrit.</p></div>
      <div class="pstep reveal"><span class="dot">03</span><h3>Fabrication</h3><p>Votre porte est fabriquée sur mesure aux dimensions exactes de votre ouverture.</p></div>
      <div class="pstep reveal"><span class="dot">04</span><h3>Pose en 1 jour</h3><p>Dépose, installation, réglages, remise des clés et du certificat.</p></div>
    </div>
  </div>
</section>

<!-- ================= GALERIE ================= -->
<section class="section">
  <div class="container">
    <div class="head reveal">
      <div><span class="kicker">Sur le terrain</span><h2>Nos interventions en images.</h2></div>
      <p>Pose de serrures multipoints, protections de cylindre, mises en sécurité : un travail précis, du premier au dernier point de fermeture. <a class="arrow-link" href="/realisations.html">Toutes nos réalisations {I["arrow"]}</a></p>
    </div>
    <div class="gallery reveal">
      <figure class="g-tall"><img src="/assets/img/photos/serrure-multipoints-porte-blindee.webp" alt="Serrure multipoints sur porte blindée" loading="lazy"><figcaption>Serrure 5 points</figcaption></figure>
      <figure class="g-wide"><img src="/assets/img/photos/cle-serrure-porte-blindee.webp" alt="Clés sur une porte blindée" loading="lazy"><figcaption>Porte blindée</figcaption></figure>
      <figure class="g-tall"><img src="/assets/img/photos/protege-cylindre-porte-entree.webp" alt="Protège-cylindre sur porte d'entrée" loading="lazy"><figcaption>Protège-cylindre</figcaption></figure>
      <figure><img src="/assets/img/photos/serrurier-ouverture-porte.webp" alt="Technicien intervenant sur une serrure" loading="lazy"><figcaption>Intervention</figcaption></figure>
      <figure><img src="/assets/img/photos/porte-vitree-reparee.webp" alt="Porte vitrée réparée après effraction" loading="lazy"><figcaption>Après effraction</figcaption></figure>
    </div>
  </div>
</section>

<!-- ================= TARIFS ================= -->
<section class="section section-sand" id="tarifs">
  <div class="container">
    <div class="head reveal">
      <div><span class="kicker">Tarifs indicatifs</span><h2>Combien coûte une porte blindée ?</h2></div>
      <p>Le prix dépend du niveau de certification, des dimensions et des finitions. Budgets constatés, fourniture et pose comprises.</p>
    </div>
    <div class="price-list reveal">
      <div class="price-row"><div><h3>Changement de cylindre haute sécurité</h3><small>Cylindre seul, sur serrure existante</small></div><span class="who">Clés perdues, déménagement</span><span class="amt">150 – 450 €<small>posé TTC</small></span></div>
      <div class="price-row"><div><h3>Serrure multipoints en applique A2P</h3><small>3 ou 5 points, A2P★ à ★★★</small></div><span class="who">Porte bois à sécuriser</span><span class="amt">400 – 1 200 €<small>posé TTC</small></span></div>
      <div class="price-row"><div><h3>Blindage de porte existante</h3><small>Tôle acier, cornières, serrure multipoints</small></div><span class="who">Budget maîtrisé</span><span class="amt">1 300 – 2 800 €<small>posé TTC</small></span></div>
      <div class="price-row"><div><h3>Bloc-porte blindé A2P BP1</h3><small>Porte + bâti neufs, certifiés</small></div><span class="who">Appartement en étage</span><span class="amt">3 000 – 5 000 €<small>posé TTC</small></span></div>
      <div class="price-row"><div><h3>Bloc-porte blindé A2P BP2</h3><small>Résistance 10 minutes</small></div><span class="who">Rez-de-chaussée, maison</span><span class="amt">4 500 – 7 000 €<small>posé TTC</small></span></div>
      <div class="price-row"><div><h3>Bloc-porte blindé A2P BP3</h3><small>Résistance 15 minutes</small></div><span class="who">Biens de grande valeur</span><span class="amt">7 000 € et +<small>posé TTC</small></span></div>
    </div>
    <p class="fine">Prix indicatifs, variables selon le modèle, les dimensions et les finitions. Seul le devis établi après visite fait foi. TVA réduite possible sous conditions pour les logements de plus de 2 ans.</p>
    <div class="sim-teaser reveal">
      <span class="ico">{I["calc"]}</span>
      <div><strong>Obtenez une estimation adaptée à votre logement</strong><span>4 questions, une fourchette de prix en 1 minute. Gratuit et anonyme.</span></div>
      <a class="btn btn-red" href="/simulateur.html">Lancer le simulateur {I["arrow"]}</a>
    </div>
  </div>
</section>

<!-- ================= GUIDES ================= -->
<section class="section">
  <div class="container">
    <div class="head reveal">
      <div><span class="kicker">Guides &amp; conseils</span><h2>Bien choisir avant d'acheter.</h2></div>
      <p>Prix, certifications, assurance : nos guides pour décider en connaissance de cause. <a class="arrow-link" href="/guides/">Tous les guides {I["arrow"]}</a></p>
    </div>
    <div class="guide-grid reveal">{"".join(guide_card(g) for g in GUIDES[:3])}</div>
  </div>
</section>

<!-- ================= ZONES ================= -->
<section class="section section-ink on-dark zones-band">
  <div class="container">
    <div class="head reveal">
      <div><span class="kicker">Zones d'intervention</span><h2>{ZONE}.</h2></div>
      <p>Nous intervenons dans {len(ZONES)} arrondissements et villes. Visite technique et devis gratuits partout dans notre zone.</p>
    </div>
    <div class="zone-list reveal">{"".join(zone_link(z) for z in ZONES[:24])}<a class="zone-chip more" href="/zones/">Toutes les villes {I["arrow"]}</a></div>
  </div>
</section>

<!-- ================= FAQ ================= -->
<section class="section" id="faq">
  <div class="container faq-layout">
    <div class="faq-aside reveal">
      <span class="kicker">Questions fréquentes</span>
      <h2>Vos questions, nos réponses.</h2>
      <div class="help">
        <strong>Une question technique ?</strong>
        <p>Un technicien vous répond directement, sans engagement.</p>
        <a class="btn btn-ink btn-sm" href="tel:{PHONE_TEL}" data-track="clic_appel">{I["phone"]} {PHONE}</a>
      </div>
    </div>
    <div class="faq reveal">
{faq_html}
    </div>
  </div>
</section>

<!-- ================= DEVIS ================= -->
<section class="section section-sand" id="devis">
  <div class="container">
    <div class="quote reveal">
      <div class="quote-side on-dark">
        <img class="bg" src="/assets/img/photos/cle-serrure-porte-blindee.webp" alt="" aria-hidden="true" loading="lazy">
        <span class="kicker">Devis gratuit</span>
        <h2>Parlons de votre projet.</h2>
        <p>Décrivez votre besoin : nous vous rappelons pour fixer une visite technique gratuite.</p>
        <ul>
          <li>{I["check"]} Réponse rapide, par un technicien</li>
          <li>{I["check"]} Devis écrit, détaillé, sans engagement</li>
          <li>{I["check"]} {len(BRANDS)}+ marques du marché français</li>
          <li>{I["check"]} {ZONE}</li>
        </ul>
        <a class="phone-big" href="tel:{PHONE_TEL}" data-track="clic_appel"><small>Ou appelez-nous directement</small><strong>{PHONE}</strong></a>
        {wa_btn("btn btn-ghost wa-side", "Envoyer une photo sur WhatsApp")}
      </div>
      <form class="quote-form" id="devis-form" name="devis" method="POST" action="/merci.html" data-netlify="true" netlify-honeypot="bot-field">
        <input type="hidden" name="form-name" value="devis">
        <p class="sr-only"><label>Ne pas remplir : <input name="bot-field"></label></p>
        <h3>Demande de devis</h3>
        <div class="field">
          <span class="label">Votre besoin <span class="req">*</span></span>
          <div class="choice" role="radiogroup" aria-label="Type de prestation">
            <label><input type="radio" name="prestation" value="remplacement" checked><span>{I["door"]}Porte blindée</span></label>
            <label><input type="radio" name="prestation" value="blindage"><span>{I["shield"]}Blindage</span></label>
            <label><input type="radio" name="prestation" value="serrure"><span>{I["lock"]}Serrure</span></label>
            <label><input type="radio" name="prestation" value="effraction"><span>{I["tool"]}Effraction</span></label>
          </div>
        </div>
        <div class="form-row">
          <div class="field"><label for="nom">Nom <span class="req">*</span></label><input id="nom" name="nom" type="text" autocomplete="name" required></div>
          <div class="field"><label for="telephone">Téléphone <span class="req">*</span></label><input id="telephone" name="telephone" type="tel" autocomplete="tel" inputmode="tel" required></div>
        </div>
        <div class="form-row">
          <div class="field"><label for="email">E-mail</label><input id="email" name="email" type="email" autocomplete="email"></div>
          <div class="field"><label for="cp">Code postal <span class="req">*</span></label><input id="cp" name="code_postal" type="text" inputmode="numeric" pattern="[0-9]{{5}}" autocomplete="postal-code" required></div>
        </div>
        <div class="form-row">
          <div class="field"><label for="logement">Logement</label>
            <select id="logement" name="logement"><option>Appartement</option><option>Maison</option><option>Immeuble / copropriété</option><option>Local professionnel</option></select>
          </div>
          <div class="field"><label for="niveau">Niveau souhaité</label>
            <select id="niveau" name="niveau"><option>Conseillez-moi</option><option>A2P BP1</option><option>A2P BP2</option><option>A2P BP3</option><option>Serrure A2P★ à ★★★</option></select>
          </div>
        </div>
        <div class="field"><label for="message">Votre message</label><textarea id="message" name="message" placeholder="Marque souhaitée, dimensions approximatives, délai…"></textarea></div>
        <label class="consent"><input type="checkbox" name="rgpd" required> <span>J'accepte que mes données soient utilisées pour être recontacté au sujet de ma demande (<a href="/mentions-legales.html#confidentialite">confidentialité</a>).</span></label>
        <button class="btn btn-red btn-block" type="submit">Recevoir mon devis gratuit {I["arrow"]}</button>
        <p class="secure">{I["lock"]} Données confidentielles, jamais revendues.</p>
      </form>
    </div>
  </div>
</section>

''' + cta_block() + '''
</main>
''' + footer()
