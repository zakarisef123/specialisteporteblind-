# Spécialiste Porte Blindée — site web

Site vitrine statique (HTML / CSS / JavaScript, sans dépendance) pour une entreprise de
remplacement de portes blindées, blindage de portes et installation / changement de serrures.

## Pages

| Fichier | Contenu |
|---|---|
| `index.html` | Accueil : services, marques, certifications A2P, tarifs indicatifs, FAQ, formulaire de devis |
| `portes-blindees.html` | Catalogue filtrable des portes blindées (marque, certification, logement, solution) |
| `serrures.html` | Catalogue filtrable des serrures et cylindres |
| `mentions-legales.html` | Mentions légales + politique de confidentialité (RGPD) |
| `merci.html` | Page de confirmation après envoi du formulaire |

Les produits des catalogues sont définis dans `assets/js/main.js` (tableaux `DOORS` et `LOCKS`) :
ajoutez, retirez ou modifiez une entrée pour mettre à jour le catalogue.

## À personnaliser AVANT la mise en ligne

Remplacez dans **tous les fichiers `.html`** (rechercher / remplacer) :

- `Spécialiste Porte Blindée` → nom de l'entreprise
- `01 23 45 67 89` et `+33123456789` → votre numéro
- `contact@specialiste-porte-blindee.fr` → votre e-mail
- `12 rue de l'Exemple, 75000 Paris` → votre adresse
- `Paris & Île-de-France` → votre zone d'intervention
- `Lun – Sam : 8h – 20h` → vos horaires
- `https://www.specialiste-porte-blindee.fr` → votre domaine (aussi dans `robots.txt` et `sitemap.xml`)
- Les champs surlignés `[...]` dans `mentions-legales.html` (SIRET, assurance décennale, médiateur, hébergeur)

Vérifiez aussi que les engagements affichés correspondent à votre activité réelle
(assurance décennale, devis et déplacement gratuits, délais, budgets indicatifs).

N'ajoutez des avis clients que s'ils sont authentiques (ex. widget Google Business) :
les faux avis sont interdits par le Code de la consommation.

## Formulaire de devis

Le formulaire est prêt pour **Netlify Forms** (attribut `data-netlify="true"`) : une fois le site
déployé sur Netlify, les demandes arrivent dans le tableau de bord et peuvent être envoyées par e-mail.
Sur un autre hébergeur, remplacez l'attribut `action` du formulaire par un service comme Formspree.

## Aperçu en local

```bash
python3 -m http.server 8000
```

Puis ouvrir http://localhost:8000
