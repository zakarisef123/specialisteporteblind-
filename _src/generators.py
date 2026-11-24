# Exécuté dans l'espace de noms de build.py (accès à head, header, footer, write, etc.)


from finitions import COLORIS, PANNEAUX, POIGNEES, OPTIONS, NIVEAUX

CERT_SHORT = {"BP1": "A2P BP1", "BP2": "A2P BP2", "BP3": "A2P BP3", "RC3": "EN 1627 cl. 3", "RC4": "EN 1627 cl. 4",
              "A2P1": "A2P★", "A2P2": "A2P★★", "A2P3": "A2P★★★", "hs": "Haute sécurité", "none": "—"}
USAGE = {"appartement": "Appartement", "maison": "Maison", "immeuble": "Immeuble"}

def brand_compare(prods):
    if len(prods) < 2:
        return ""
    is_door = prods[0]["kind_label"] == "porte"
    rows = ""
    for p in prods:
        col3 = ", ".join(USAGE[u] for u in p.get("usage", [])) if is_door else {"multipoints": "Multipoints", "cylindre": "Cylindre", "verrou": "Verrou", "connectee": "Connectée"}[p["kind"]]
        col4 = ("Bloc-porte" if p.get("type") == "bloc-porte" else "Blindage") if is_door else {"applique": "Applique", "encastree": "Encastrée", "cylindre": "Cylindre", "electronique": "Électronique"}[p["pose"]]
        rows += f'<tr><td><a href="/produits/{p["slug"]}.html">{E(p["name"])}</a></td><td>{CERT_SHORT.get(p.get("cert"), "—")}</td><td>{col3}</td><td>{col4}</td><td class="num">{p.get("price") or "Sur devis"}</td><td><label class="cmp-check"><input type="checkbox" data-compare="{p["id"]}"> Comparer</label></td></tr>'
    h3, h4 = ("Logement", "Solution") if is_door else ("Type", "Pose")
    return f"""<section class="section" style="padding-top:0">
  <div class="container">
    <div class="head"><div><span class="kicker">Comparatif</span><h2>Toute la gamme en un coup d'œil</h2></div><p>Cochez jusqu'à 3 modèles pour les comparer côte à côte.</p></div>
    <div class="table-wrap spec-table"><table>
      <thead><tr><th>Modèle</th><th>Certification</th><th>{h3}</th><th>{h4}</th><th>Budget posé</th><th></th></tr></thead>
      <tbody>{rows}</tbody>
    </table></div>
  </div>
</section>"""

def swatch(c):
    code, nom, col, dark = c
    return f'<span class="swatch"><i style="background:{col}"></i><strong>{code}</strong><small>{nom}</small></span>'

def brand_finishes(name):
    return f"""<section class="section section-sand">
  <div class="container">
    <div class="head"><div><span class="kicker">Finitions</span><h2>Personnalisez votre porte {E(name)}</h2></div><p>Habillages, coloris et options : les finitions disponibles dépendent de la gamme choisie et sont confirmées sur le devis.</p></div>
    <div class="swatches">{"".join(swatch(c) for c in COLORIS[:8])}</div>
    <div class="hero-actions" style="margin:32px 0 0"><a class="btn btn-red" href="/configurateur.html">Configurer ma porte {I["arrow"]}</a><a class="btn btn-line" href="/finitions.html">Toutes les finitions</a></div>
  </div>
</section>"""

CAT_LABEL = {"portes": "Portes blindées", "serrures": "Serrures & cylindres", "connectees": "Serrures connectées"}
DEP_LABEL = {"83": "Var (83)"}

def products_of(name):
    return [p for p in ALL_PRODUCTS if p["brand"] == name]

def devis_href(label, prestation):
    from urllib.parse import quote
    return f"/?produit={quote(label)}&prestation={prestation}#devis"

def wa_btn(cls="btn btn-line", text="WhatsApp"):
    if not WHATSAPP:
        return ""
    return f'<a class="{cls}" href="https://wa.me/{WHATSAPP}" target="_blank" rel="noopener" data-track="clic_whatsapp">{I["whatsapp"]} {text}</a>'

def aside_card(title="Un projet de porte blindée ?", text="Visite technique et devis gratuits, sans engagement."):
    return f'''<aside class="aside-card">
  <strong>{title}</strong>
  <p>{text}</p>
  <a class="btn btn-red btn-block" href="/#devis">Demander un devis {I["arrow"]}</a>
  <a class="btn btn-line btn-block" href="tel:{PHONE_TEL}" data-track="clic_appel">{I["phone"]} {PHONE}</a>
  <a class="aside-link" href="/simulateur.html">{I["calc"]} Estimer mon budget en 1 minute</a>
</aside>'''

# ======================================================== MARQUES
def brand_card(b):
    slug, name, logo, cats, origin, desc = b
    n = len(products_of(name))
    lg = logo_img(logo, name) if logo else f'<span class="brand-word">{E(name)}</span>'
    return f'''<a class="brand-card" href="/marques/{slug}.html" data-cats="{" ".join(cats)}">
  <span class="bc-logo">{lg}</span>
  <span class="bc-body"><strong>{E(name)}</strong><small>{" · ".join(CAT_LABEL[c] for c in cats)}{" · " + origin if origin else ""}</small></span>
  <span class="bc-count">{n} modèle{"s" if n > 1 else ""}</span>
</a>'''

n_p = sum(1 for b in BRAND_DATA if "portes" in b[3])
n_s = sum(1 for b in BRAND_DATA if "serrures" in b[3])
n_c = sum(1 for b in BRAND_DATA if "connectees" in b[3])
html_ = head(f"Marques de portes blindées et serrures installées | {NAME}",
             f"Fichet, Picard, Bricard, Héraclès, Tordjman, Mul-T-Lock, Vachette… Découvrez les {len(BRAND_DATA)} marques de portes blindées, serrures et serrures connectées que nous installons.",
             "marques/", crumbs_ld([("Accueil", "/"), ("Marques", "/marques/")])) + header("marques") + page_hero(
    "Marques", "Les marques que nous installons.",
    f"{len(BRAND_DATA)} fabricants français et européens de portes blindées, de serrures haute sécurité et de serrures connectées. Installateur indépendant, nous vous conseillons sans parti pris.",
    "serrure-multipoints-porte-blindee") + f'''
<main id="main">
<section class="section">
  <div class="container">
    <div class="tabs" role="tablist" aria-label="Filtrer les marques">
      <button type="button" role="tab" aria-selected="true" data-filter="all">Toutes ({len(BRAND_DATA)})</button>
      <button type="button" role="tab" aria-selected="false" data-filter="portes">Portes ({n_p})</button>
      <button type="button" role="tab" aria-selected="false" data-filter="serrures">Serrures ({n_s})</button>
      <button type="button" role="tab" aria-selected="false" data-filter="connectees">Connectées ({n_c})</button>
    </div>
    <div class="brand-cards" id="brand-wall">{"".join(brand_card(b) for b in BRAND_DATA)}</div>
  </div>
</section>
''' + cta_block("Votre marque n'est pas listée ?", "Nous intervenons sur l'ensemble des fabricants du marché français.") + "</main>\n" + footer()
write("marques/index.html", html_, "0.8")

for b in BRAND_DATA:
    slug, name, logo, cats, origin, desc = b
    prods = products_of(name)
    is_door = "portes" in cats
    prest = "remplacement" if is_door else "serrure"
    others = [o for o in BRAND_DATA if o[0] != slug and set(o[3]) & set(cats)][:8]
    services = []
    if is_door:
        services += [("door", f"Pose de porte blindée {name}", "Prise de mesures, fabrication sur mesure, dépose de l'ancienne porte et pose en une journée."),
                     ("tool", "Réglages et entretien", "Réglage des paumelles, de la serrure et des joints pour un fonctionnement durable.")]
    if "serrures" in cats:
        services += [("lock", f"Installation de serrure {name}", "Serrure multipoints en applique ou encastrée, adaptée à votre porte."),
                     ("key", "Changement de cylindre", "Remplacement du cylindre après une perte de clés ou un déménagement.")]
    if "connectees" in cats:
        services += [("smart", f"Installation {name}", "Pose, paramétrage et prise en main de votre serrure connectée."),
                     ("shield", "Conseil sécurité", "Vérification de la serrure et de la porte sur lesquelles la serrure connectée est installée.")]
    services.append(("file", "Devis gratuit", "Visite technique et devis écrit et détaillé, sans engagement."))
    svc = "".join(f'<div class="feature"><span class="ico">{I[i]}</span><h3>{E(t)}</h3><p>{d}</p></div>' for i, t, d in services[:3])
    prod_html = (f'<div class="products cols-3">{"".join(product_card(p) for p in prods)}</div>' if prods else
                 f'<div class="empty"><strong>Les modèles {E(name)} sont disponibles sur devis.</strong><br>Indiquez-nous le modèle souhaité : nous vous conseillons et établissons un devis gratuit.</div>')
    lg = f'<span class="brand-hero-logo">{logo_img(logo, name, lazy=False)}</span>' if logo else ""
    title_kw = "Porte blindée" if is_door else ("Serrure connectée" if cats == ["connectees"] else "Serrure")
    html_ = head(f"{title_kw} {name} : pose et installation | {NAME}",
                 f"{title_kw} {name} : fourniture, pose et installation par un spécialiste. {desc[:110]}… Devis gratuit.",
                 f"marques/{slug}.html", crumbs_ld([("Accueil", "/"), ("Marques", "/marques/"), (name, f"/marques/{slug}.html")])) + header("marques") + f'''
<section class="page-hero brand-hero">
  <img class="bg" src="/assets/img/photos/{"cle-serrure-porte-blindee" if is_door else "changement-cylindre"}.webp" alt="" aria-hidden="true">
  <div class="container brand-hero-grid">
    <div>
      <nav class="crumbs" aria-label="Fil d'Ariane"><a href="/">Accueil</a><span>/</span><a href="/marques/">Marques</a><span>/</span><span>{E(name)}</span></nav>
      <h1>{title_kw} {E(name)}</h1>
      <p>{E(desc)}</p>
      <div class="hero-actions" style="margin:28px 0 0">
        <a class="btn btn-red" href="{devis_href(name, prest)}">Devis gratuit {name} {I["arrow"]}</a>
        <a class="btn btn-ghost" href="tel:{PHONE_TEL}" data-track="clic_appel">{I["phone"]} {PHONE}</a>
        <button class="btn btn-ghost js-print" type="button">{I["file"]} Catalogue PDF</button>
      </div>
    </div>
    {lg}
  </div>
</section>
<main id="main">
<section class="section">
  <div class="container">
    <div class="head"><div><span class="kicker">{E(name)}</span><h2>Les modèles {E(name)} que nous installons.</h2></div>
      <p>{"Origine : " + origin + ". " if origin else ""}Chaque fabricant décline de nombreuses versions : nous vous présentons les modèles adaptés lors de la visite technique.</p></div>
    {prod_html}
  </div>
</section>
{brand_compare(prods)}
{brand_finishes(name) if is_door else ""}
<section class="section section-sand">
  <div class="container">
    <div class="head"><div><span class="kicker">Nos services</span><h2>Votre projet {E(name)}, de A à Z.</h2></div>
      <p>Installateur indépendant, nous ne sommes pas le fabricant : nous assurons le conseil, la fourniture et la pose, avec une garantie sur nos travaux.</p></div>
    <div class="feature-row three">{svc}</div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="head"><div><span class="kicker">À comparer</span><h2>Autres marques.</h2></div><p>Comparez avant de choisir : nous installons aussi ces fabricants.</p></div>
    <div class="brand-cards">{"".join(brand_card(o) for o in others)}</div>
  </div>
</section>
''' + cta_block() + "</main>\n" + footer()
    write(f"marques/{slug}.html", html_, "0.7")

# ======================================================== PRODUITS
for p in ALL_PRODUCTS:
    is_door = p["kind_label"] == "porte"
    brand = BRAND_BY_NAME.get(p["brand"])
    label = (p["brand"] + " – " if p["brand"] != "Toutes marques" else "") + p["name"]
    prest = ("blindage" if p.get("type") == "blindage" else "remplacement") if is_door else "serrure"
    cert = CERT_TEXT.get(p.get("cert"), "")
    related = [q for q in ALL_PRODUCTS if q is not p and q["kind_label"] == p["kind_label"] and (q.get("cert") == p.get("cert") or q["brand"] == p["brand"])][:3]
    included = (["Visite technique et prise de mesures", "Fabrication aux dimensions exactes", "Dépose et évacuation de l'ancienne porte",
                 "Pose, réglages et nettoyage du chantier", "Remise des clés, de la carte de propriété et du certificat"]
                if is_door and p.get("type") != "blindage" else
                ["Diagnostic de la porte existante", "Tôle d'acier et cornières anti-pince", "Paumelles renforcées", "Serrure multipoints", "Réglages et nettoyage"]
                if is_door else
                ["Diagnostic de la porte et de la serrure", "Fourniture du modèle choisi", "Pose et réglages", "Remise des clés et de la carte de propriété", "Explications d'utilisation"])
    blogo = f'<a class="pd-logo" href="/marques/{brand[0]}.html">{logo_img(brand[2], p["brand"], lazy=False)}</a>' if brand and brand[2] else ""
    brand_link = f'<a href="/marques/{brand[0]}.html">{E(p["brand"])}</a>' if brand else E(p["brand"])
    price = p.get("price") or "Sur devis"
    specs_rows = "".join(f"<li>{I['check']} {s}</li>" for s in p["specs"])
    html_ = head(f"{label} – fourniture et pose | {NAME}",
                 f"{label} : {p['desc']} Budget indicatif posé : {price}. Devis gratuit.",
                 f"produits/{p['slug']}.html",
                 crumbs_ld([("Accueil", "/"), ("Portes blindées" if is_door else "Serrures", "/portes-blindees.html" if is_door else "/serrures.html"), (p["name"], f"/produits/{p['slug']}.html")])) + header("portes" if is_door else "serrures") + f'''
<main id="main">
<section class="pd">
  <div class="container">
    <nav class="crumbs dark" aria-label="Fil d'Ariane"><a href="/">Accueil</a><span>/</span><a href="{"/portes-blindees.html" if is_door else "/serrures.html"}">{"Portes blindées" if is_door else "Serrures"}</a><span>/</span><span>{E(p["name"])}</span></nav>
    <div class="pd-grid">
      <div class="pd-visual">{('<span class="cert-tag">' + p["badge"] + '</span>') if p.get("badge") else ""}<span data-visual="{p["id"]}"></span></div>
      <div class="pd-info">
        {blogo}
        <div class="product-brand">{brand_link}</div>
        <h1>{E(p["name"])}</h1>
        <p class="pd-desc">{E(p["desc"])}</p>
        {f'<p class="pd-cert">{I["shield"]} {cert[0].upper() + cert[1:]}.</p>' if cert else ""}
        <ul class="pd-specs">{specs_rows}</ul>
        <div class="pd-price"><span>Budget indicatif fourniture et pose</span><strong>{price}</strong><small>Prix variable selon dimensions et finitions — devis gratuit après visite.</small></div>
        <div class="pd-actions">
          <a class="btn btn-red" href="{devis_href(label, prest)}">Demander un devis {I["arrow"]}</a>
          <a class="btn btn-line" href="tel:{PHONE_TEL}" data-track="clic_appel">{I["phone"]} {PHONE}</a>
          {wa_btn()}
        </div>
        <label class="cmp-check big"><input type="checkbox" data-compare="{p["id"]}"> Ajouter au comparateur</label>
      </div>
    </div>
  </div>
</section>
<section class="section section-sand">
  <div class="container split-2">
    <div>
      <span class="kicker">Inclus</span>
      <h2>Ce que comprend notre prestation.</h2>
      <ul class="points compact">{"".join(f'<li><span class="n">{I["check"]}</span><div><strong>{x}</strong></div></li>' for x in included)}</ul>
    </div>
    <div>
      <span class="kicker">Bon à savoir</span>
      <h2>Avant de choisir.</h2>
      <p class="muted">Chaque fabricant propose plusieurs versions d'une même gamme (certification, dimensions, finitions). Lors de la visite, nous vérifions l'état de votre ouverture et vous indiquons la version exacte et sa certification sur le devis.</p>
      <p><a class="arrow-link" href="/guides/{"certification-a2p-bp1-bp2-bp3" if is_door else "choisir-serrure-haute-securite"}.html">{"Comprendre la certification A2P" if is_door else "Bien choisir sa serrure"} {I["arrow"]}</a></p>
      <p><a class="arrow-link" href="/simulateur.html">Estimer mon budget {I["arrow"]}</a></p>
    </div>
  </div>
</section>
{f"""<section class="section"><div class="container"><div class="head"><div><span class="kicker">À comparer</span><h2>Modèles similaires.</h2></div><p>D'autres solutions au même niveau de sécurité ou de la même marque.</p></div><div class="products cols-3">{"".join(product_card(q) for q in related)}</div></div></section>""" if related else ""}
''' + cta_block() + "</main>\n" + footer()
    write(f"produits/{p['slug']}.html", html_, "0.6")

# ======================================================== GUIDES
def guide_card(g):
    slug, title, desc, photo, mins, body = g
    return f'''<a class="guide-card" href="/guides/{slug}.html">
  <span class="gc-img"><img src="/assets/img/photos/{photo}.webp" alt="" loading="lazy"></span>
  <span class="gc-body"><small>{mins} min de lecture</small><strong>{E(title)}</strong><span>{E(desc)}</span></span>
</a>'''

html_ = head(f"Guides et conseils porte blindée et serrure | {NAME}",
             "Nos guides pour bien choisir votre porte blindée et votre serrure : prix, certification A2P, assurance, blindage ou bloc-porte.",
             "guides/", crumbs_ld([("Accueil", "/"), ("Guides", "/guides/")])) + header("guides") + page_hero(
    "Guides", "Guides &amp; conseils.", "Prix, certifications, assurance : tout ce qu'il faut savoir avant de changer de porte ou de serrure.", "serrurier-conseil-clients") + f'''
<main id="main"><section class="section"><div class="container"><div class="guide-grid">{"".join(guide_card(g) for g in GUIDES)}</div></div></section>
''' + cta_block() + "</main>\n" + footer()
write("guides/index.html", html_, "0.7")

for g in GUIDES:
    slug, title, desc, photo, mins, body = g
    others = [o for o in GUIDES if o[0] != slug][:3]
    ld = '<script type="application/ld+json">' + json.dumps({
        "@context": "https://schema.org", "@type": "Article", "headline": title, "description": desc,
        "image": f"{DOMAIN}/assets/img/photos/{photo}.webp", "dateModified": TODAY,
        "author": {"@type": "Organization", "name": NAME}, "publisher": {"@type": "Organization", "name": NAME},
        "mainEntityOfPage": f"{DOMAIN}/guides/{slug}.html"}, ensure_ascii=False) + "</script>\n"
    html_ = head(f"{title} | {NAME}", desc, f"guides/{slug}.html",
                 ld + crumbs_ld([("Accueil", "/"), ("Guides", "/guides/"), (title, f"/guides/{slug}.html")]), image=photo) + header("guides") + page_hero(
        title.split(":")[0].split("?")[0].strip(), E(title), E(desc), photo, trail=[("Guides", "/guides/")]) + f'''
<main id="main">
<section class="section">
  <div class="container article-layout">
    <article class="prose article">
      <p class="meta">{mins} min de lecture · Mis à jour le {datetime.date.today().strftime("%d/%m/%Y")}</p>
      {body}
    </article>
    <div class="article-aside">{aside_card()}</div>
  </div>
</section>
<section class="section section-sand"><div class="container"><div class="head"><div><span class="kicker">À lire aussi</span><h2>Autres guides.</h2></div><p></p></div><div class="guide-grid">{"".join(guide_card(o) for o in others)}</div></div></section>
''' + cta_block() + "</main>\n" + footer()
    write(f"guides/{slug}.html", html_, "0.7")

# ======================================================== ZONES
def zone_link(z):
    return f'<a class="zone-chip" href="/zones/{z["slug"]}.html">{E(z["name"])} <small>{z["cp"]}</small></a>'

letters = {}
for z in sorted(ZONES, key=lambda z: slugify(z["name"])):
    letters.setdefault(slugify(z["name"])[0].upper(), []).append(z)
big = sorted(ZONES, key=lambda z: -z["pop"])[:12]
zones_html = (f'<div class="zone-group"><h2>Principales villes</h2><div class="zone-list">{"".join(zone_link(z) for z in big)}</div></div>' +
              "".join(f'<div class="zone-group"><h2>{l}</h2><div class="zone-list">{"".join(zone_link(z) for z in zs)}</div></div>' for l, zs in letters.items()))
html_ = head(f"Porte blindée dans le Var (83) : les {len(ZONES)} communes | {NAME}",
             f"Ouverture de porte blindée sans dégâts, dépannage, déblocage et pose de portes blindées dans les {len(ZONES)} communes du Var (83). Prix annoncé avant intervention.",
             "zones/", crumbs_ld([("Accueil", "/"), ("Zones d'intervention", "/zones/")])) + header("") + page_hero(
    "Zones d'intervention", "Tout le Var (83)", f"Ouverture, dépannage, déblocage et pose de portes blindées dans les {len(ZONES)} communes du Var, de Toulon à Fréjus, de Hyères à Draguignan.", "serrurier-ouverture-porte") + f'''
<main id="main"><section class="section"><div class="container">{zones_html}</div></section>
''' + cta_block() + "</main>\n" + footer()
write("zones/index.html", html_, "0.8")

# ======================================================== SERVICES D'URGENCE
URGENCES = [
  ("ouverture-porte-blindee", "Ouverture de porte blindée", "Ouverture de porte blindée sans dégâts",
   "Porte claquée, clés perdues, volées ou oubliées à l'intérieur : nous ouvrons votre porte blindée par des techniques fines, sans casse, dans la grande majorité des cas.",
   "serrurier-ouverture-porte", "ouverture",
   [("Porte claquée", "La porte s'est refermée derrière vous, sans être verrouillée à clé : c'est la situation la plus simple, l'ouverture est presque toujours possible sans aucune trace."),
    ("Porte fermée à clé", "Les pênes de la serrure multipoints sont sortis : l'ouverture se fait par le cylindre ou la serrure, avec des techniques adaptées à leur niveau de sécurité."),
    ("Clés perdues ou volées", "Après l'ouverture, nous vous conseillons de remplacer le cylindre : quelqu'un pourrait posséder vos clés."),
    ("Clé cassée ou tournant dans le vide", "Extraction du morceau de clé et ouverture, puis remplacement du cylindre si nécessaire.")],
   [("Pourquoi faire appel à un spécialiste ?", "Une porte blindée associe une serrure multipoints, un cylindre haute sécurité et un bâti renforcé. Une ouverture en force abîme la porte et le bâti, et peut coûter bien plus cher que l'intervention elle-même. Un spécialiste connaît les serrures Fichet, Picard, Bricard, Vachette, Mul-T-Lock et les autres marques du marché, et choisit la technique adaptée."),
    ("Sans dégâts : dans quels cas ?", "Dans la grande majorité des situations, l'ouverture se fait sans aucune dégradation de la porte. Certains cylindres très haute sécurité ne permettent pas d'ouverture fine : dans ce cas, nous vous l'expliquons avant d'intervenir et la solution (en général le remplacement du cylindre) vous est chiffrée avant de commencer."),
    ("Prix annoncé avant l'intervention", "Le tarif dépend de la situation (porte claquée ou fermée à clé) et du type de serrure. Il vous est annoncé au téléphone, puis confirmé par un devis écrit sur place avant de commencer. Aucune surprise sur la facture."),
    ("Justificatif de domicile", "Pour votre sécurité, nous demandons une pièce d'identité et un justificatif de domicile. C'est une règle de base de la profession.")]),
  ("depannage-porte-blindee", "Dépannage de porte blindée", "Dépannage de porte blindée",
   "Serrure qui force, clé qui tourne mal, porte qui frotte ou ne ferme plus correctement : nous diagnostiquons et réparons votre porte blindée, toutes marques.",
   "changement-cylindre", "ouverture",
   [("Serrure qui force", "Pênes mal alignés avec les gâches, mécanisme encrassé ou usé : réglage et entretien de la serrure multipoints."),
    ("Clé cassée dans le cylindre", "Extraction sans démontage de la porte, puis remplacement du cylindre si besoin."),
    ("Porte qui frotte ou s'affaisse", "Réglage des paumelles et du vantail : une porte blindée est lourde, elle doit être réglée régulièrement."),
    ("Cylindre usé ou endommagé", "Remplacement par un cylindre haute sécurité adapté à votre serrure, avec carte de propriété.")],
   [("Toutes marques de portes blindées", "Nous intervenons sur les portes et serrures Fichet, Picard Serrures, Bricard, Héraclès, Tordjman, Vachette, Mul-T-Lock, Mottura et les autres marques du marché. Nous disposons des cylindres les plus courants."),
    ("Réparer plutôt que remplacer", "La plupart des pannes se règlent par un réglage, un entretien ou le remplacement d'une pièce. Nous ne vous proposons le remplacement de la serrure ou de la porte que lorsqu'il est réellement nécessaire."),
    ("Après une effraction", "Mise en sécurité provisoire, remplacement du cylindre ou de la serrure, et devis détaillé à transmettre à votre assurance."),
    ("Prix annoncé avant l'intervention", "Diagnostic, tarif annoncé et devis écrit avant toute réparation.")]),
  ("deblocage-porte-blindee", "Déblocage de porte blindée", "Déblocage de porte blindée sans dégâts",
   "Serrure multipoints bloquée, pênes coincés, cylindre grippé, porte qui ne s'ouvre plus de l'intérieur ou de l'extérieur : nous débloquons votre porte blindée sans la dégrader.",
   "serrure-multipoints-porte-blindee", "ouverture",
   [("Serrure multipoints bloquée", "Un pêne coincé dans sa gâche ou une tringle grippée peut bloquer toute la serrure : déblocage puis réglage."),
    ("Cylindre grippé", "Clé qui n'entre plus ou ne tourne plus : déblocage, nettoyage ou remplacement du cylindre."),
    ("Porte bloquée de l'intérieur", "Vous êtes enfermé ? Nous intervenons de l'extérieur pour libérer la porte."),
    ("Porte voilée ou affaissée", "Les pênes frottent et la porte se bloque : réglage des paumelles et des gâches.")],
   [("Ne forcez pas", "Forcer sur la clé ou la poignée peut casser la clé dans le cylindre ou endommager la serrure. Appelez-nous avant d'en arriver là : un déblocage est souvent simple pour un spécialiste."),
    ("Comprendre la cause", "Après le déblocage, nous identifions l'origine du problème (usure, réglage, encrassement) et la corrigeons pour éviter que la porte se bloque à nouveau."),
    ("Toutes marques", "Serrures Fichet, Picard, Bricard, Vachette, Mul-T-Lock, Mottura et autres : nous connaissons leurs mécanismes."),
    ("Prix annoncé avant l'intervention", "Tarif annoncé au téléphone et devis écrit sur place avant de commencer.")]),
]
for slug, crumb, h1, lead, photo, prest, cases, blocks in URGENCES:
    others = [u for u in URGENCES if u[0] != slug]
    big = sorted(ZONES, key=lambda z: -z["pop"])[:16]
    cases_html = "".join(f'<div class="feature"><h3>{t}</h3><p>{d}</p></div>' for t, d in cases)
    blocks_html = "".join(f"<h2>{t}</h2><p>{d}</p>" for t, d in blocks)
    ld = '<script type="application/ld+json">' + json.dumps({
        "@context": "https://schema.org", "@type": "Service", "serviceType": crumb, "areaServed": ZONE,
        "provider": {"@type": "Locksmith", "name": NAME, "telephone": PHONE_TEL, "url": DOMAIN + "/"}}, ensure_ascii=False) + "</script>\n"
    html_ = head(f"{h1} dans le Var (83) | {NAME}", f"{lead} Intervention dans tout le Var (83), prix annoncé avant intervention.",
                 f"{slug}.html", ld + crumbs_ld([("Accueil", "/"), (crumb, f"/{slug}.html")]), image=photo) + header("ouverture" if slug.startswith("ouverture") else "") + f'''
<section class="page-hero">
  <img class="bg" src="/assets/img/photos/{photo}.webp" alt="" aria-hidden="true">
  <div class="container">
    <nav class="crumbs" aria-label="Fil d'Ariane"><a href="/">Accueil</a><span>/</span><span>{crumb}</span></nav>
    <h1>{h1}</h1>
    <p>{lead}</p>
    <div class="hero-actions" style="margin:32px 0 0">
      <a class="btn btn-white" href="tel:{PHONE_TEL}" data-track="clic_appel">{I["phone"]} Appeler le {PHONE}</a>
      {wa_btn("btn btn-ghost", "Envoyer une photo")}
    </div>
  </div>
</section>
<main id="main">
<section class="section">
  <div class="container">
    <div class="head"><div><span class="kicker">Situations</span><h2>Nous intervenons pour</h2></div><p>Toutes marques de portes blindées et de serrures, dans tout le Var.</p></div>
    <div class="feature-row">{cases_html}</div>
  </div>
</section>
<section class="section section-sand">
  <div class="container article-layout">
    <div class="prose">{blocks_html}</div>
    <div class="article-aside">{aside_card("Besoin d'une intervention ?", "Tarif annoncé au téléphone, devis écrit avant de commencer.")}</div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="head"><div><span class="kicker">Aussi</span><h2>Nos autres interventions</h2></div><p></p></div>
    <div class="urgent-grid two">{"".join(f'<a class="urgent-card" href="/{u[0]}.html"><h3>{u[1]}</h3><p>{u[3]}</p><span class="go">En savoir plus {I["arrow"]}</span></a>' for u in others)}</div>
    <div class="head" style="margin-top:80px"><div><span class="kicker">Dans tout le Var</span><h2>{crumb} près de chez vous</h2></div><p></p></div>
    <div class="zone-list">{"".join(zone_link(z) for z in big)}<a class="zone-chip more" href="/zones/">Les {len(ZONES)} communes {I["arrow"]}</a></div>
  </div>
</section>
''' + cta_block("Porte blindée bloquée ou claquée ?", "Appelez-nous : tarif annoncé avant intervention, ouverture sans dégâts.") + "</main>\n" + footer()
    write(f"{slug}.html", html_, "0.9")

# ======================================================== SIMULATEUR
def radio(name, value, label, sub="", icon=None, checked=False):
    ico = I[icon] if icon else ""
    return f'<label class="opt"><input type="radio" name="{name}" value="{value}"{" checked" if checked else ""}><span>{ico}<strong>{label}</strong>{f"<small>{sub}</small>" if sub else ""}</span></label>'

def check(name, value, label, sub=""):
    return f'<label class="opt"><input type="checkbox" name="{name}" value="{value}"><span><strong>{label}</strong>{f"<small>{sub}</small>" if sub else ""}</span></label>'

html_ = head(f"Simulateur de prix porte blindée et serrure | {NAME}",
             "Estimez en une minute le prix de votre porte blindée, blindage de porte ou serrure, fourniture et pose comprises. Gratuit et sans engagement.",
             "simulateur.html", crumbs_ld([("Accueil", "/"), ("Simulateur de prix", "/simulateur.html")])) + header("prix") + page_hero(
    "Simulateur de prix", "Estimez le prix de votre projet.", "Quatre questions, une fourchette de prix fourniture et pose comprises. Gratuit, anonyme et sans engagement.", "pose-serrure-porte-blindee") + f'''
<main id="main">
<section class="section">
  <div class="container sim-layout">
    <form class="sim" id="simulateur" novalidate>
      <fieldset class="sim-step">
        <legend><span class="step-n"></span> Que souhaitez-vous faire ?</legend>
        <div class="opts four">
          {radio("projet", "porte", "Porte blindée", "Bloc-porte neuf", "door", True)}
          {radio("projet", "blindage", "Blindage", "Renforcer ma porte", "shield")}
          {radio("projet", "serrure", "Serrure", "Multipoints", "lock")}
          {radio("projet", "cylindre", "Cylindre", "Changer le barillet", "key")}
        </div>
      </fieldset>
      <fieldset class="sim-step" data-for="porte">
        <legend><span class="step-n"></span> Quel niveau de sécurité ?</legend>
        <div class="opts four">
          {radio("niveau", "none", "Non certifiée", "Budget minimal")}
          {radio("niveau", "BP1", "A2P BP1", "5 min · appartement", None, True)}
          {radio("niveau", "BP2", "A2P BP2", "10 min · RDC, maison")}
          {radio("niveau", "BP3", "A2P BP3", "15 min · haute valeur")}
        </div>
      </fieldset>
      <fieldset class="sim-step" data-for="serrure">
        <legend><span class="step-n"></span> Quelle certification de serrure ?</legend>
        <div class="opts three">
          {radio("serrure", "A2P1", "A2P★", "5 min")}
          {radio("serrure", "A2P2", "A2P★★", "10 min", None, True)}
          {radio("serrure", "A2P3", "A2P★★★", "15 min")}
        </div>
      </fieldset>
      <fieldset class="sim-step">
        <legend><span class="step-n"></span> Type de logement</legend>
        <div class="opts three">
          {radio("logement", "appartement", "Appartement", "Porte palière", "building", True)}
          {radio("logement", "maison", "Maison", "Porte sur l'extérieur", "home")}
          {radio("logement", "immeuble", "Copropriété", "Hall, cave, local", "users")}
        </div>
      </fieldset>
      <fieldset class="sim-step" data-for="porte blindage">
        <legend><span class="step-n"></span> Options</legend>
        <div class="opts two">
          {check("options", "finition", "Finition haut de gamme", "Bois massif, laqué, moulures")}
          {check("options", "dimensions", "Dimensions hors standard", "Ouverture large, haute ou cintrée")}
          {check("options", "isolation", "Isolation thermique renforcée", "Porte donnant sur l'extérieur")}
          {check("options", "connectee", "Serrure connectée", "Code, badge ou smartphone")}
        </div>
      </fieldset>
    </form>
    <aside class="sim-result" id="sim-result" aria-live="polite">
      <span class="kicker">Votre estimation</span>
      <div class="sim-amount"><strong id="sim-min">–</strong><span>à</span><strong id="sim-max">–</strong></div>
      <p class="sim-label" id="sim-label">Fourniture et pose, TTC</p>
      <ul class="sim-incl" id="sim-incl"></ul>
      <a class="btn btn-red btn-block" id="sim-cta" href="/#devis">Recevoir un devis précis {I["arrow"]}</a>
      <a class="btn btn-line btn-block" href="tel:{PHONE_TEL}" data-track="clic_appel">{I["phone"]} {PHONE}</a>
      <p class="fine">Estimation indicative fondée sur les prix moyens constatés. Le prix définitif dépend du modèle, des dimensions et de l'état de l'ouverture : seul le devis établi après visite fait foi.</p>
    </aside>
  </div>
</section>
''' + cta_block() + "</main>\n" + footer()
write("simulateur.html", html_, "0.9")

# ======================================================== RÉALISATIONS
GALLERY = [
    ("serrure-multipoints-porte-blindee", "Serrure 5 points sur porte blindée", "porte"),
    ("pose-serrure-porte-blindee", "Pose d'un boîtier multipoints", "porte"),
    ("cle-serrure-porte-blindee", "Porte blindée à serrure multipoints", "porte"),
    ("protege-cylindre-porte-entree", "Protège-cylindre sur porte d'entrée", "serrure"),
    ("changement-cylindre", "Changement de cylindre", "serrure"),
    ("serrurier-ouverture-porte", "Intervention sur serrure", "serrure"),
    ("porte-effraction", "Porte fracturée avant intervention", "effraction"),
    ("porte-vitree-mise-en-securite", "Mise en sécurité provisoire", "effraction"),
    ("porte-vitree-reparee", "Porte réparée après effraction", "effraction"),
]
gal = "".join(f'<figure data-cat="{c}"><img src="/assets/img/photos/{f}.webp" alt="{E(t)}" loading="lazy"><figcaption>{E(t)}</figcaption></figure>' for f, t, c in GALLERY)
html_ = head(f"Nos réalisations : portes blindées et serrures posées | {NAME}",
             "Photos de nos chantiers : pose de portes blindées, serrures multipoints, protège-cylindres et mises en sécurité après effraction.",
             "realisations.html", crumbs_ld([("Accueil", "/"), ("Réalisations", "/realisations.html")])) + header("realisations") + page_hero(
    "Réalisations", "Nos réalisations.", "Des chantiers soignés, du premier au dernier point de fermeture. Faites glisser le curseur pour voir l'avant / après.", "protege-cylindre-porte-entree") + f'''
<main id="main">
<section class="section">
  <div class="container split">
    <div class="ba reveal" id="ba">
      <img src="/assets/img/photos/porte-vitree-reparee.webp" alt="Après : porte réparée" class="ba-after">
      <div class="ba-before"><img src="/assets/img/photos/porte-vitree-mise-en-securite.webp" alt="Avant : porte mise en sécurité provisoirement"></div>
      <span class="ba-tag l">Avant</span><span class="ba-tag r">Après</span>
      <input type="range" min="0" max="100" value="50" aria-label="Comparer avant et après">
      <span class="ba-handle" aria-hidden="true"></span>
    </div>
    <div class="reveal">
      <span class="kicker">Avant / après</span>
      <h2>Après une effraction : sécuriser, puis réparer.</h2>
      <p class="muted">Le soir même, l'accès est fermé provisoirement pour protéger le logement. Une fois l'accord de l'assurance obtenu, la porte est remplacée et l'ensemble est remis en état.</p>
      <ul class="points">
        <li><span class="n">{I["shield"]}</span><div><strong>Mise en sécurité immédiate</strong><span>Panneau de fermeture, cylindre provisoire.</span></div></li>
        <li><span class="n">{I["file"]}</span><div><strong>Devis pour l'assurance</strong><span>Photos et devis détaillé à transmettre à votre assureur.</span></div></li>
        <li><span class="n">{I["tool"]}</span><div><strong>Remise en état</strong><span>Remplacement définitif et réglages.</span></div></li>
      </ul>
    </div>
  </div>
</section>
<section class="section section-sand">
  <div class="container">
    <div class="head"><div><span class="kicker">Galerie</span><h2>Sur le terrain.</h2></div><p>Portes blindées, serrures et interventions après effraction.</p></div>
    <div class="tabs" role="tablist" aria-label="Filtrer les photos">
      <button type="button" role="tab" aria-selected="true" data-gal="all">Toutes</button>
      <button type="button" role="tab" aria-selected="false" data-gal="porte">Portes blindées</button>
      <button type="button" role="tab" aria-selected="false" data-gal="serrure">Serrures</button>
      <button type="button" role="tab" aria-selected="false" data-gal="effraction">Après effraction</button>
    </div>
    <div class="masonry" id="gallery">{gal}</div>
  </div>
</section>
''' + cta_block("Votre porte sera la prochaine ?", "Visite technique et devis gratuits, sans engagement.") + "</main>\n" + footer()
write("realisations.html", html_, "0.7")

# ======================================================== À PROPOS
html_ = head(f"Qui sommes-nous | {NAME}",
             f"{NAME} : installateur indépendant spécialisé dans les portes blindées et les serrures haute sécurité. Notre méthode, nos engagements.",
             "a-propos.html", crumbs_ld([("Accueil", "/"), ("Qui sommes-nous", "/a-propos.html")])) + header("") + page_hero(
    "Qui sommes-nous", "Un spécialiste de la porte d'entrée.", "Nous avons fait de la porte blindée et de la serrure haute sécurité notre métier : conseil, pose et suivi.", "serrurier-conseil-clients") + f'''
<main id="main">
<section class="section">
  <div class="container split">
    <div class="split-photo reveal"><img src="/assets/img/photos/serrurier-conseil-clients.webp" alt="Technicien conseillant des clients" loading="lazy"></div>
    <div class="reveal">
      <span class="kicker">Notre métier</span>
      <h2>Indépendants, pour vous conseiller objectivement.</h2>
      <p class="muted">{NAME} est un installateur indépendant. Nous ne sommes liés à aucun fabricant : notre rôle est de vous proposer la porte ou la serrure adaptée à votre logement, à votre budget et aux exigences de votre assurance, parmi les grandes marques du marché français.</p>
      <p class="muted">Nous intervenons sur {ZONE}, de la visite technique jusqu'à la remise des clés.</p>
      <ul class="points">
        <li><span class="n">{I["award"]}</span><div><strong>Conseil indépendant</strong><span>{len(BRAND_DATA)} marques comparées, aucune imposée.</span></div></li>
        <li><span class="n">{I["file"]}</span><div><strong>Transparence</strong><span>Devis écrit et détaillé avant tout engagement, prix ferme.</span></div></li>
        <li><span class="n">{I["tool"]}</span><div><strong>Travail soigné</strong><span>Protection des lieux, évacuation des gravats, réglages précis.</span></div></li>
        <li><span class="n">{I["shield"]}</span><div><strong>Suivi</strong><span>Un interlocuteur unique, joignable après la pose.</span></div></li>
      </ul>
    </div>
  </div>
</section>
<section class="section section-sand">
  <div class="container">
    <div class="head"><div><span class="kicker">Nos engagements</span><h2>Ce sur quoi vous pouvez compter.</h2></div><p></p></div>
    <div class="feature-row">
      <div class="feature"><span class="ico">{I["euro"]}</span><h3>Devis gratuit</h3><p>Visite technique et devis sans engagement.</p></div>
      <div class="feature"><span class="ico">{I["shield"]}</span><h3>Matériel certifié</h3><p>Portes et serrures certifiées A2P ou EN 1627.</p></div>
      <div class="feature"><span class="ico">{I["clock"]}</span><h3>Pose en 1 jour</h3><p>Pour une porte blindée palière standard.</p></div>
      <div class="feature"><span class="ico">{I["file"]}</span><h3>Documents remis</h3><p>Facture, certificat et carte de propriété.</p></div>
    </div>
  </div>
</section>
''' + cta_block() + "</main>\n" + footer()
write("a-propos.html", html_, "0.5")

# ======================================================== PLAN DU SITE & 404
def ul(items):
    return "<ul>" + "".join(f'<li><a href="{u}">{E(t)}</a></li>' for t, u in items) + "</ul>"
html_ = head(f"Plan du site | {NAME}", "Plan du site.", "plan-du-site.html") + header("") + page_hero(
    "Plan du site", "Plan du site.", "Toutes les pages du site.", "changement-cylindre") + f'''
<main id="main"><section class="section"><div class="container sitemap-cols">
<div><h2>Pages principales</h2>{ul([("Accueil", "/"), ("Portes blindées", "/portes-blindees.html"), ("Serrures", "/serrures.html"), ("Simulateur de prix", "/simulateur.html"), ("Réalisations", "/realisations.html"), ("Qui sommes-nous", "/a-propos.html"), ("Marques", "/marques/"), ("Guides", "/guides/"), ("Zones d'intervention", "/zones/"), ("Mentions légales", "/mentions-legales.html")])}
<h2>Guides</h2>{ul([(g[1], f"/guides/{g[0]}.html") for g in GUIDES])}</div>
<div><h2>Marques</h2>{ul([(b[1], f"/marques/{b[0]}.html") for b in BRAND_DATA])}</div>
<div><h2>Produits</h2>{ul([((p["brand"] + " – " if p["brand"] != "Toutes marques" else "") + p["name"], f"/produits/{p['slug']}.html") for p in ALL_PRODUCTS])}</div>
<div><h2>Zones</h2>{ul([(z["name"], f"/zones/{z['slug']}.html") for z in ZONES])}</div>
</div></section></main>
''' + footer()
write("plan-du-site.html", html_, "0.3")

html_ = head(f"Page introuvable | {NAME}", "Cette page n'existe pas.", "404.html", '  <meta name="robots" content="noindex">\n') + header("") + f'''
<main id="main"><section class="section"><div class="container" style="max-width:720px;text-align:center">
<span class="kicker">Erreur 404</span><h1>Cette page est introuvable.</h1>
<p class="muted">Elle a peut-être été déplacée. Voici quelques liens utiles :</p>
<div class="hero-actions" style="justify-content:center"><a class="btn btn-red" href="/">Accueil</a><a class="btn btn-line" href="/portes-blindees.html">Portes blindées</a><a class="btn btn-line" href="/serrures.html">Serrures</a></div>
</div></section></main>
''' + footer()
write("404.html", html_, index=False)


# ======================================================== CONFIGURATEUR
def cfg_radio(name, value, inner, checked=False, cls="opt"):
    return f'<label class="{cls}"><input type="radio" name="{name}" value="{value}"{" checked" if checked else ""}><span>{inner}</span></label>'

col_opts = "".join(cfg_radio("coloris", i, f'<i style="background:{c[2]}"></i><strong>{c[0]}</strong><small>{c[1]}</small>', i == 0, "opt sw") for i, c in enumerate(COLORIS))
pan_opts = "".join(cfg_radio("panneau", k, f'<span data-panel="{k}"></span><strong>{n}</strong>', k == "classic", "opt pan") for k, n, d in PANNEAUX if k != "plate")
poi_opts = "".join(cfg_radio("poignee", k, f'<strong>{n}</strong>', k == "alu") for k, n in POIGNEES)
niv_opts = "".join(cfg_radio("niveau", k, f'<strong>{n}</strong><small>{d}</small>', k == "BP1") for k, n, d, a, b in NIVEAUX)
opt_opts = "".join(f'<label class="opt"><input type="checkbox" name="options" value="{k}"><span><strong>{n}</strong><small>{d}</small></span></label>' for k, n, d, a, b in OPTIONS)
html_ = head(f"Configurateur de porte blindée | {NAME}",
             "Composez votre porte blindée : panneau, coloris RAL, poignée, certification A2P et options. Aperçu en direct et estimation du prix posé.",
             "configurateur.html", crumbs_ld([("Accueil", "/"), ("Configurateur", "/configurateur.html")])) + header("config") + f'''
<main id="main">
<section class="cfg" id="configurateur">
  <div class="cfg-stage">
    <div class="cfg-preview" id="cfg-preview" aria-live="polite"></div>
    <div class="cfg-summary">
      <span class="kicker">Votre porte</span>
      <p id="cfg-recap">—</p>
      <div class="sim-amount"><strong id="cfg-min">–</strong><span>à</span><strong id="cfg-max">–</strong></div>
      <p class="sim-label">Estimation fourniture et pose, TTC</p>
      <a class="btn btn-red btn-block" id="cfg-cta" href="/#devis">Recevoir un devis pour cette porte {I["arrow"]}</a>
    </div>
  </div>
  <form class="cfg-panel" id="cfg-form">
    <nav class="crumbs dark" aria-label="Fil d'Ariane"><a href="/">Accueil</a><span>/</span><span>Configurateur</span></nav>
    <h1>Configurez votre porte blindée</h1>
    <p class="muted">Choisissez l'habillage, le coloris, la poignée et le niveau de sécurité : votre porte se dessine en direct.</p>
    <fieldset><legend>1. Habillage extérieur</legend><div class="opts three pans">{pan_opts}</div></fieldset>
    <fieldset><legend>2. Coloris</legend><div class="sw-grid">{col_opts}</div></fieldset>
    <fieldset><legend>3. Poignée</legend><div class="opts four">{poi_opts}</div></fieldset>
    <fieldset><legend>4. Niveau de sécurité</legend><div class="opts four">{niv_opts}</div></fieldset>
    <fieldset><legend>5. Options</legend><div class="opts two">{opt_opts}</div></fieldset>
    <p class="fine">Aperçu non contractuel. Les coloris, habillages et options disponibles dépendent du fabricant et de la gamme : ils sont confirmés lors de la visite technique et sur le devis.</p>
  </form>
</section>
</main>
''' + footer()
write("configurateur.html", html_, "0.9")

# ======================================================== FINITIONS
pan_cards = "".join(f'<div class="fin-card"><span class="fin-visual" data-panel="{k}" data-color="#383e42" data-dark="#24282b"></span><strong>{n}</strong><p>{d}</p></div>' for k, n, d in PANNEAUX)
poi_cards = "".join(f'<div class="fin-card small"><span class="fin-visual" data-panel="modern" data-color="#e6e8e9" data-dark="#b9bfc4" data-handle="{k}"></span><strong>{n}</strong></div>' for k, n in POIGNEES)
opt_cards = "".join(f'<div class="feature"><h3>{n}</h3><p>{d}</p><p class="opt-price">+ {a} à {b} € posé</p></div>' for k, n, d, a, b in OPTIONS)
html_ = head(f"Finitions et coloris de portes blindées | {NAME}",
             "Habillages, coloris RAL, poignées et options pour votre porte blindée : nuancier, panneaux moulurés, contemporains ou vitrés.",
             "finitions.html", crumbs_ld([("Accueil", "/"), ("Finitions & coloris", "/finitions.html")])) + header("") + page_hero(
    "Finitions & coloris", "Finitions &amp; coloris", "Une porte blindée se personnalise comme une porte d'entrée : habillage, coloris, poignée et options. Voici les possibilités les plus courantes.", "cle-serrure-porte-blindee") + f'''
<main id="main">
<section class="section">
  <div class="container">
    <div class="head"><div><span class="kicker">Habillages</span><h2>Le panneau extérieur</h2></div><p>Côté palier ou côté rue, l'habillage donne son style à la porte. Le panneau intérieur peut être choisi séparément.</p></div>
    <div class="fin-grid">{pan_cards}</div>
  </div>
</section>
<section class="section section-sand">
  <div class="container">
    <div class="head"><div><span class="kicker">Nuancier</span><h2>Les coloris</h2></div><p>Les teintes RAL les plus demandées et les placages bois. D'autres teintes sont possibles selon les fabricants.</p></div>
    <div class="swatches big">{"".join(swatch(c) for c in COLORIS)}</div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="head"><div><span class="kicker">Poignées</span><h2>Garnitures</h2></div><p>Béquilles, plaques et rosaces de sécurité, assorties au style de la porte.</p></div>
    <div class="fin-grid four">{poi_cards}</div>
  </div>
</section>
<section class="section section-sand">
  <div class="container">
    <div class="head"><div><span class="kicker">Options</span><h2>Confort et isolation</h2></div><p>Suppléments indicatifs, fourniture et pose comprises.</p></div>
    <div class="feature-row three">{opt_cards}</div>
    <div class="hero-actions" style="margin:40px 0 0"><a class="btn btn-red" href="/configurateur.html">Configurer ma porte {I["arrow"]}</a></div>
  </div>
</section>
''' + cta_block() + "</main>\n" + footer()
write("finitions.html", html_, "0.7")

# ======================================================== COMPARATEUR
html_ = head(f"Comparateur de portes blindées et serrures | {NAME}",
             "Comparez côte à côte les portes blindées et serrures : certification, usage, caractéristiques et budget posé.",
             "comparateur.html", crumbs_ld([("Accueil", "/"), ("Comparateur", "/comparateur.html")])) + header("") + page_hero(
    "Comparateur", "Comparateur", "Comparez jusqu'à 3 modèles côte à côte. Ajoutez des modèles depuis les catalogues ou les pages marques.", "serrure-multipoints-porte-blindee") + f'''
<main id="main">
<section class="section">
  <div class="container">
    <div id="compare-view" class="compare-view"></div>
    <div class="hero-actions" style="margin:40px 0 0"><a class="btn btn-line" href="/portes-blindees.html">Ajouter une porte</a><a class="btn btn-line" href="/serrures.html">Ajouter une serrure</a><button class="btn btn-line" type="button" id="compare-clear">Vider le comparateur</button></div>
  </div>
</section>
''' + cta_block() + "</main>\n" + footer()
write("comparateur.html", html_, "0.4")

# ======================================================== PROFESSIONNELS
html_ = head(f"Professionnels, syndics et copropriétés | {NAME}",
             "Portes blindées, portes de caves et de locaux, contrôle d'accès et organigrammes de clés pour syndics, gestionnaires et bailleurs. Devis groupés.",
             "professionnels.html", crumbs_ld([("Accueil", "/"), ("Professionnels", "/professionnels.html")])) + header("") + page_hero(
    "Professionnels", "Syndics, gestionnaires &amp; bailleurs", "Un interlocuteur unique pour sécuriser les accès d'un immeuble ou d'un parc de logements : parties communes, logements, locaux techniques.", "porte-vitree-reparee") + f'''
<main id="main">
<section class="section">
  <div class="container">
    <div class="head"><div><span class="kicker">Nos prestations</span><h2>Pour les immeubles et les parcs de logements</h2></div><p>Interventions planifiées, devis groupés et suivi par un interlocuteur unique.</p></div>
    <div class="feature-row">
      <div class="feature"><span class="ico">{I["door"]}</span><h3>Portes palières en lot</h3><p>Remplacement coordonné de plusieurs portes palières avec un habillage extérieur identique, conforme au règlement de copropriété.</p></div>
      <div class="feature"><span class="ico">{I["building"]}</span><h3>Halls et parties communes</h3><p>Portes d'entrée d'immeuble, ventouses, interphones et contrôle d'accès par badge.</p></div>
      <div class="feature"><span class="ico">{I["lock"]}</span><h3>Caves et locaux</h3><p>Portes métalliques renforcées pour caves, locaux vélos, poubelles et techniques.</p></div>
      <div class="feature"><span class="ico">{I["key"]}</span><h3>Organigrammes de clés</h3><p>Un même passe pour les parties communes, des clés individuelles protégées pour chaque logement.</p></div>
    </div>
  </div>
</section>
<section class="section section-sand">
  <div class="container split-2">
    <div>
      <span class="kicker">Méthode</span>
      <h2>Comment nous travaillons</h2>
      <ul class="points compact">
        <li><span class="n">{I["check"]}</span><div><strong>Visite de l'immeuble et relevé de toutes les ouvertures</strong></div></li>
        <li><span class="n">{I["check"]}</span><div><strong>Devis détaillé par lot, présentable en assemblée générale</strong></div></li>
        <li><span class="n">{I["check"]}</span><div><strong>Planning d'intervention coordonné avec le gardien</strong></div></li>
        <li><span class="n">{I["check"]}</span><div><strong>Procès-verbal de fin de travaux et documents par logement</strong></div></li>
      </ul>
    </div>
    <div>
      <span class="kicker">Pour qui</span>
      <h2>Ils peuvent nous confier leurs accès</h2>
      <p class="muted">Syndics de copropriété, conseils syndicaux, gestionnaires locatifs, bailleurs, agences immobilières, commerces et bureaux.</p>
      <div class="hero-actions" style="margin-top:28px"><a class="btn btn-red" href="/?prestation=remplacement&produit=Projet%20professionnel%20%2F%20copropri%C3%A9t%C3%A9#devis">Demander un devis groupé {I["arrow"]}</a><a class="btn btn-line" href="mailto:{EMAIL}">{I["mail"]} {EMAIL}</a></div>
    </div>
  </div>
</section>
''' + cta_block() + "</main>\n" + footer()
write("professionnels.html", html_, "0.6")
