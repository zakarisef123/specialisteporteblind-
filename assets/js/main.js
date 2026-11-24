/* ==========================================================
   Spécialiste Porte Blindée — scripts
   ========================================================== */
(function () {
  "use strict";

  /* ---------- Menu mobile ---------- */
  var toggle = document.querySelector(".menu-toggle");
  var nav = document.getElementById("nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    nav.addEventListener("click", function (e) {
      if (e.target.tagName === "A") {
        nav.classList.remove("open");
        toggle.setAttribute("aria-expanded", "false");
      }
    });
  }

  /* ---------- Année du footer ---------- */
  document.querySelectorAll("[data-year]").forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });

  /* ---------- Apparition au scroll ---------- */
  var reveals = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("visible");
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12 });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add("visible"); });
  }

  /* ---------- Formulaire de devis ---------- */
  var form = document.getElementById("devis-form");
  if (form) {
    // Pré-remplissage depuis le catalogue : ?produit=...
    var params = new URLSearchParams(window.location.search);
    var produit = params.get("produit");
    var message = form.querySelector("#message");
    if (produit && message && !message.value) {
      message.value = "Je souhaite un devis pour : " + produit + "\n";
    }
    var prestation = params.get("prestation");
    if (prestation) {
      var radio = form.querySelector('input[name="prestation"][value="' + prestation + '"]');
      if (radio) radio.checked = true;
    }

    form.addEventListener("submit", function (e) {
      var phone = form.querySelector("#telephone");
      if (phone) {
        var digits = phone.value.replace(/\D/g, "");
        if (digits.length < 10) {
          e.preventDefault();
          phone.setCustomValidity("Merci d'indiquer un numéro de téléphone valide (10 chiffres).");
          phone.reportValidity();
          return;
        }
        phone.setCustomValidity("");
      }
    });
    var tel = form.querySelector("#telephone");
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
      '<rect x="94" y="112" width="8" height="34" rx="4" fill="#c9a24a"/>' +
      '<rect x="80" y="124" width="22" height="6" rx="3" fill="#d9b867"/>' +
      '<circle cx="98" cy="156" r="5" fill="#c9a24a"/><rect x="97" y="153" width="2" height="6" fill="#5c4614"/>';
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
        '<circle cx="36" cy="60" r="14" fill="#fff" opacity=".35"/><circle cx="36" cy="60" r="10" fill="none" stroke="#5c4614" stroke-width="2"/>' +
        '<rect x="33" y="52" width="6" height="16" rx="2" fill="#5c4614"/>' +
        '<circle cx="124" cy="60" r="10" fill="none" stroke="#5c4614" stroke-width="2"/>' +
        '<rect x="66" y="40" width="28" height="40" fill="#000" opacity=".08"/>' +
        '<path d="M100 18h40a6 6 0 0 1 6 6v6h-52v-6a6 6 0 0 1 6-6z" fill="#1a2b4f"/>' +
        '<text x="120" y="28" font-size="9" font-weight="800" fill="#d9b867" text-anchor="middle" font-family="Arial">A2P</text>' +
        '</svg>';
    }
    if (t === "connectee") {
      return '<svg viewBox="0 0 160 120" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">' +
        '<rect x="44" y="10" width="72" height="100" rx="14" fill="#1a2b4f"/>' +
        '<rect x="54" y="22" width="52" height="40" rx="6" fill="#0b1426"/>' +
        '<g fill="#d9b867"><circle cx="66" cy="76" r="4"/><circle cx="80" cy="76" r="4"/><circle cx="94" cy="76" r="4"/><circle cx="66" cy="90" r="4"/><circle cx="80" cy="90" r="4"/><circle cx="94" cy="90" r="4"/></g>' +
        '<path d="M70 42a14 14 0 0 1 20 0M74 47a8 8 0 0 1 12 0" stroke="#3ddc84" stroke-width="3" fill="none" stroke-linecap="round"/>' +
        '<circle cx="80" cy="52" r="2.5" fill="#3ddc84"/>' +
        '</svg>';
    }
    if (t === "verrou") {
      return '<svg viewBox="0 0 160 120" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">' +
        '<rect x="30" y="34" width="70" height="52" rx="6" fill="' + (o.color || "#8d96a6") + '"/>' +
        '<rect x="100" y="50" width="34" height="20" rx="3" fill="#c3cad5"/>' +
        '<circle cx="54" cy="60" r="12" fill="#c9a24a"/><rect x="52" y="52" width="4" height="16" rx="1" fill="#5c4614"/>' +
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
      '<circle cx="50" cy="70" r="10" fill="#c9a24a"/><rect x="48" y="63" width="4" height="14" rx="1" fill="#5c4614"/>' +
      '<text x="68" y="56" font-size="10" font-weight="800" fill="#d9b867" text-anchor="middle" font-family="Arial">' + n + 'pts</text>' +
      '</svg>';
  }

  /* ======================================================
     Catalogue générique (filtrage + recherche)
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

    // Liste des marques
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
      return Array.prototype.map.call(
        root.querySelectorAll('input[name="' + name + '"]:checked'),
        function (i) { return i.value; }
      );
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
            var v = p[f];
            var vals = Array.isArray(v) ? v : [v];
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
      if (!list.length) {
        grid.innerHTML = '<div class="empty"><strong>Aucun modèle ne correspond à ces critères.</strong><br>Appelez-nous : nous travaillons avec toutes les marques du marché français, même celles non listées ici.</div>';
        return;
      }
      grid.innerHTML = list.map(function (p) {
        var label = p.brand + " – " + p.name;
        return '<article class="product">' +
          '<div class="product-visual">' + (p.badge ? '<span class="cert">' + p.badge + '</span>' : "") + cfg.visual(p) + '</div>' +
          '<div class="product-body">' +
          '<div class="product-brand">' + p.brand + '</div>' +
          '<h3>' + p.name + '</h3>' +
          '<p>' + p.desc + '</p>' +
          '<div class="specs">' + p.specs.map(function (s) { return '<span>' + s + '</span>'; }).join("") + '</div>' +
          '<div class="product-foot"><div class="price">' + (p.price ? 'Budget indicatif posé<strong>' + p.price + '</strong>' : 'Prix posé<strong>Sur devis</strong>') + '</div>' +
          '<a class="btn btn-navy" href="index.html?produit=' + encodeURIComponent(label) + '&prestation=' + cfg.prestation + '#devis">Devis</a></div>' +
          '</div></article>';
      }).join("");
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

  /* ======================================================
     Données : portes blindées
     Les certifications indiquées correspondent aux versions
     proposées ; chaque fabricant décline plusieurs niveaux.
     ====================================================== */
  var DOORS = [
    { brand: "Fichet", name: "Bloc-porte blindé Forstyl – appartement", cert: "BP1", usage: ["appartement"], type: "bloc-porte",
      desc: "Bloc-porte complet (porte + bâti) pour porte palière, avec serrure multipoints haute sécurité et finitions personnalisables.",
      specs: ["A2P BP1", "Serrure A2P★★★", "Isolation phonique"], price: "à partir de 3 500 €", badge: "A2P BP1", color: "#2a3f6b", style: "moulure" },
    { brand: "Fichet", name: "Bloc-porte blindé haute sécurité", cert: "BP3", usage: ["appartement", "maison"], type: "bloc-porte",
      desc: "Le niveau de résistance le plus élevé de la certification A2P, pour les biens exposés ou les exigences d'assurance renforcées.",
      specs: ["A2P BP3", "Serrure A2P★★★", "Pions anti-dégondage"], price: "à partir de 7 000 €", badge: "A2P BP3", color: "#1d2a40", style: "classic" },
    { brand: "Fichet", name: "Blindage de porte existante", cert: "none", usage: ["appartement", "maison"], type: "blindage",
      desc: "Conservez votre porte : nous la renforçons par une tôle d'acier, des cornières anti-pince et une serrure multipoints.",
      specs: ["Tôle acier", "Cornières anti-pince", "Serrure multipoints"], price: "à partir de 1 500 €", color: "#6b4b33", dark: "#3e2a1b", style: "plate" },
    { brand: "Picard Serrures", name: "Bloc-porte blindé palier", cert: "BP1", usage: ["appartement"], type: "bloc-porte",
      desc: "Fabrication française, idéal en remplacement de porte palière d'immeuble. Habillages bois, laqués ou moulurés.",
      specs: ["A2P BP1", "Fabrication française", "Seuil à la suisse"], price: "à partir de 3 200 €", badge: "A2P BP1", color: "#5a3a26", dark: "#38231a", style: "moulure" },
    { brand: "Picard Serrures", name: "Bloc-porte blindé renforcé", cert: "BP2", usage: ["appartement", "maison"], type: "bloc-porte",
      desc: "Résistance accrue à l'effraction, serrure à combinaisons protégées et carte de propriété pour la reproduction des clés.",
      specs: ["A2P BP2", "Carte de propriété", "Acoustique renforcée"], price: "à partir de 4 800 €", badge: "A2P BP2", color: "#2b2f36", dark: "#14171b", style: "classic" },
    { brand: "Bricard", name: "Porte blindée certifiée A2P", cert: "BP1", usage: ["appartement"], type: "bloc-porte",
      desc: "Bloc-porte blindé associé aux serrures et cylindres de la marque, pour une solution homogène et certifiée.",
      specs: ["A2P BP1", "Cylindre haute sécurité", "Paumelles renforcées"], price: "à partir de 3 300 €", badge: "A2P BP1", color: "#33465f", dark: "#1c2738", style: "modern" },
    { brand: "Bricard", name: "Porte blindée haute résistance", cert: "BP2", usage: ["appartement", "maison"], type: "bloc-porte",
      desc: "Pour les logements en rez-de-chaussée ou les biens de valeur : temps de résistance doublé par rapport au niveau BP1.",
      specs: ["A2P BP2", "Multipoints", "Anti-dégondage"], price: "à partir de 5 000 €", badge: "A2P BP2", color: "#4a4f57", dark: "#2a2e33", style: "lines" },
    { brand: "Héraclès", name: "Porte blindée palière", cert: "BP1", usage: ["appartement"], type: "bloc-porte",
      desc: "Porte palière blindée certifiée, large choix de panneaux décoratifs pour s'harmoniser avec les parties communes.",
      specs: ["A2P BP1", "Panneaux décoratifs", "Joint isophonique"], price: "à partir de 3 000 €", badge: "A2P BP1", color: "#7a5132", dark: "#4a3020", style: "classic" },
    { brand: "Héraclès", name: "Porte d'entrée blindée isolante", cert: "BP2", usage: ["maison"], type: "bloc-porte",
      desc: "Porte d'entrée de maison alliant sécurité et performance thermique, résistante aux intempéries.",
      specs: ["A2P BP2", "Isolation thermique", "Usage extérieur"], price: "à partir de 4 900 €", badge: "A2P BP2", color: "#3c4a3e", dark: "#222b23", style: "glass" },
    { brand: "Dierre", name: "Porte blindée design", cert: "RC3", usage: ["appartement", "maison"], type: "bloc-porte",
      desc: "Fabricant italien réputé pour ses portes blindées au design contemporain et leurs nombreuses finitions.",
      specs: ["EN 1627 classe 3", "Design italien", "Finitions sur mesure"], price: "à partir de 3 800 €", badge: "Classe 3", color: "#e9e4dc", dark: "#b7ae9f", style: "modern" },
    { brand: "Gardesa", name: "Porte blindée classe 4", cert: "RC4", usage: ["appartement", "maison"], type: "bloc-porte",
      desc: "Porte blindée italienne haute sécurité, structure acier, compatible serrures mécaniques ou électroniques.",
      specs: ["EN 1627 classe 4", "Serrure électronique possible", "Isolation"], price: "à partir de 5 500 €", badge: "Classe 4", color: "#24272c", dark: "#0f1113", style: "lines" },
    { brand: "Di.Bi.", name: "Porte blindée contemporaine", cert: "RC3", usage: ["appartement", "maison"], type: "bloc-porte",
      desc: "Portes blindées italiennes aux lignes épurées, disponibles en version thermique pour l'extérieur.",
      specs: ["EN 1627 classe 3", "Version thermique", "Design épuré"], price: "à partir de 3 600 €", badge: "Classe 3", color: "#8a8f96", dark: "#5a5e64", style: "modern" },
    { brand: "Torterolo & Re", name: "Porte blindée sur mesure", cert: "RC3", usage: ["appartement", "maison"], type: "bloc-porte",
      desc: "Portes blindées italiennes fabriquées sur mesure, panneaux bois, laqués ou à moulures classiques.",
      specs: ["EN 1627 classe 3", "Sur mesure", "Panneaux au choix"], price: "à partir de 3 900 €", badge: "Classe 3", color: "#6e2f2a", dark: "#431b18", style: "moulure" },
    { brand: "Stremler", name: "Blindage de porte", cert: "none", usage: ["appartement", "maison"], type: "blindage",
      desc: "Solution de blindage français pour renforcer une porte en bois existante sans changer l'huisserie.",
      specs: ["Blindage acier", "Fabrication française", "Serrure multipoints"], price: "à partir de 1 300 €", color: "#7d5a3c", dark: "#4b3422", style: "plate" },
    { brand: "Toutes marques", name: "Porte blindée de cave / local technique", cert: "none", usage: ["immeuble"], type: "bloc-porte",
      desc: "Porte métallique renforcée pour caves, locaux poubelles, locaux vélos ou locaux techniques en copropriété.",
      specs: ["Acier", "Serrure 3 points", "Ferme-porte"], price: "à partir de 1 200 €", color: "#5b6678", dark: "#394150", style: "lines" },
    { brand: "Toutes marques", name: "Porte blindée de hall d'immeuble", cert: "none", usage: ["immeuble"], type: "bloc-porte",
      desc: "Remplacement de porte d'entrée d'immeuble avec contrôle d'accès (badge, interphone, ventouse).",
      specs: ["Contrôle d'accès", "Ventouse", "Copropriété"], color: "#1f2937", dark: "#0b0f16", style: "glass" }
  ];

  var LOCKS = [
    { brand: "Fichet", name: "Serrure multipoints 787 Z", kind: "multipoints", cert: "A2P3", pose: "encastree", points: 5,
      desc: "Serrure de référence chez Fichet pour portes blindées, mécanisme haute sécurité à clé protégée.",
      specs: ["A2P★★★", "Encastrée", "Clé protégée"], badge: "A2P★★★", color: "#1a2b4f" },
    { brand: "Fichet", name: "Cylindre F3D", kind: "cylindre", cert: "A2P3", pose: "cylindre",
      desc: "Cylindre haute sécurité à clé brevetée, compatible de nombreuses serrures multipoints.",
      specs: ["A2P★★★", "Clé brevetée", "Carte de propriété"], badge: "A2P★★★" },
    { brand: "Mul-T-Lock", name: "Cylindre MT5+", kind: "cylindre", cert: "A2P2", pose: "cylindre",
      desc: "Cylindre réputé pour sa résistance au crochetage et sa clé à reproduction contrôlée.",
      specs: ["A2P selon version", "Anti-crochetage", "Carte de propriété"], badge: "A2P", color: "#e8e8e8", dark: "#9aa1ab" },
    { brand: "Mul-T-Lock", name: "Cylindre Interactive+", kind: "cylindre", cert: "A2P1", pose: "cylindre",
      desc: "Bon compromis prix / sécurité, idéal pour un changement de cylindre sur serrure existante.",
      specs: ["A2P selon version", "Anti-perçage", "Clé protégée"], badge: "A2P", color: "#e8e8e8", dark: "#9aa1ab" },
    { brand: "Vachette", name: "Cylindre Radial NT", kind: "cylindre", cert: "A2P2", pose: "cylindre",
      desc: "Cylindre de sécurité à clé réversible, protections anti-arrachement et anti-perçage.",
      specs: ["A2P selon version", "Clé réversible", "Anti-arrachement"], badge: "A2P" },
    { brand: "Bricard", name: "Serrure multipoints en applique", kind: "multipoints", cert: "A2P2", pose: "applique", points: 3,
      desc: "Serrure 3 points posée en applique, solution efficace pour sécuriser une porte d'appartement sans la changer.",
      specs: ["A2P★★", "En applique", "3 points"], badge: "A2P★★", color: "#33465f" },
    { brand: "Bricard", name: "Cylindre haute sécurité", kind: "cylindre", cert: "A2P3", pose: "cylindre",
      desc: "Cylindre haut de gamme avec clés à reproduction protégée, pour serrures multipoints.",
      specs: ["A2P★★★", "Reproduction protégée"], badge: "A2P★★★" },
    { brand: "Picard Serrures", name: "Serrure multipoints à encastrer", kind: "multipoints", cert: "A2P2", pose: "encastree", points: 5,
      desc: "Serrure 5 points intégrée dans l'épaisseur de la porte, fabrication française.",
      specs: ["A2P selon version", "Encastrée", "5 points"], badge: "A2P", color: "#2b2f36" },
    { brand: "Abus", name: "Cylindre Bravus", kind: "cylindre", cert: "A2P2", pose: "cylindre",
      desc: "Gamme de cylindres modulaires avec niveaux de sécurité adaptés à chaque porte.",
      specs: ["A2P selon version", "Modulaire", "Anti-casse"], badge: "A2P", color: "#e8e8e8", dark: "#9aa1ab" },
    { brand: "Iseo", name: "Cylindre R50", kind: "cylindre", cert: "hs", pose: "cylindre",
      desc: "Cylindre européen à clé plate, bonne résistance aux techniques d'effraction courantes.",
      specs: ["Haute sécurité", "Clé plate", "Anti-bumping"], badge: "Sécurité" },
    { brand: "Cisa", name: "Cylindre AP4 S", kind: "cylindre", cert: "hs", pose: "cylindre",
      desc: "Cylindre de sécurité avec protection anti-bumping et anti-perçage.",
      specs: ["Anti-bumping", "Anti-perçage", "Carte de propriété"], badge: "Sécurité" },
    { brand: "Kaba", name: "Cylindre ExperT", kind: "cylindre", cert: "hs", pose: "cylindre",
      desc: "Cylindre à clé réversible à alvéoles, système breveté de reproduction contrôlée.",
      specs: ["Clé à alvéoles", "Reproduction contrôlée"], badge: "Sécurité", color: "#e8e8e8", dark: "#9aa1ab" },
    { brand: "Keso", name: "Cylindre Keso 8000", kind: "cylindre", cert: "hs", pose: "cylindre",
      desc: "Cylindre très haute sécurité utilisé en résidentiel haut de gamme et en tertiaire.",
      specs: ["Très haute sécurité", "Clé brevetée"], badge: "Sécurité", color: "#e8e8e8", dark: "#9aa1ab" },
    { brand: "Evva", name: "Cylindre 4KS", kind: "cylindre", cert: "hs", pose: "cylindre",
      desc: "Système à courbes de contrôle, conçu pour résister au crochetage et à la copie illicite.",
      specs: ["Anti-crochetage", "Anti-copie"], badge: "Sécurité" },
    { brand: "Mottura", name: "Serrure multipoints Champions", kind: "multipoints", cert: "hs", pose: "encastree", points: 5,
      desc: "Serrure italienne pour porte blindée, déclinable avec cylindre européen haute sécurité.",
      specs: ["Encastrée", "Cylindre européen", "5 points"], badge: "Sécurité", color: "#24272c" },
    { brand: "Toutes marques", name: "Serrure 3 points en applique A2P★", kind: "multipoints", cert: "A2P1", pose: "applique", points: 3,
      desc: "La solution la plus courante pour sécuriser une porte d'entrée en bois : pose rapide, certification A2P.",
      specs: ["A2P★", "En applique", "3 points"], badge: "A2P★", color: "#4a4f57" },
    { brand: "Toutes marques", name: "Verrou de sécurité", kind: "verrou", cert: "A2P1", pose: "applique",
      desc: "Verrou additionnel à cylindre pour renforcer une serrure existante à moindre coût.",
      specs: ["Complément", "Pose rapide"], badge: "Verrou" },
    { brand: "Toutes marques", name: "Serrure connectée / électronique", kind: "connectee", cert: "none", pose: "electronique",
      desc: "Ouverture par code, badge ou smartphone, compatible avec de nombreuses serrures et portes blindées.",
      specs: ["Smartphone", "Code / badge", "Historique d'accès"], badge: "Connectée" }
  ];

  initCatalog({
    rootId: "catalogue-portes",
    data: DOORS.map(function (d, i) { d.id = "d" + i; return d; }),
    filters: ["cert", "usage", "type"],
    prestation: "remplacement",
    visual: function (p) { return doorSVG(p); }
  });

  initCatalog({
    rootId: "catalogue-serrures",
    data: LOCKS.map(function (d, i) { d.id = "l" + i; return d; }),
    filters: ["kind", "cert", "pose"],
    prestation: "serrure",
    visual: function (p) { return lockSVG(p); }
  });
})();
