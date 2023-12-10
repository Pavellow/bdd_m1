from datetime import timedelta
from SQLConn import *
import random

from Composante import *
from Etudiant import *
from Compte import *
from Diplome import *
from Etape import *
from Entreprise import *
from Enseignant import *
from Tuteur import *
from Stage import *

from util  import *
from faker import Faker

faker = Faker('fr_FR')
faker_it  = Faker('it_IT')

host = "localhost"
user = "admin"
password = "admin"
db = "bdd_tp_test"

# utile pour le peuplement des tables
deja_used_randint = []

sql = SQLConn(host, user, password, db)
conn = sql.connect_to_bdd()

sql_operator = SQLConn(host, user, password, db)

#sql_operator.update_row("composante", "Libelle_composante = 'Composante 25'", "id_composante = 1")
#sql_operator.delete_row("composante", "id_composante = 0")

def populate_composante():
    libelles_composante = ["Faculté de Droit et de Science Politique", "Institut d'Études Judiciaires (IEJ)", "Faculté des Lettres, langues, arts, sciences humaines et sociales (FLLASHS)", "Faculté des Sciences et techniques (FST)", "École d’ingénieurs Paoli Tech", "Institut National Supérieur du Professorat et de l’Éducation (INSPÉ)", "EME-IAE de Corse / École de Management et d'Économie", "Institut Universitaire de Santé (IUS)", "Institut Universitaire de Technologie (IUT)", "École doctorale Environnement et Société"]
    composante = Composante("", 0)
    i = 0
    for libelle in libelles_composante:
        composante.set_libelle(libelle)
        composante.set_id(i)
        i += 1
        #composante.add_composante_bdd(conn)
        composante.ecrire_requete_dans_fichier("composantes.sql") 

def generer_diplomes(diplomes, filieres, exclusions):
    combinaisons = []
    for filiere in filieres:
        for diplome in diplomes:
            # Création de la combinaison diplôme-filière
            combinaison = f"{diplome} {filiere['Filière']}"
            if combinaison not in exclusions:
                # Ajout de l'indice de la faculté et de la combinaison dans une liste
                combinaison_finale = [filiere['Faculté'], combinaison]
                combinaisons.append(combinaison_finale)
    return combinaisons

def generer_etapes(diplomes, etapes, exclusions, etapes_dict):
    combinaisons = []
    for etape in etapes:
        for diplome in diplomes:
            # Création de la combinaison étape-diplôme
            combinaison = f"{etape} {diplome}"
            if combinaison not in exclusions:
                # Utilisation de l'entier correspondant à l'étape
                etape_index = etapes_dict[etape]
                combinaison_finale = [etape_index, combinaison]
                combinaisons.append(combinaison_finale)
    return combinaisons

def populate_diplome():
    diplomes = ["Licence", "Master", "Doctorat"]
    filieres = [
    {"Faculté": 0, "Filière": "Droit Notarial"},
    {"Faculté": 2, "Filière": "Information Communication"},
    {"Faculté": 2, "Filière": "Gestion et Accompagnement des Publics à Besoins Spécifiques"},
    {"Faculté": 8, "Filière": "Gestion des Entreprises et des Administrations - Techniques de Commercialisation"},
    {"Faculté": 3, "Filière": "Santé, Gestion de l'Environnement, Informatique, Risques et Environnement"},
    {"Faculté": 5, "Filière": "Métiers de l’Enseignement, de l’Éducation et de la Formation"},
    {"Faculté": 8, "Filière": "Commercialisation des Produits Touristiques"},
    {"Faculté": 3, "Filière": "Sciences Pour l'Ingénieur"},
    {"Faculté": 3, "Filière": "Informatique"}
    ]
    exclusions = [
    "Master Sciences Pour l'Ingénieur",
    "Doctorat Sciences Pour l'Ingénieur",
    "Licence Informatique"
]
    combinaisons_diplomes = generer_diplomes(diplomes, filieres, exclusions)
    for i in range(len(combinaisons_diplomes)):
        diplome = Diplome(combinaisons_diplomes[i][1], combinaisons_diplomes[i][0])
        #diplome.add_diplome_bdd(conn)
        diplome.ecrire_requete_dans_fichier("diplomes.sql")

def populate_etape():
    etapes = ["L1", "L2", "L3", "M1", "M2"]
    etapes_dict = {"L1": 1, "L2": 2, "L3": 3, "M1": 4, "M2": 5}
    filieres = [
    "Droit Notarial",
    "Information Communication",
    "Gestion et Accompagnement des Publics à Besoins Spécifiques",
    "Gestion des Entreprises et des Administrations - Techniques de Commercialisation",
    "Santé, Gestion de l'Environnement, Informatique, Risques et Environnement",
    "Métiers de l’Enseignement, de l’Éducation et de la Formation",
    "Commercialisation des Produits Touristiques",
    "Sciences Pour l'Ingénieur",
    "Informatique"
        ]
    exclusions = [
    "Master Sciences Pour l'Ingénieur",
    "Doctorat Sciences Pour l'Ingénieur",
    "Licence Informatique"
    ]
    combi = generer_etapes(filieres, etapes, exclusions, etapes_dict)
    for result in combi:
        etape = Etape(result[1], result[0])
        etape.ecrire_requete_dans_fichier("etapes.sql")

    dut = ["Génie Civil", "Métiers du Multimédia et de l'Internet", "Techniques de commercialisations", "Génie Biologique", "Génie Électrique et Informatique Industrielle", "Génie Mécanique et Productique", "Gestion Administrative et Commerciale", "Gestion des Entreprises et des Administrations", "Informatique", "Carrières Juridiques", "Métiers du Livre", "Carrières Sociales", "Gestion Logistique et Transport", "Qualité, Logistique Industrielle et Organisation", "Réseaux et Télécommunications", "Statistique et Informatique Décisionnelle", "Techniques de Commercialisation", "Techniques de Commercialisation (en apprentissage)", "Techniques de Commercialisation (en apprentissage)", "Techniques de Commercialisation (en apprentissage)"]
    niveau = ["DUT 1", "DUT 2", "BUT 1", "BUT 2", "BUT 3"]
    niveau_dict = {"DUT 1": 11, "DUT 2": 12, "BUT 1": 13, "BUT 2": 14, "BUT 3": 15}
    combin = generer_etapes(dut, niveau, [], niveau_dict)
    for etape in combin:
        etape = Etape(etape[1], etape[0])
        #etape.add_etape_bdd(conn)
        etape.ecrire_requete_dans_fichier("etapes.sql")

def populate_entreprise():
    nom = faker.company()
    entreprise = Entreprise(nom)
    #entreprise.add_entreprise_bdd(conn)
    entreprise.ecrire_requete_dans_fichier("entreprises.sql")

def populate_compte():
    prenom = faker.name().split()[0]
    nom = faker_it.name().split()[-1]
    compte = Compte(generate_random_string(), nom, prenom)
    print(compte)
    #compte.add_compte_bdd(conn)
    compte.ecrire_requete_dans_fichier("comptes.sql")

def choisir_entier_aleatoire_unique(min_val, max_val, deja_utilises):
    while True:
        entier_aleatoire = random.randint(min_val, max_val)
        if entier_aleatoire not in deja_utilises:
            deja_utilises.append(entier_aleatoire)
            return entier_aleatoire

def populate_enseignant_aleatoire(deja_used_randint):
    entier = choisir_entier_aleatoire_unique(0, 2000, deja_used_randint)
    enseignant = Enseignant(entier)
    enseignant.add_enseignant_bdd(conn)

def populate_etudiant_aleatoire(deja_used_randint):
    entier = choisir_entier_aleatoire_unique(0, 2000, deja_used_randint)
    etudiant = Etudiant(entier, entier)
    etudiant.add_etudiant_bdd(conn)

def populate_enseignant():
    for i in range(200):
        enseignant = Enseignant(i)
        #enseignant.add_enseignant_bdd(conn)
        enseignant.ecrire_requete_dans_fichier("enseignants.sql")

def attribuer_filiere_et_compter_etudiants(nb_etudiants, nb_filieres):
    attribution_filiere = {}
    compteur_etudiants_par_filiere = {filiere: 0 for filiere in range(1, nb_filieres + 1)}

    for id_etudiant in range(201, 201 + nb_etudiants):
        id_filiere = random.randint(1, nb_filieres)
        attribution_filiere[id_etudiant] = id_filiere
        compteur_etudiants_par_filiere[id_filiere] += 1

    return attribution_filiere, compteur_etudiants_par_filiere

def populate_etudiant():
    attribution, comptage = attribuer_filiere_et_compter_etudiants(1500, 145)
    for id_etudiant in attribution:
        etudiant = Etudiant(attribution[id_etudiant], id_etudiant)
        #etudiant.add_etudiant_bdd(conn)
        etudiant.ecrire_requete_dans_fichier("etudiants.sql")

def populate_tuteur(nbr_tuteurs):
    for _ in range(nbr_tuteurs):
        tuteur = Tuteur(faker.name(), random.randint(1, 200))
        #tuteur.add_tuteur_bdd(conn)
        tuteur.ecrire_requete_dans_fichier("tuteurs.sql")

def get_l3m1m2():
    cur = conn.cursor()
    cur.execute("SELECT id_etudiant FROM etudiant INNER JOIN etape ON etudiant.id_filiere = etape.id_filiere WHERE etape.Niveau = 3 OR etape.Niveau = 4 OR etape.Niveau = 5; ")
    rows = cur.fetchall()
    cur.close()
    return rows
"""
def generer_stage(id_etudiant, nb_entreprises, nb_tuteurs):
    stages = []
    etudiants_ayant_un_stage = set()

    id_entreprise = random.randint(1, nb_entreprises)
    id_tuteur = random.randint(1, nb_tuteurs)
    feedback_stage = faker.text()
    feedback_entreprise = faker.text()
    feedback_prof = faker.text()
    etat = random.choice(['En cours', 'Terminé', 'Planifié'])
    date_debut = faker.date_between(start_date='-2y', end_date='today')
    date_fin = date_debut + timedelta(days=random.randint(30, 180))  # Durée du stage entre 1 et 6 mois
    etudiants_ayant_un_stage.add(id_etudiant)
    if etat == 'Terminé':
        note = random.randint(0, 20)
    else:
        note = -1
    stage = (id_etudiant, id_entreprise, id_tuteur, feedback_stage, feedback_entreprise, feedback_prof, etat, date_debut, date_fin, note)
    stages.append(stage)

    return stages """

def generer_stage_non_chevauchant(id_etudiant, nb_entreprises, nb_tuteurs, stages_existants):
    while True:
        id_entreprise = random.randint(1, nb_entreprises)
        id_tuteur = random.randint(1, nb_tuteurs)
        feedback_stage = faker.text()
        feedback_entreprise = faker.text()
        feedback_prof = faker.text()
        etat = random.choice(['En cours', 'Terminé', 'Planifié'])
        date_debut = faker.date_between(start_date='-4y', end_date='today')
        date_fin = date_debut + timedelta(days=random.randint(30, 180))  # Durée du stage entre 1 et 6 mois

        # Vérifier le chevauchement
        chevauche = any(d_fin > date_debut and d_debut < date_fin for d_debut, d_fin in stages_existants.get(id_etudiant, []))
        if not chevauche:
            note = random.randint(0, 20) if etat == 'Terminé' else -1
            stage = (id_etudiant, id_entreprise, id_tuteur, feedback_stage, feedback_entreprise, feedback_prof, etat, date_debut, date_fin, note)

            # Mise à jour des périodes de stage pour l'étudiant
            if id_etudiant not in stages_existants:
                stages_existants[id_etudiant] = []
            stages_existants[id_etudiant].append((date_debut, date_fin))

            return stage

def ajouter_stages(conn, nbr_iter,  nb_entreprises, nb_tuteurs):
    l3m1m2 = get_l3m1m2()
    stages_existants = {}  # Dictionnaire pour suivre les périodes de stages des étudiants
    for _ in range(nbr_iter):
        for etud in l3m1m2:
            stage = generer_stage_non_chevauchant(etud[0], nb_entreprises, nb_tuteurs, stages_existants)
            obj_stage = Stage(stage[0], stage[1], stage[2], stage[3], stage[4], stage[5], stage[6], stage[7], stage[8], stage[9])
            obj_stage.add_stage_bdd(conn)

#Génération de composante.sql
#populate_composante()

#Génération de diplome.sql
#populate_diplome()

#Génération de etape.sql
#populate_etape()

#Génération de entreprise.sql
""" for i in range(200):
    populate_entreprise() """

#Génération de compte.sql
""" for i in range(2000):
    populate_compte() """

#Génération de enseignant.sql
#populate_enseignant()

#Génération de etudiant.sql
#populate_etudiant()

#Génération de tuteur.sql
#populate_tuteur(200)

#Génération de stage.sql
ajouter_stages(conn, 4,  1000, 1000)

sql.close_connection()