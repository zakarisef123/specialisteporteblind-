# Spécialiste Porte Blindée — site web

Site vitrine statique (HTML / CSS / JavaScript) pour une entreprise de remplacement de portes blindées,
blindage de portes et installation / changement de serrures. Les pages sont **générées** par un script
Python (sans dépendance) puis versionnées : le site se publie tel quel, sans étape de compilation.

## Modifier le site

1. Modifier les fichiers de `_src/` (voir ci-dessous) ;
2. lancer `python3 _src/build.py` ;
3. vérifier en local : `python3 -m http.server 8000` puis http://localhost:8000 ;
4. commiter les fichiers générés.

| Fichier | Rôle |
|---|---|
| `_src/config.py` | **Coordonnées, WhatsApp, mentions légales, Google Tag Manager, lien avis Google** |
| `_src/products.json` | Catalogue des portes et serrures (fiches produits + catalogues filtrables) |
| `_src/brands.py` | Les marques (logo, catégories, description) → pages `/marques/` |
| `_src/finitions.py` | Coloris RAL, habillages, poignées, options et prix de base du configurateur |
| `_src/guides.py` | Les guides de conseil → pages `/guides/` |
| `_src/zones.json` | Les 153 communes du Var (source : geo.api.gouv.fr) → une page d'accueil localisée par commune dans `/zones/` |
| `_src/pages/*.py` | Accueil, catalogues, mentions légales, page merci |
| `_src/generators.py` | Pages marques, produits, guides, zones, simulateur, réalisations, à propos, plan du site, 404 |
| `assets/css/style.css` | Styles |
| `assets/js/main.js` | Menu, catalogues, simulateur de prix, avant / après, suivi des clics |

## Pages générées (~165)

- Accueil, catalogues **Portes blindées** et **Serrures** (filtres + recherche)
- **52 fiches produits** (`/produits/`) et **40 pages marques** (`/marques/`)
- **153 pages commune** (`/zones/`) : la page d'accueil déclinée pour chaque commune du Var
- **Ouverture, dépannage et déblocage de porte blindée** : 3 pages de service
- **5 guides** (`/guides/`) : prix, certification A2P, blindage ou bloc-porte, assurance, serrure
- **Configurateur de porte** (aperçu en direct + estimation), **Finitions & coloris**, **Comparateur** (3 modèles), **Professionnels & syndics**
- Pages marques avec tableau comparatif de la gamme, finitions et catalogue PDF (impression)
- **Simulateur de prix**, **Réalisations** (avant / après + galerie), **Qui sommes-nous**, plan du site, 404
- `sitemap.xml` et `robots.txt` régénérés à chaque build

## À personnaliser AVANT la mise en ligne

Tout se trouve dans `_src/config.py` : nom, téléphone, WhatsApp, e-mail, adresse, zone, horaires,
domaine, mentions légales (SIRET, assurance décennale, médiateur…), identifiant Google Tag Manager.
La zone d'intervention est le Var (83) : pour la modifier, remplacez `_src/zones.json`.

Vérifiez aussi que les engagements affichés correspondent à votre activité réelle (assurance décennale,
devis gratuit, pose en une journée, budgets indicatifs). N'ajoutez des avis clients que s'ils sont
authentiques : les faux avis sont interdits par le Code de la consommation.

## Suivi des conversions

Renseignez `GTM_ID` dans `_src/config.py`. Le site envoie dans `dataLayer` les événements
`clic_appel`, `clic_whatsapp`, `envoi_formulaire` et `simulateur_resultat`, à relier à Google Ads / GA4 dans GTM.

## Mise en ligne (Netlify)

`netlify.toml` est prêt : publication du dossier racine, en-têtes de sécurité et de cache, `_src/` non exposé.
Le formulaire de devis utilise **Netlify Forms** : les demandes apparaissent dans le tableau de bord Netlify
(notifications par e-mail à activer dans *Forms → Notifications*).

## Logos et photos

- `assets/img/marques/` : 38 logos de fabricants (repris du dépôt Shopta-serrure).
- `assets/img/photos/` : photos d'interventions (reprises du dépôt Shopta-serrure, redimensionnées).

Les logos indiquent les marques installées ; le site précise que l'entreprise est un installateur indépendant.
Ne pas se présenter comme revendeur agréé d'une marque (ex. réseau « Point Fort Fichet ») sans l'être.
