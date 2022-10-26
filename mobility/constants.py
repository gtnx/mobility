import pandas as pd

__all__ = ("motifs", "moyens")

motifs = pd.DataFrame(
    [
        {"key": "1.1", "name": "1.1 - Retour au domicile", "group": ""},
        {
            "key": "1.2",
            "name": "1.2 - Retour à la résidence occasionnelle",
            "group": "",
        },
        {
            "key": "1.3",
            "name": "1.3 - Retour au domicile de parents (hors ménage) ou d’amis",
            "group": "",
        },
        {"key": "1.4", "name": "1.4 - Étudier (école, lycée, université)", "group": ""},
        {
            "key": "1.5",
            "name": "1.5 - Faire garder un enfant en bas âge (nourrice, crèche, famille)",
            "group": "",
        },
        {
            "key": "2.1",
            "name": "2.1 - Se rendre dans une grande surface ou un centre commercial (y compris boutiques et services)",
            "group": "",
        },
        {
            "key": "2.2",
            "name": "2.2 - Se rendre dans un centre de proximité, petit commerce, supérette, boutique, services",
            "group": "",
        },
        {
            "key": "3.1",
            "name": "3.1 - Soins médicaux ou personnels (médecin, coiffeur…)",
            "group": "",
        },
        {
            "key": "4.1",
            "name": "4.1 - Démarche administrative, recherche d’informations",
            "group": "",
        },
        {"key": "4.12", "name": "4.12 - Déchetterie", "group": ""},
        {"key": "5.1", "name": "5.1 - Visite à la famille", "group": ""},
        {"key": "5.2", "name": "5.2 - Visite à des amis", "group": ""},
        {
            "key": "6.1",
            "name": "6.1 - Accompagner quelqu’un à la gare, à l’aéroport, à une station de métro, de bus, de car",
            "group": "",
        },
        {
            "key": "6.2",
            "name": "6.2 - Accompagner quelqu’un à un autre endroit",
            "group": "",
        },
        {
            "key": "6.3",
            "name": "6.3 - Aller chercher quelqu’un à la gare, à l’aéroport, à une station de métro, de bus, de car",
            "group": "",
        },
        {
            "key": "6.4",
            "name": "6.4 - Aller chercher quelqu’un à un autre endroit",
            "group": "",
        },
        {
            "key": "7.1",
            "name": "7.1 - Activité associative, cérémonie religieuse, réunion",
            "group": "",
        },
        {
            "key": "7.2",
            "name": "7.2 - Aller dans un centre de loisir, parc d’attraction, foire",
            "group": "",
        },
        {
            "key": "7.3",
            "name": "7.3 - Manger ou boire à l’extérieur du domicile",
            "group": "",
        },
        {
            "key": "7.4",
            "name": "7.4 - Visiter un monument ou un site historique",
            "group": "",
        },
        {
            "key": "7.5",
            "name": "7.5 - Voir un spectacle culturel ou sportif (cinéma, théâtre, concert, cirque, match), assister à une",
            "group": "",
        },
        {"key": "7.6", "name": "7.6 - Faire du sport", "group": ""},
        {
            "key": "7.7",
            "name": "7.7 - Se promener sans destination précise",
            "group": "",
        },
        {"key": "7.8", "name": "7.8 - Se rendre sur un lieu de promenade", "group": ""},
        {"key": "8.1", "name": "8.1 - Vacances hors résidence secondaire", "group": ""},
        {
            "key": "8.2",
            "name": "8.2 - Se rendre dans une résidence secondaire",
            "group": "",
        },
        {
            "key": "8.3",
            "name": "8.3 - Se rendre dans une résidence occasionnelle",
            "group": "",
        },
        {"key": "8.4", "name": "8.4 - Autres motifs personnels", "group": ""},
        {
            "key": "9.1",
            "name": "9.1 - Travailler dans son lieu fixe et habituel",
            "group": "",
        },
        {
            "key": "9.2",
            "name": "9.2 - Travailler en dehors d’un lieu fixe et habituel, sauf tournée (chantier, contacts professionnels,",
            "group": "",
        },
        {
            "key": "9.3",
            "name": "9.3 - Stages, conférence, congrès, formations, exposition",
            "group": "",
        },
        {
            "key": "9.4",
            "name": "9.4 - Tournées professionnelles (VRP) ou visites de patients",
            "group": "",
        },
        {"key": "9.5", "name": "9.5 - Autres motifs professionnels", "group": ""},
        {"key": "9999.0", "name": "9999.0 - Unknown", "group": ""},
    ]
)
motifs.set_index("key", inplace=True)

moyens = pd.DataFrame(
    [
        {"key": "1.1", "name": "1.1 - Uniquement marche à pied", "group": "Piéton"},
        {
            "key": "1.2",
            "name": "1.2 - Porté, transporté en poussette",
            "group": "Piéton",
        },
        {"key": "1.3", "name": "1.3 - Rollers, trottinette", "group": "Piéton"},
        {
            "key": "1.4",
            "name": "1.4 - Fauteuil roulant (y compris motorisé)",
            "group": "Piéton",
        },
        {
            "key": "2.1",
            "name": "2.1 - Bicyclette, tricycle (y compris à assistance électrique) sauf vélo en libre-service",
            "group": "Deux Roues",
        },
        {"key": "2.2", "name": "2.2 - Vélo en libre-service", "group": "Deux Roues"},
        {
            "key": "2.3",
            "name": "2.3 - Cyclomoteur (2 roues de moins de 50 cm3) – Conducteur",
            "group": "Deux Roues",
        },
        {
            "key": "2.4",
            "name": "2.4 - Cyclomoteur (2 roues de moins de 50 cm3) – Passager",
            "group": "Deux Roues",
        },
        {
            "key": "2.5",
            "name": "2.5 - Moto (plus de 50 cm3) – Conducteur (y compris avec side-car et scooter à trois roues)",
            "group": "Deux Roues",
        },
        {
            "key": "2.6",
            "name": "2.6 - Moto (plus de 50 cm3) – Passager (y compris avec side-car et scooter à trois roues)",
            "group": "Deux Roues",
        },
        {
            "key": "2.7",
            "name": "2.7 - Motocycles sans précision (y compris quads)",
            "group": "Deux Roues",
        },
        {
            "key": "3.1",
            "name": "3.1 - Voiture, VUL, voiturette… – Conducteur",
            "group": "Automobile",
        },
        {
            "key": "3.2",
            "name": "3.2 - Voiture, VUL, voiturette… – Passager",
            "group": "Automobile",
        },
        {
            "key": "3.3",
            "name": "3.3 - Voiture, VUL, voiturette… – Tantôt conducteur tantôt passager",
            "group": "Automobile",
        },
        {
            "key": "3.4",
            "name": "3.4 - Trois ou quatre roues sans précision",
            "group": "Automobile",
        },
        {
            "key": "4.1",
            "name": "4.1 - Taxi (individuel, collectif), VTC",
            "group": "Transport spécialisé, scolaire, taxi",
        },
        {
            "key": "4.2",
            "name": "4.2 - Transport spécialisé (handicapé)",
            "group": "Transport spécialisé, scolaire, taxi",
        },
        {
            "key": "4.3",
            "name": "4.3 - Ramassage organisé par l'employeur",
            "group": "Transport spécialisé, scolaire, taxi",
        },
        {
            "key": "4.4",
            "name": "4.4 - Ramassage scolaire",
            "group": "Transport spécialisé, scolaire, taxi",
        },
        {
            "key": "5.1",
            "name": "5.1 - Autobus urbain, trolleybus",
            "group": "Transport en commun urbain ou régional, autocar",
        },
        {
            "key": "5.2",
            "name": "5.2 - Navette fluviale",
            "group": "Transport en commun urbain ou régional, autocar",
        },
        {
            "key": "5.3",
            "name": "5.3 - Autocar de ligne (sauf SNCF)",
            "group": "Transport en commun urbain ou régional, autocar",
        },
        {
            "key": "5.4",
            "name": "5.4 - Autre autocar (affrètement, service spécialisé)",
            "group": "Transport en commun urbain ou régional, autocar",
        },
        {
            "key": "5.5",
            "name": "5.5 - Autocar TER",
            "group": "Transport en commun urbain ou régional, autocar",
        },
        {
            "key": "5.6",
            "name": "5.6 - Tramway",
            "group": "Transport en commun urbain ou régional, autocar",
        },
        {
            "key": "5.7",
            "name": "5.7 - Métro, VAL, funiculaire",
            "group": "Transport en commun urbain ou régional, autocar",
        },
        {
            "key": "5.8",
            "name": "5.8 - RER, SNCF banlieue",
            "group": "Transport en commun urbain ou régional, autocar",
        },
        {
            "key": "5.9",
            "name": "5.9 - TER",
            "group": "Transport en commun urbain ou régional, autocar",
        },
        {
            "key": "5.10",
            "name": "5.10 - Autres transports urbains et régionaux (sans précision)",
            "group": "Transport en commun urbain ou régional, autocar",
        },
        {
            "key": "6.1",
            "name": "6.1 - Train à grande vitesse, 1ère classe (TGV, Eurostar, etc.)",
            "group": "Train grande ligne ou Train à grande vitesse",
        },
        {
            "key": "6.2",
            "name": "6.2 - Train à grande vitesse, 2ème classe (TGV, Eurostar, etc.)",
            "group": "Train grande ligne ou Train à grande vitesse",
        },
        {
            "key": "6.3",
            "name": "6.3 - Autre train, 1ère classe",
            "group": "Train grande ligne ou Train à grande vitesse",
        },
        {
            "key": "6.4",
            "name": "6.4 - Autre train, 2ème classe",
            "group": "Train grande ligne ou Train à grande vitesse",
        },
        {
            "key": "6.5",
            "name": "6.5 - Train, sans précision",
            "group": "Train grande ligne ou Train à grande vitesse",
        },
        {
            "key": "7.1",
            "name": "7.1 - Avion, classe première ou affaires",
            "group": "Avion",
        },
        {
            "key": "7.2",
            "name": "7.2 - Avion, classe premium économique",
            "group": "Avion",
        },
        {"key": "7.3", "name": "7.3 - Avion, classe économique", "group": "Avion"},
        {"key": "8.1", "name": "8.1 - Bateau", "group": "Bateau"},
        {"key": "9.1", "name": "9.1 - Autre", "group": "Autre"},
    ]
)
moyens.set_index("key", inplace=True)


tuus = pd.DataFrame(
    [
        {"key": 0, "name": "0 - Commune hors unité urbaine"},
        {
            "key": 1,
            "name": "1 - Commune appartenant à une unité urbaine de 2 000 à 4 999 habitants",
        },
        {
            "key": 2,
            "name": "2 - Commune appartenant à une unité urbaine de 5 000 à 9 999 habitants",
        },
        {
            "key": 3,
            "name": "3 - Commune appartenant à une unité urbaine de 10 000 à 19 999 habitants",
        },
        {
            "key": 4,
            "name": "4 - Commune appartenant à une unité urbaine de 20 000 à 49 999 habitants",
        },
        {
            "key": 5,
            "name": "5 - Commune appartenant à une unité urbaine de 50 000 à 99 999 habitants ",
        },
        {
            "key": 6,
            "name": "6 - Commune appartenant à une unité urbaine de 100 000 à 199 999 habitants",
        },
        {
            "key": 7,
            "name": "7 - Commune appartenant à une unité urbaine de 200 000 à 1 999 999 habitants",
        },
        {"key": 8, "name": "8 - Commune appartenant à l'unité urbaine de Paris"},
    ]
)
tuus.set_index("key", inplace=True)
