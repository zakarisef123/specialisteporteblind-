# Finitions proposées (configurateur + page Finitions & coloris)
# Les disponibilités exactes dépendent du fabricant et de la gamme : elles sont confirmées sur le devis.

# (code, nom, couleur principale, couleur des moulures/ombres)
COLORIS = [
    ("RAL 7016", "Gris anthracite", "#383e42", "#24282b"),
    ("RAL 9005", "Noir foncé", "#141416", "#000000"),
    ("RAL 9016", "Blanc signalisation", "#f1f0ea", "#c9c8c1"),
    ("RAL 7035", "Gris clair", "#cbd0cc", "#9fa5a1"),
    ("RAL 7039", "Gris quartz", "#6b665e", "#48443e"),
    ("RAL 5011", "Bleu acier", "#1f2c3a", "#111a24"),
    ("RAL 6009", "Vert sapin", "#27352a", "#161f18"),
    ("RAL 3004", "Rouge pourpre", "#6d1a22", "#460f15"),
    ("RAL 1015", "Ivoire clair", "#e6d2b5", "#b9a68b"),
    ("Chêne doré", "Placage bois", "#9c6b3c", "#6b4624"),
    ("Noyer", "Placage bois", "#5a3d2b", "#3a2619"),
]

# (identifiant du dessin, nom, description)
PANNEAUX = [
    ("classic", "Classique à panneaux", "Deux panneaux en relief, l'aspect traditionnel des portes palières."),
    ("moulure", "Mouluré haussmannien", "Moulures et panneau cintré, pour respecter le style des immeubles anciens."),
    ("modern", "Contemporain lisse", "Panneau lisse à fine rainure verticale, lignes épurées."),
    ("lines", "Rainures horizontales", "Rainures usinées horizontales, style design."),
    ("glass", "Vitré sécurisé", "Vitrage feuilleté retardateur d'effraction, pour les portes de maison."),
    ("plate", "Acier brut", "Tôle d'acier apparente : caves, locaux techniques, blindages."),
]

# (identifiant, nom)
POIGNEES = [
    ("alu", "Aluminium brossé"),
    ("inox", "Inox poli"),
    ("noir", "Noir mat"),
    ("laiton", "Laiton"),
]

# (identifiant, nom, description, supplément min, supplément max)
OPTIONS = [
    ("judas", "Judas numérique", "Écran intérieur, vision grand angle, éventuellement avec enregistrement.", 150, 350),
    ("seuil", "Seuil à la suisse", "Seuil en applique qui améliore l'étanchéité à l'air et au bruit.", 120, 250),
    ("barre", "Barre de seuil automatique", "Joint qui descend à la fermeture : isolation sans seuil apparent.", 150, 300),
    ("acoustique", "Acoustique renforcée", "Joints et remplissage pour atténuer les bruits du palier.", 250, 600),
    ("thermique", "Isolation thermique", "Pour une porte donnant sur l'extérieur.", 300, 700),
    ("connectee", "Serrure connectée", "Ouverture par code, badge ou smartphone.", 250, 500),
]

# Prix de base indicatifs posés selon la certification (min, max)
NIVEAUX = [
    ("none", "Non certifiée", "Budget minimal", 1800, 3000),
    ("BP1", "A2P BP1", "5 min · appartement", 3000, 5000),
    ("BP2", "A2P BP2", "10 min · RDC, maison", 4500, 7000),
    ("BP3", "A2P BP3", "15 min · haute valeur", 7000, 10000),
]
