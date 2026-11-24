#!/usr/bin/env python3
"""Générateur du site Spécialiste Porte Blindée.

Usage :  python3 _src/build.py
Régénère toutes les pages HTML, assets/js/data.js, sitemap.xml et robots.txt
à partir des fichiers de _src/ (config.py, brands.py, guides.py, zones.json,
products.json, pages/*.py).
"""
import json, math, pathlib, re, sys, unicodedata, datetime, html as _html

SRC = pathlib.Path(__file__).resolve().parent
ROOT = SRC.parent
sys.path.insert(0, str(SRC))

from config import *            # noqa: F401,F403
from icons import I, ic         # noqa: F401
from brands import BRANDS as BRAND_DATA
from guides import GUIDES

E = _html.escape
TODAY = datetime.date.today().isoformat()
ADDRESS = f"{STREET}, {POSTCODE} {CITY}"
SITEMAP = []

def slugify(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")

# ---------------------------------------------------------------- données
PRODUCTS = json.loads((SRC / "products.json").read_text(encoding="utf-8"))
ZONES = json.loads((SRC / "zones.json").read_text(encoding="utf-8"))

BRAND_BY_NAME = {b[1]: b for b in BRAND_DATA}
BRAND_SLUG = {b[1]: b[0] for b in BRAND_DATA}
# Liste (logo, nom, catégories) des marques ayant un logo — utilisée par les modèles
BRANDS = [(b[2], b[1], b[3]) for b in BRAND_DATA if b[2]]

for kind, items in (("porte", PRODUCTS["doors"]), ("serrure", PRODUCTS["locks"])):
    for i, p in enumerate(items):
        p["id"] = ("d" if kind == "porte" else "l") + str(i)
        p["kind_label"] = kind
        base = slugify(p["name"] + ("" if p["brand"] == "Toutes marques" else " " + p["brand"]))
        p["slug"] = base
ALL_PRODUCTS = PRODUCTS["doors"] + PRODUCTS["locks"]
seen = {}
for p in ALL_PRODUCTS:
    if p["slug"] in seen:
        seen[p["slug"]] += 1
        p["slug"] += "-" + str(seen[p["slug"]])
    else:
        seen[p["slug"]] = 1

CERT_TEXT = {
    "BP1": "certifié A2P BP1 : 5 minutes de résistance à l'effraction en laboratoire",
    "BP2": "certifié A2P BP2 : 10 minutes de résistance à l'effraction en laboratoire",
    "BP3": "certifié A2P BP3 : 15 minutes de résistance, le plus haut niveau A2P",
    "RC3": "classé selon la norme européenne EN 1627 (classe 3)",
    "RC4": "classé selon la norme européenne EN 1627 (classe 4)",
    "A2P1": "niveau A2P★ (5 minutes de résistance), selon les versions",
    "A2P2": "niveau A2P★★ (10 minutes de résistance), selon les versions",
    "A2P3": "niveau A2P★★★ (15 minutes de résistance), selon les versions",
}

# ---------------------------------------------------------------- briques HTML
def logo_img(slug, name, lazy=True, cls=""):
    c = f' class="{cls}"' if cls else ""
    return f'<img{c} src="/assets/img/marques/{slug}.webp" alt="{E(name)}"{" loading=\"lazy\"" if lazy else ""} decoding="async">'

LOGO = '''<svg class="logo-mark" viewBox="0 0 40 40" aria-hidden="true">
  <rect width="40" height="40" fill="#141516"/>
  <rect x="13" y="8" width="14" height="24" fill="none" stroke="#fff" stroke-width="1.6"/>
  <line x1="13" y1="20" x2="27" y2="20" stroke="#b9bfc4" stroke-width="1.6"/>
  <rect x="23" y="18" width="2" height="4" fill="#b9bfc4"/>
</svg>'''

def logo_block():
    return f'''<a class="logo" href="/" aria-label="{NAME} – accueil">
        {LOGO}
        <span class="logo-text"><strong>Porte Blindée</strong><span>Spécialiste</span></span>
      </a>'''

def gtm_head():
    if not GTM_ID:
        return ""
    return f"""  <script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);}})(window,document,'script','dataLayer','{GTM_ID}');</script>\n"""

def gtm_body():
    if not GTM_ID:
        return ""
    return f'<noscript><iframe src="https://www.googletagmanager.com/ns.html?id={GTM_ID}" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>\n'

def head(title, desc, canonical, extra="", image="serrure-multipoints-porte-blindee"):
    path = "/" + canonical.lstrip("/")
    return f'''<!doctype html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{E(title)}</title>
  <meta name="description" content="{E(desc)}">
  <link rel="canonical" href="{DOMAIN}{path}">
  <meta property="og:type" content="website">
  <meta property="og:locale" content="fr_FR">
  <meta property="og:site_name" content="{E(NAME)}">
  <meta property="og:title" content="{E(title)}">
  <meta property="og:description" content="{E(desc)}">
  <meta property="og:url" content="{DOMAIN}{path}">
  <meta property="og:image" content="{DOMAIN}/assets/img/photos/{image}.webp">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="theme-color" content="#141516">
  <link rel="icon" href="/assets/img/favicon.svg" type="image/svg+xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;700;800&family=Public+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/assets/css/style.css">
{gtm_head()}{extra}</head>
<body>
{gtm_body()}<a class="skip-link" href="#main">Aller au contenu</a>
'''

def header(active):
    def a(href, label, key):
        cur = ' aria-current="page"' if key == active else ''
        return f'<a href="{href}"{cur}>{label}</a>'
    return f'''<div class="utility">
  <div class="container">
    <ul>
      <li>Devis gratuit · Pose en une journée · Matériel certifié A2P</li>
      <li class="hide-sm">{I["pin"]} <a href="/zones/">{ZONE}</a></li>
      <li class="hide-sm">{I["clock"]} {HOURS}</li>
    </ul>
    <ul>
      <li>{I["mail"]} <a href="mailto:{EMAIL}">{EMAIL}</a></li>
    </ul>
  </div>
</div>
<header class="header">
  <div class="container">
    {logo_block()}
    <nav class="nav" id="nav" aria-label="Navigation principale">
      {a("/portes-blindees.html", "Portes blindées", "portes")}
      {a("/serrures.html", "Serrures", "serrures")}
      {a("/marques/", "Marques", "marques")}
      {a("/simulateur.html", "Prix", "prix")}
      {a("/realisations.html", "Réalisations", "realisations")}
      {a("/guides/", "Guides", "guides")}
    </nav>
    <div class="header-cta">
      <a class="phone-pill" href="tel:{PHONE_TEL}" data-track="clic_appel" aria-label="Appeler le {PHONE}"><span class="ring">{I["phone"]}</span><span><small>Devis gratuit</small><strong>{PHONE}</strong></span></a>
      <a class="btn btn-red btn-sm" href="/#devis">Demander un devis</a>
      <button class="menu-toggle" type="button" aria-controls="nav" aria-expanded="false" aria-label="Ouvrir le menu">{I["menu"]}</button>
    </div>
  </div>
</header>
'''

def cta_block(title="Porte fracturée, serrure bloquée ?", text="Un technicien vous rappelle rapidement pour sécuriser votre logement."):
    wa = f'<a class="btn btn-ghost" href="https://wa.me/{WHATSAPP}" target="_blank" rel="noopener" data-track="clic_whatsapp">{I["whatsapp"]} WhatsApp</a>' if WHATSAPP else f'<a class="btn btn-ghost" href="/#devis">Devis en ligne</a>'
    return f'''<section class="section cta-wrap">
  <div class="container">
    <div class="cta reveal">
      <div>
        <h2>{title}</h2>
        <p>{text}</p>
      </div>
      <div class="btns">
        <a class="btn btn-white" href="tel:{PHONE_TEL}" data-track="clic_appel">{I["phone"]} {PHONE}</a>
        {wa}
      </div>
    </div>
  </div>
</section>
'''

def footer():
    logos = "".join(f'<a href="/marques/{BRAND_SLUG[n]}.html" title="{E(n)}">{logo_img(s, n)}</a>' for s, n, c in BRANDS)
    zones = "".join(f'<li><a href="/zones/{z["slug"]}.html">Porte blindée {E(z["name"])}</a></li>' for z in ZONES[:6])
    guides = "".join(f'<li><a href="/guides/{g[0]}.html">{E(g[1].split(":")[0].split("?")[0].strip())}</a></li>' for g in GUIDES[:4])
    wa = ""
    _unused = f'<a class="wa-float" href="https://wa.me/{WHATSAPP}" target="_blank" rel="noopener" data-track="clic_whatsapp" aria-label="Nous écrire sur WhatsApp">{I["whatsapp"]}<span>Envoyez une photo de votre porte</span></a>' if WHATSAPP else ""
    return f'''<footer class="footer">
  <div class="container">
    <div class="footer-top">
      <div>
        {logo_block()}
        <p>Installateur indépendant spécialisé dans le remplacement de portes blindées, le blindage de portes existantes et l'installation de serrures haute sécurité certifiées A2P.</p>
        <p><a class="arrow-link light" href="/a-propos.html">Qui sommes-nous {I["arrow"]}</a></p>
      </div>
      <div>
        <h4>Prestations</h4>
        <ul>
          <li><a href="/portes-blindees.html">Remplacement de porte blindée</a></li>
          <li><a href="/?prestation=blindage#devis">Blindage de porte existante</a></li>
          <li><a href="/serrures.html">Changement de serrure</a></li>
          <li><a href="/simulateur.html">Simulateur de prix</a></li>
          <li><a href="/realisations.html">Nos réalisations</a></li>
        </ul>
      </div>
      <div>
        <h4>Guides</h4>
        <ul>{guides}<li><a href="/guides/">Tous les guides</a></li></ul>
      </div>
      <div>
        <h4>Contact</h4>
        <ul class="contact">
          <li>{I["phone"]} <a href="tel:{PHONE_TEL}" data-track="clic_appel">{PHONE}</a></li>
          <li>{I["mail"]} <a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li>{I["pin"]} <span>{ADDRESS}</span></li>
          <li>{I["clock"]} <span>{HOURS}</span></li>
        </ul>
      </div>
    </div>
    <div class="footer-zones"><h4>Zones d'intervention</h4><ul>{zones}<li><a href="/zones/">Toutes les villes ({len(ZONES)})</a></li></ul></div>
    <div class="footer-logos"><small>Marques installées</small>{logos}</div>
    <div class="footer-bottom">
      <span>© <span data-year>2026</span> {NAME}. Installateur indépendant — les marques et logos cités appartiennent à leurs propriétaires respectifs.</span>
      <ul>
        <li><a href="/mentions-legales.html">Mentions légales</a></li>
        <li><a href="/mentions-legales.html#confidentialite">Confidentialité</a></li>
        <li><a href="/plan-du-site.html">Plan du site</a></li>
      </ul>
    </div>
  </div>
</footer>
{wa}
<nav class="mobile-bar" aria-label="Contact rapide">
  <a class="call" href="tel:{PHONE_TEL}" data-track="clic_appel">{I["phone"]} Appeler</a>
  <a class="quote-btn" href="/#devis">{I["file"]} Devis gratuit</a>
</nav>
<script src="/assets/js/data.js" defer></script>
<script src="/assets/js/main.js" defer></script>
</body>
</html>
'''

def crumbs_ld(items):
    return '<script type="application/ld+json">' + json.dumps({
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": DOMAIN + u}
                            for i, (n, u) in enumerate(items)]}, ensure_ascii=False) + '</script>\n'

def page_hero(crumb, h1, lead, photo, logos=None, trail=None):
    lg = ""
    if logos:
        lg = '<div class="hero-logos">' + "".join(f'<span>{logo_img(s, n, lazy=False)}</span>' for s, n, c in BRANDS if s in logos) + '</div>'
    t = "".join(f'<a href="{u}">{E(n)}</a><span>/</span>' for n, u in (trail or []))
    return f'''<section class="page-hero">
  <img class="bg" src="/assets/img/photos/{photo}.webp" alt="" aria-hidden="true">
  <div class="container">
    <nav class="crumbs" aria-label="Fil d'Ariane"><a href="/">Accueil</a><span>/</span>{t}<span>{crumb}</span></nav>
    <h1>{h1}</h1>
    <p>{lead}</p>
    {lg}
  </div>
</section>
'''

def product_card(p):
    brand = BRAND_BY_NAME.get(p["brand"])
    lg = f'<span class="brand-logo">{logo_img(brand[2], p["brand"])}</span>' if brand and brand[2] else ""
    badge = f'<span class="cert-tag">{p["badge"]}</span>' if p.get("badge") else ""
    price = f'Budget indicatif posé<strong>{p["price"]}</strong>' if p.get("price") else 'Prix posé<strong>Sur devis</strong>'
    return f'''<article class="product">
  <a class="product-visual" href="/produits/{p["slug"]}.html" aria-label="{E(p["name"])}">{lg}{badge}<span data-visual="{p["id"]}"></span></a>
  <div class="product-body">
    <div class="product-brand">{E(p["brand"])}</div>
    <h3><a href="/produits/{p["slug"]}.html">{E(p["name"])}</a></h3>
    <p>{E(p["desc"])}</p>
    <div class="specs">{"".join(f"<span>{s}</span>" for s in p["specs"])}</div>
    <div class="product-foot"><div class="price">{price}</div><a class="btn btn-ink btn-sm" href="/produits/{p["slug"]}.html">Voir</a></div>
  </div>
</article>'''

def write(rel, content, priority="0.6", index=True):
    content = re.sub(r"\.(\s*</h[12]>)", r"\1", content)
    out = ROOT / rel
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(content, encoding="utf-8")
    if index:
        url = "/" + rel
        if url.endswith("index.html"):
            url = url[:-len("index.html")]
        SITEMAP.append((url, priority))

def dist(a, b):
    return math.hypot(a["lat"] - b["lat"], (a["lng"] - b["lng"]) * math.cos(math.radians(a["lat"])))

# ---------------------------------------------------------------- pages
exec((SRC / "generators.py").read_text(encoding="utf-8"), globals())
ctx = dict(globals())

# Modèles de pages classiques (_src/pages/*.py)
for tpl in sorted((SRC / "pages").glob("*.py")):
    ns = dict(ctx)
    ns.update({k: v for k, v in globals().items() if k not in ns})
    exec(tpl.read_text(encoding="utf-8"), ns)
    write(ns["FILENAME"], ns["HTML"], ns.get("PRIORITY", "0.8"), ns.get("INDEX", True))

# ---------------------------------------------------------------- data.js
data = {
    "doors": PRODUCTS["doors"], "locks": PRODUCTS["locks"],
    "logos": {b[1]: b[2] for b in BRAND_DATA if b[2]},
}
(ROOT / "assets/js/data.js").write_text(
    "/* Généré par _src/build.py — ne pas modifier à la main */\nwindow.SITE_DATA = " +
    json.dumps(data, ensure_ascii=False, separators=(",", ":")) + ";\n", encoding="utf-8")

# ---------------------------------------------------------------- sitemap & robots
SITEMAP.sort(key=lambda u: (-float(u[1]), u[0]))
xml = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for url, pr in SITEMAP:
    xml.append(f"  <url><loc>{DOMAIN}{url}</loc><lastmod>{TODAY}</lastmod><priority>{pr}</priority></url>")
xml.append("</urlset>")
(ROOT / "sitemap.xml").write_text("\n".join(xml) + "\n", encoding="utf-8")
(ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nDisallow: /_src/\n\nSitemap: {DOMAIN}/sitemap.xml\n", encoding="utf-8")
print(f"{len(SITEMAP)} pages indexables générées.")
