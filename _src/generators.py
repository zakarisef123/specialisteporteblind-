# Exécuté dans l'espace de noms de build.py (accès à head, header, footer, write, etc.)

CAT_LABEL = {"portes": "Portes blindées", "serrures": "Serrures & cylindres", "connectees": "Serrures connectées"}
DEP_LABEL = {"75": "Paris (75)", "92": "Hauts-de-Seine (92)", "93": "Seine-Saint-Denis (93)"}

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

groups = {}
for z in ZONES:
    groups.setdefault(z["dep"], []).append(z)
zones_html = "".join(f'<div class="zone-group"><h2>{DEP_LABEL.get(d, d)}</h2><div class="zone-list">{"".join(zone_link(z) for z in sorted(zs, key=lambda z: (len(z["name"]) if d == "75" else 0, z["name"])))}</div></div>' for d, zs in groups.items())
html_ = head(f"Zones d'intervention – porte blindée {ZONE} | {NAME}",
             f"Remplacement de porte blindée et changement de serrure à {ZONE} : {len(ZONES)} villes et arrondissements desservis. Devis gratuit.",
             "zones/", crumbs_ld([("Accueil", "/"), ("Zones d'intervention", "/zones/")])) + header("") + page_hero(
    "Zones d'intervention", "Nos zones d'intervention.", f"Nous intervenons dans {len(ZONES)} arrondissements et villes : {ZONE}. Votre ville n'est pas listée ? Appelez-nous.", "serrurier-ouverture-porte") + f'''
<main id="main"><section class="section"><div class="container">{zones_html}</div></section>
''' + cta_block() + "</main>\n" + footer()
write("zones/index.html", html_, "0.7")

PARIS_TXT = ("Dans les immeubles parisiens, la porte palière est souvent d'origine : bois massif, huisserie ancienne, serrure en applique fatiguée. "
             "Le remplacement par un bloc-porte blindé certifié permet de conserver un habillage extérieur conforme au style de l'immeuble tout en atteignant le niveau A2P BP1 ou BP2.")
HDS_TXT = ("Entre appartements en résidence, pavillons et maisons de ville, les besoins varient : porte palière à remplacer, porte d'entrée de maison à isoler "
           "et sécuriser, ou simple renforcement de la serrure. Nous vous conseillons la solution adaptée à votre logement.")

for z in ZONES:
    near = sorted((o for o in ZONES if o is not z), key=lambda o: dist(z, o))[:8]
    is_paris = z["dep"] == "75"
    local = ""
    if z["quartiers"]:
        local = (f"<p>Nous intervenons dans tous les quartiers du {E(z['name'])} — {', '.join(z['quartiers'][:-1])} et {z['quartiers'][-1]} — "
                 f"notamment autour de {', '.join(z['lieux'][:-1])} et {z['lieux'][-1]}.</p>")
    pop = f"{z['pop']:,}".replace(",", " ")
    feats = [p for p in PRODUCTS["doors"] if p.get("cert") in ("BP1", "BP2")][:3]
    zone_ld = '<script type="application/ld+json">' + json.dumps({
        "@context": "https://schema.org", "@type": "Service", "serviceType": "Remplacement de porte blindée et installation de serrure",
        "provider": {"@type": "Locksmith", "name": NAME, "telephone": PHONE_TEL, "url": DOMAIN + "/"},
        "areaServed": {"@type": "City", "name": z["name"], "postalCode": z["cp"]}}, ensure_ascii=False) + "</script>\n"
    html_ = head(f"Porte blindée {z['name']} ({z['cp']}) – pose et serrure A2P | {NAME}",
                 f"Remplacement de porte blindée, blindage de porte et changement de serrure à {z['name']} ({z['cp']}). Portes certifiées A2P, toutes marques. Visite et devis gratuits.",
                 f"zones/{z['slug']}.html", zone_ld + crumbs_ld([("Accueil", "/"), ("Zones", "/zones/"), (z["name"], f"/zones/{z['slug']}.html")])) + header("") + page_hero(
        z["name"], f"Porte blindée à {E(z['name'])}.",
        f"Remplacement de porte blindée, blindage de porte et serrures haute sécurité à {E(z['name'])} ({z['cp']}). Visite technique et devis gratuits.",
        "cle-serrure-porte-blindee" if is_paris else "pose-serrure-porte-blindee", trail=[("Zones", "/zones/")]) + f'''
<main id="main">
<section class="section">
  <div class="container article-layout">
    <div class="prose">
      <h2>Votre spécialiste porte blindée à {E(z["name"])}</h2>
      <p>{PARIS_TXT if is_paris else HDS_TXT}</p>
      {local}
      <p>Avec environ {pop} habitants, {E(z["name"])} fait partie de notre zone d'intervention régulière : la visite technique et le devis sont gratuits, et la pose d'une porte blindée se fait en une journée.</p>
      <h2>Nos prestations à {E(z["name"])}</h2>
      <ul>
        <li><strong><a href="/portes-blindees.html">Remplacement de porte blindée</a></strong> : bloc-porte certifié A2P BP1, BP2 ou BP3, sur mesure.</li>
        <li><strong>Blindage de porte existante</strong> : tôle d'acier, cornières anti-pince et serrure multipoints.</li>
        <li><strong><a href="/serrures.html">Installation et changement de serrure</a></strong> : serrures multipoints A2P, cylindres haute sécurité.</li>
        <li><strong>Mise en sécurité après effraction</strong> et devis pour votre assurance.</li>
      </ul>
      <h2>Combien coûte une porte blindée à {E(z["name"])} ?</h2>
      <p>Les prix sont les mêmes sur toute notre zone : comptez en moyenne de 3 000 à 5 000 € posé pour un bloc-porte A2P BP1, et de 1 300 à 2 800 € pour le blindage d'une porte existante. Pour une estimation adaptée à votre logement, utilisez notre <a href="/simulateur.html">simulateur de prix</a> ou consultez notre <a href="/guides/prix-porte-blindee.html">guide des prix</a>.</p>
      <h2>Les marques que nous posons</h2>
      <p>Fichet, Picard Serrures, Bricard, Héraclès, Tordjman Métal, Zilten, Dierre, Gardesa pour les portes ; Mul-T-Lock, Vachette, Abus, Thirard et bien d'autres pour les serrures. <a href="/marques/">Voir toutes les marques</a>.</p>
    </div>
    <div class="article-aside">{aside_card(f"Un projet à {E(z['name'])} ?")}</div>
  </div>
</section>
<section class="section section-sand">
  <div class="container">
    <div class="head"><div><span class="kicker">Les plus demandées</span><h2>Portes blindées certifiées.</h2></div><p>Une sélection de blocs-portes A2P adaptés aux appartements et maisons.</p></div>
    <div class="products cols-3">{"".join(product_card(p) for p in feats)}</div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="head"><div><span class="kicker">À proximité</span><h2>Nous intervenons aussi à…</h2></div><p></p></div>
    <div class="zone-list">{"".join(zone_link(o) for o in near)}</div>
  </div>
</section>
''' + cta_block() + "</main>\n" + footer()
    write(f"zones/{z['slug']}.html", html_, "0.6")

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
