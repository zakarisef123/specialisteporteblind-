/* ==========================================================
   Spécialiste Porte Blindée — scripts
   Données produits : assets/js/data.js (généré par _src/build.py)
   ========================================================== */
(function () {
  "use strict";
  var DATA = window.SITE_DATA || { doors: [], locks: [], logos: {} };
  var dl = window.dataLayer = window.dataLayer || [];
  function track(event, extra) {
    var o = { event: event };
    for (var k in extra || {}) o[k] = extra[k];
    dl.push(o);
  }

  /* ---------- Suivi des clics (appel, WhatsApp) ---------- */
  document.addEventListener("click", function (e) {
    var a = e.target.closest && e.target.closest("[data-track]");
    if (a) track(a.getAttribute("data-track"), { page: location.pathname });
  });

  /* ---------- Menu mobile ---------- */
  var toggle = document.querySelector(".menu-toggle");
  var nav = document.getElementById("nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    nav.addEventListener("click", function (e) {
      if (e.target.tagName === "A") { nav.classList.remove("open"); toggle.setAttribute("aria-expanded", "false"); }
    });
  }

  /* ---------- En-tête au scroll ---------- */
  var headerEl = document.querySelector(".header");
  if (headerEl) {
    var onScroll = function () { headerEl.classList.toggle("scrolled", window.scrollY > 8); };
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
  }

  /* ---------- Onglets de filtrage (marques, galerie) ---------- */
  function tabFilter(btnAttr, containerId, itemSel, itemAttr) {
    var box = document.getElementById(containerId);
    if (!box) return;
    var tabs = document.querySelectorAll("[" + btnAttr + "]");
    tabs.forEach(function (tab) {
      tab.addEventListener("click", function () {
        var f = tab.getAttribute(btnAttr);
        tabs.forEach(function (t) { t.setAttribute("aria-selected", t === tab ? "true" : "false"); });
        box.querySelectorAll(itemSel).forEach(function (el) {
          el.hidden = f !== "all" && (" " + el.getAttribute(itemAttr) + " ").indexOf(" " + f + " ") === -1;
        });
      });
    });
  }
  tabFilter("data-filter", "brand-wall", "[data-cats]", "data-cats");
  tabFilter("data-gal", "gallery", "figure", "data-cat");

  /* ---------- Année ---------- */
  document.querySelectorAll("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });

  /* ---------- Apparition au scroll ---------- */
  var reveals = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) { entry.target.classList.add("visible"); io.unobserve(entry.target); }
      });
    }, { threshold: 0.08 });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add("visible"); });
  }

  /* ---------- Formulaire de devis ---------- */
  var form = document.getElementById("devis-form");
  if (form) {
    var params = new URLSearchParams(window.location.search);
    var produit = params.get("produit");
    var message = form.querySelector("#message");
    if (produit && message && !message.value) message.value = "Je souhaite un devis pour : " + produit + "\n";
    var prestation = params.get("prestation");
    if (prestation) {
      var radio = form.querySelector('input[name="prestation"][value="' + prestation + '"]');
      if (radio) radio.checked = true;
    }
    var tel = form.querySelector("#telephone");
    form.addEventListener("submit", function (e) {
      if (tel) {
        var digits = tel.value.replace(/\D/g, "");
        if (digits.length < 10) {
          e.preventDefault();
          tel.setCustomValidity("Merci d'indiquer un numéro de téléphone valide (10 chiffres).");
          tel.reportValidity();
          return;
        }
        tel.setCustomValidity("");
      }
      track("envoi_formulaire", { prestation: (form.querySelector('input[name="prestation"]:checked') || {}).value });
    });
    if (tel) tel.addEventListener("input", function () { tel.setCustomValidity(""); });
  }

  /* ======================================================
     Visuels SVG des produits
     ====================================================== */
  function doorSVG(o) {
    var c = o.color || "#2a3f6b";
    var dark = o.dark || "#16233f";
    var style = o.style || "classic";
    var panels = "";
    if (style === "classic") {
      panels =
        '<rect x="30" y="30" width="60" height="70" rx="3" fill="none" stroke="' + dark + '" stroke-width="3"/>' +
        '<rect x="30" y="118" width="60" height="92" rx="3" fill="none" stroke="' + dark + '" stroke-width="3"/>';
    } else if (style === "modern") {
      panels =
        '<rect x="56" y="24" width="6" height="194" rx="3" fill="' + dark + '" opacity=".55"/>' +
        '<rect x="24" y="24" width="72" height="194" rx="2" fill="none" stroke="' + dark + '" stroke-opacity=".3" stroke-width="1.5"/>';
    } else if (style === "lines") {
      for (var i = 0; i < 9; i++) {
        panels += '<rect x="26" y="' + (34 + i * 21) + '" width="68" height="4" rx="2" fill="' + dark + '" opacity=".45"/>';
      }
    } else if (style === "moulure") {
      panels =
        '<rect x="28" y="28" width="64" height="186" rx="4" fill="none" stroke="' + dark + '" stroke-width="3"/>' +
        '<rect x="38" y="40" width="44" height="60" rx="22" fill="none" stroke="' + dark + '" stroke-width="2.5"/>' +
        '<rect x="38" y="118" width="44" height="84" rx="3" fill="none" stroke="' + dark + '" stroke-width="2.5"/>';
    } else if (style === "glass") {
      panels =
        '<rect x="36" y="32" width="48" height="96" rx="3" fill="#a9c3dc" stroke="' + dark + '" stroke-width="3"/>' +
        '<path d="M36 32h48v96z" fill="#fff" opacity=".25"/>' +
        '<rect x="30" y="146" width="60" height="64" rx="3" fill="none" stroke="' + dark + '" stroke-width="3"/>';
    } else if (style === "plate") {
      panels =
        '<rect x="20" y="20" width="80" height="202" rx="2" fill="url(#steel)"/>' +
        '<g fill="' + dark + '" opacity=".5">' +
        '<circle cx="28" cy="28" r="2.5"/><circle cx="92" cy="28" r="2.5"/><circle cx="28" cy="214" r="2.5"/><circle cx="92" cy="214" r="2.5"/>' +
        '<circle cx="28" cy="121" r="2.5"/><circle cx="92" cy="121" r="2.5"/></g>';
    }
    var hinge = '<rect x="13" y="50" width="5" height="18" rx="2" fill="#8d96a6"/><rect x="13" y="175" width="5" height="18" rx="2" fill="#8d96a6"/>';
    var handle =
      '<rect x="94" y="112" width="8" height="34" rx="4" fill="#aab1b7"/>' +
      '<rect x="80" y="124" width="22" height="6" rx="3" fill="#c8cdd1"/>' +
      '<circle cx="98" cy="156" r="5" fill="#aab1b7"/><rect x="97" y="153" width="2" height="6" fill="#3a3f44"/>';
    return '' +
      '<svg viewBox="0 0 120 250" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">' +
      '<defs><linearGradient id="steel" x1="0" x2="1"><stop offset="0" stop-color="#c3cad5"/><stop offset=".5" stop-color="#e6eaf0"/><stop offset="1" stop-color="#aeb7c4"/></linearGradient>' +
      '<linearGradient id="shade' + o.id + '" x1="0" x2="1"><stop offset="0" stop-color="#fff" stop-opacity=".12"/><stop offset="1" stop-color="#000" stop-opacity=".18"/></linearGradient></defs>' +
      '<rect x="4" y="4" width="112" height="242" rx="4" fill="#3b4352"/>' +
      '<rect x="12" y="12" width="96" height="234" rx="2" fill="' + c + '"/>' +
      panels +
      '<rect x="12" y="12" width="96" height="234" rx="2" fill="url(#shade' + o.id + ')"/>' +
      hinge + handle +
      '</svg>';
  }

  function lockSVG(o) {
    var t = o.kind;
    if (t === "cylindre") {
      return '<svg viewBox="0 0 160 120" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">' +
        '<defs><linearGradient id="brass' + o.id + '" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="' + (o.color || "#e2c77a") + '"/><stop offset="1" stop-color="' + (o.dark || "#a8842f") + '"/></linearGradient></defs>' +
        '<rect x="16" y="40" width="128" height="40" rx="20" fill="url(#brass' + o.id + ')"/>' +
        '<rect x="70" y="72" width="20" height="30" rx="4" fill="url(#brass' + o.id + ')"/>' +
        '<circle cx="36" cy="60" r="14" fill="#fff" opacity=".35"/><circle cx="36" cy="60" r="10" fill="none" stroke="#3a3f44" stroke-width="2"/>' +
        '<rect x="33" y="52" width="6" height="16" rx="2" fill="#3a3f44"/>' +
        '<circle cx="124" cy="60" r="10" fill="none" stroke="#3a3f44" stroke-width="2"/>' +
        '<rect x="66" y="40" width="28" height="40" fill="#000" opacity=".08"/>' +
        '<path d="M100 18h40a6 6 0 0 1 6 6v6h-52v-6a6 6 0 0 1 6-6z" fill="#1a2b4f"/>' +
        '<text x="120" y="28" font-size="9" font-weight="800" fill="#c8cdd1" text-anchor="middle" font-family="Arial">A2P</text>' +
        '</svg>';
    }
    if (t === "connectee") {
      return '<svg viewBox="0 0 160 120" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">' +
        '<rect x="44" y="10" width="72" height="100" rx="14" fill="#1a2b4f"/>' +
        '<rect x="54" y="22" width="52" height="40" rx="6" fill="#0b1426"/>' +
        '<g fill="#c8cdd1"><circle cx="66" cy="76" r="4"/><circle cx="80" cy="76" r="4"/><circle cx="94" cy="76" r="4"/><circle cx="66" cy="90" r="4"/><circle cx="80" cy="90" r="4"/><circle cx="94" cy="90" r="4"/></g>' +
        '<path d="M70 42a14 14 0 0 1 20 0M74 47a8 8 0 0 1 12 0" stroke="#3ddc84" stroke-width="3" fill="none" stroke-linecap="round"/>' +
        '<circle cx="80" cy="52" r="2.5" fill="#3ddc84"/>' +
        '</svg>';
    }
    if (t === "verrou") {
      return '<svg viewBox="0 0 160 120" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">' +
        '<rect x="30" y="34" width="70" height="52" rx="6" fill="' + (o.color || "#8d96a6") + '"/>' +
        '<rect x="100" y="50" width="34" height="20" rx="3" fill="#c3cad5"/>' +
        '<circle cx="54" cy="60" r="12" fill="#aab1b7"/><rect x="52" y="52" width="4" height="16" rx="1" fill="#3a3f44"/>' +
        '<rect x="30" y="34" width="70" height="10" rx="5" fill="#fff" opacity=".2"/>' +
        '</svg>';
    }
    // multipoints (applique ou encastrée)
    var bolts = "";
    var n = o.points || 3;
    var ys = n >= 5 ? [14, 36, 60, 84, 106] : [18, 60, 102];
    ys.forEach(function (y) { bolts += '<rect x="96" y="' + (y - 4) + '" width="26" height="8" rx="3" fill="#c3cad5" stroke="#5b6678" stroke-width="1"/>'; });
    return '<svg viewBox="0 0 160 120" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">' +
      '<rect x="74" y="6" width="22" height="108" rx="3" fill="#8d96a6"/>' +
      bolts +
      '<rect x="30" y="34" width="58" height="56" rx="6" fill="' + (o.color || "#1a2b4f") + '"/>' +
      '<rect x="30" y="34" width="58" height="10" rx="5" fill="#fff" opacity=".12"/>' +
      '<circle cx="50" cy="70" r="10" fill="#aab1b7"/><rect x="48" y="63" width="4" height="14" rx="1" fill="#3a3f44"/>' +
      '<text x="68" y="56" font-size="10" font-weight="800" fill="#c8cdd1" text-anchor="middle" font-family="Arial">' + n + 'pts</text>' +
      '</svg>';
  }

  var BY_ID = {};
  DATA.doors.forEach(function (p) { p.isDoor = true; BY_ID[p.id] = p; });
  DATA.locks.forEach(function (p) { BY_ID[p.id] = p; });
  function visual(p) { return p.isDoor ? doorSVG(p) : lockSVG(p); }

  // Visuels insérés dans les pages générées : <span data-visual="d3">
  document.querySelectorAll("[data-visual]").forEach(function (el) {
    var p = BY_ID[el.getAttribute("data-visual")];
    if (p) el.outerHTML = visual(p);
  });

  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
  function brandLogo(name) {
    var slug = DATA.logos[name];
    return slug ? '<span class="brand-logo"><img src="/assets/img/marques/' + slug + '.webp" alt="' + esc(name) + '" loading="lazy"></span>' : "";
  }
  function card(p) {
    var url = "/produits/" + p.slug + ".html";
    return '<article class="product">' +
      '<a class="product-visual" href="' + url + '" aria-label="' + esc(p.name) + '">' + brandLogo(p.brand) + (p.badge ? '<span class="cert-tag">' + p.badge + '</span>' : "") + visual(p) + '</a>' +
      '<div class="product-body">' +
      '<div class="product-brand">' + esc(p.brand) + '</div>' +
      '<h3><a href="' + url + '">' + esc(p.name) + '</a></h3>' +
      '<p>' + esc(p.desc) + '</p>' +
      '<div class="specs">' + p.specs.map(function (s) { return '<span>' + s + '</span>'; }).join("") + '</div>' +
      '<div class="product-foot"><div class="price">' + (p.price ? 'Budget indicatif posé<strong>' + p.price + '</strong>' : 'Prix posé<strong>Sur devis</strong>') + '</div>' +
      '<a class="btn btn-ink btn-sm" href="' + url + '">Voir</a></div>' +
      '</div></article>';
  }

  /* ======================================================
     Catalogue (filtrage + recherche)
     ====================================================== */
  function initCatalog(cfg) {
    var root = document.getElementById(cfg.rootId);
    if (!root) return;
    var grid = root.querySelector(".products");
    var countEl = root.querySelector(".count");
    var search = root.querySelector('input[type="search"]');
    var filtersEl = root.querySelector(".filters");
    var resetBtn = root.querySelector("[data-reset]");
    var filtersToggle = root.querySelector(".filters-toggle");
    var brandSelect = root.querySelector('select[name="brand"]');

    if (brandSelect) {
      var brands = cfg.data.map(function (p) { return p.brand; })
        .filter(function (b, i, a) { return a.indexOf(b) === i; })
        .sort(function (a, b) { return a.localeCompare(b, "fr"); });
      brands.forEach(function (b) {
        var opt = document.createElement("option");
        opt.value = b; opt.textContent = b;
        brandSelect.appendChild(opt);
      });
      var preBrand = new URLSearchParams(window.location.search).get("marque");
      if (preBrand && brands.indexOf(preBrand) !== -1) brandSelect.value = preBrand;
    }
    function checked(name) {
      return Array.prototype.map.call(root.querySelectorAll('input[name="' + name + '"]:checked'), function (i) { return i.value; });
    }
    function render() {
      var q = (search && search.value || "").trim().toLowerCase();
      var brand = brandSelect ? brandSelect.value : "";
      var active = {};
      cfg.filters.forEach(function (f) { active[f] = checked(f); });
      var list = cfg.data.filter(function (p) {
        if (brand && p.brand !== brand) return false;
        for (var i = 0; i < cfg.filters.length; i++) {
          var f = cfg.filters[i];
          if (active[f].length) {
            var vals = Array.isArray(p[f]) ? p[f] : [p[f]];
            if (!vals.some(function (x) { return active[f].indexOf(x) !== -1; })) return false;
          }
        }
        if (q) {
          var hay = (p.brand + " " + p.name + " " + p.desc + " " + p.specs.join(" ")).toLowerCase();
          if (hay.indexOf(q) === -1) return false;
        }
        return true;
      });
      countEl.textContent = list.length + (list.length > 1 ? " modèles" : " modèle");
      grid.innerHTML = list.length ? list.map(card).join("") :
        '<div class="empty"><strong>Aucun modèle ne correspond à ces critères.</strong><br>Appelez-nous : nous travaillons avec toutes les marques du marché français, même celles non listées ici.</div>';
    }
    root.addEventListener("change", render);
    if (search) search.addEventListener("input", render);
    if (resetBtn) resetBtn.addEventListener("click", function () {
      root.querySelectorAll(".filters input[type=checkbox]").forEach(function (i) { i.checked = false; });
      if (brandSelect) brandSelect.value = "";
      if (search) search.value = "";
      render();
    });
    if (filtersToggle) filtersToggle.addEventListener("click", function () {
      var open = filtersEl.classList.toggle("open");
      filtersToggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    render();
  }
  initCatalog({ rootId: "catalogue-portes", data: DATA.doors, filters: ["cert", "usage", "type"] });
  initCatalog({ rootId: "catalogue-serrures", data: DATA.locks, filters: ["kind", "cert", "pose"] });

  /* ======================================================
     Simulateur de prix (fourchettes moyennes TTC posé)
     ====================================================== */
  var sim = document.getElementById("simulateur");
  if (sim) {
    var BASE = {
      porte: { none: [1800, 3000], BP1: [3000, 5000], BP2: [4500, 7000], BP3: [7000, 10000] },
      blindage: [1300, 2800],
      serrure: { A2P1: [400, 800], A2P2: [600, 1000], A2P3: [800, 1400] },
      cylindre: [150, 450]
    };
    var OPTS = { finition: [300, 900], dimensions: [400, 900], isolation: [300, 700], connectee: [250, 500] };
    var LABELS = { porte: "Bloc-porte blindé", blindage: "Blindage de porte existante", serrure: "Serrure multipoints", cylindre: "Cylindre haute sécurité" };
    var INCL = {
      porte: ["Visite technique et prise de mesures", "Fabrication sur mesure", "Dépose et évacuation de l'ancienne porte", "Pose, réglages et certificat"],
      blindage: ["Diagnostic de la porte", "Tôle acier et cornières anti-pince", "Serrure multipoints", "Pose et réglages"],
      serrure: ["Fourniture de la serrure", "Pose et réglages", "Clés et carte de propriété"],
      cylindre: ["Fourniture du cylindre", "Pose immédiate", "Clés et carte de propriété"]
    };
    var fmt = function (n) { return n.toLocaleString("fr-FR") + " €"; };
    var val = function (n) { var el = sim.querySelector('input[name="' + n + '"]:checked'); return el ? el.value : null; };
    var tracked = false;
    var update = function () {
      var projet = val("projet");
      // afficher / masquer les étapes et les renuméroter
      var n = 0;
      sim.querySelectorAll(".sim-step").forEach(function (fs) {
        var f = fs.getAttribute("data-for");
        var show = !f || (" " + f + " ").indexOf(" " + projet + " ") !== -1;
        fs.hidden = !show;
        if (show) fs.querySelector(".step-n").textContent = ++n;
      });
      var r;
      if (projet === "porte") r = BASE.porte[val("niveau")].slice();
      else if (projet === "serrure") r = BASE.serrure[val("serrure")].slice();
      else r = BASE[projet].slice();
      var label = LABELS[projet] + (projet === "porte" && val("niveau") !== "none" ? " A2P " + val("niveau") : "");
      if (projet === "porte" || projet === "blindage") {
        sim.querySelectorAll('input[name="options"]:checked').forEach(function (o) {
          r[0] += OPTS[o.value][0]; r[1] += OPTS[o.value][1];
        });
        if (projet === "porte" && val("logement") === "maison" && !sim.querySelector('input[value="isolation"]:checked')) {
          r[0] += 200; r[1] += 400;
        }
      }
      document.getElementById("sim-min").textContent = fmt(r[0]);
      document.getElementById("sim-max").textContent = fmt(r[1]);
      document.getElementById("sim-label").textContent = label + " · fourniture et pose, TTC";
      document.getElementById("sim-incl").innerHTML = INCL[projet].map(function (t) { return "<li>" + t + "</li>"; }).join("");
      var prest = projet === "porte" ? "remplacement" : projet === "blindage" ? "blindage" : "serrure";
      var msg = label + " (" + val("logement") + ") – estimation simulateur : " + fmt(r[0]) + " à " + fmt(r[1]);
      document.getElementById("sim-cta").href = "/?produit=" + encodeURIComponent(msg) + "&prestation=" + prest + "#devis";
      if (tracked) track("simulateur_resultat", { projet: projet, min: r[0], max: r[1] });
      tracked = true;
    };
    sim.addEventListener("change", update);
    update();
  }

  /* ======================================================
     Comparateur avant / après
     ====================================================== */
  var ba = document.getElementById("ba");
  if (ba) {
    var range = ba.querySelector("input[type=range]");
    var setBA = function () { ba.style.setProperty("--pos", range.value + "%"); };
    range.addEventListener("input", setBA);
    setBA();
  }
})();
