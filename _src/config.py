# ==========================================================
#  CONFIGURATION DU SITE — à personnaliser
#  Modifiez ce fichier puis relancez :  python3 _src/build.py
# ==========================================================

NAME = "Spécialiste Porte Blindée"
DOMAIN = "https://www.specialiste-porte-blindee.fr"   # sans / final

PHONE = "01 23 45 67 89"          # affiché
PHONE_TEL = "+33123456789"        # format international pour les liens tel:
WHATSAPP = "33123456789"          # numéro WhatsApp sans + ni espaces ("" pour masquer le bouton)
EMAIL = "contact@specialiste-porte-blindee.fr"
STREET = "12 rue de l'Exemple"
POSTCODE = "75000"
CITY = "Paris"
ZONE = "Paris & Île-de-France"
HOURS = "Lun – Sam : 8h – 20h"
HOURS_SCHEMA = "Mo-Sa 08:00-20:00"

# Mentions légales (laisser "" tant que non renseigné : un repère jaune s'affiche)
LEGAL = {
    "forme": "", "capital": "", "siret": "", "rcs": "", "tva": "",
    "directeur": "", "assureur": "", "contrat": "", "mediateur": "",
    "hebergeur": "Netlify, Inc. — 512 2nd Street, Suite 200, San Francisco, CA 94107, USA",
}

# Suivi des conversions : identifiant Google Tag Manager (ex. "GTM-XXXXXXX"), "" pour désactiver.
# Le site envoie dans dataLayer : clic_appel, clic_whatsapp, envoi_formulaire, simulateur_resultat.
GTM_ID = ""

# Lien vers votre fiche Google (avis). "" pour masquer les liens « Voir nos avis Google ».
GOOGLE_REVIEWS_URL = ""
