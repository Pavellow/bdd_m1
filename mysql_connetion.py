from datetime import timedelta
from SQLConn import *
import random

# Les fonctions populate_xxx() permettent de générer des données aléatoires pour les tables de la base de données
# Si vous voulez générer des scripts, ne touchez pas à ces fonctions
# Si vous voulez ajouter des données dans la base de données, décommenter la ligne ecrire_dans_fichier jsp quoi
# et décommentez la ligne add_xxx_bdd() en modifiant les infos pour la base de données dans les variables de la ligne 26 à 30

filieres = [
    {"Faculté": 0, "Filière": "Droit Notarial"},
    {"Faculté": 2, "Filière": "Information Communication"},
    {"Faculté": 2, "Filière": "Gestion et Accompagnement des Publics à Besoins Spécifiques"},
    {"Faculté": 8, "Filière": "Gestion des Entreprises et des Administrations - Techniques de Commercialisation"},
    {"Faculté": 3, "Filière": "Santé, Gestion de l'Environnement, Informatique, Risques et Environnement"},
    {"Faculté": 5, "Filière": "Métiers de l’Enseignement, de l’Éducation et de la Formation"},
    {"Faculté": 8, "Filière": "Commercialisation des Produits Touristiques"},
    {"Faculté": 3, "Filière": "Sciences Pour l'Ingénieur"},
    {"Faculté": 3, "Filière": "Informatique"},
    # Ajout des DUT et BUT avec la faculté 9
    *[
        {"Faculté": 9, "Filière": dut_filiere}
        for dut_filiere in [
            "Génie Civil", 
            "Métiers du Multimédia et de l'Internet", 
            "Techniques de commercialisations", 
            "Génie Biologique", 
            "Génie Électrique et Informatique Industrielle", 
            "Génie Mécanique et Productique", 
            "Gestion Administrative et Commerciale", 
            "Gestion des Entreprises et des Administrations", 
            "Informatique", 
            "Carrières Juridiques", 
            "Métiers du Livre", 
            "Carrières Sociales", 
            "Gestion Logistique et Transport", 
            "Qualité, Logistique Industrielle et Organisation", 
            "Réseaux et Télécommunications", 
            "Statistique et Informatique Décisionnelle", 
            "Techniques de Commercialisation", 
            "Techniques de Commercialisation (en apprentissage)"
        ]
    ]
]

from Composante import *
from Etudiant import *
from Compte import *
from Diplome import *
from Etape import *
from Entreprise import *
from Enseignant import *
from Tuteur import *
from Stage import *
from Inscription import *

from util  import *
from faker import Faker

faker = Faker('fr_FR')
faker_it  = Faker('it_IT')

host = "localhost"
user = "admin"
password = "admin"
db = "tp_bdd"

# utile pour le peuplement des tables
deja_used_randint = []

sql = SQLConn(host, user, password, db)
conn = sql.connect_to_bdd()

sql_operator = SQLConn(host, user, password, db)

tables = ['composante', 'compte', 'diplome', 'enseignant', 'entreprise', 'etape', 'etudiant', 'feedbacks_archives', 'inscription', 'stage', 'tuteur']

#sql_operator.update_row("composante", "Libelle_composante = 'Composante 25'", "id_composante = 1")
#sql_operator.delete_row("composante", "id_composante = 0")

def reset_ai_table(table):
    sql_operator.reset_ai(table)

def reset_ai_all_tables(tables):
    for table in tables:
        sql_operator.reset_ai(table)

def populate_composante():
    libelles_composante = ["Faculté de Droit et de Science Politique", "Institut d'Études Judiciaires (IEJ)", "Faculté des Lettres, langues, arts, sciences humaines et sociales (FLLASHS)", "Faculté des Sciences et techniques (FST)", "École d’ingénieurs Paoli Tech", "Institut National Supérieur du Professorat et de l’Éducation (INSPÉ)", "EME-IAE de Corse / École de Management et d'Économie", "Institut Universitaire de Santé (IUS)", "Institut Universitaire de Technologie (IUT)", "École doctorale Environnement et Société"]
    composante = Composante("")
    for libelle in libelles_composante:
        composante.set_libelle(libelle)
        composante.add_composante_bdd(conn)
        #composante.ecrire_requete_dans_fichier("composantes.sql") 

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
            print(diplome)
            diplome = diplome["Filière"]
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
    {"Faculté": 3, "Filière": "Informatique"},
    # Ajout des DUT et BUT avec la faculté 9
    *[
        {"Faculté": 9, "Filière": dut_filiere}
        for dut_filiere in [
            "Génie Civil", 
            "Métiers du Multimédia et de l'Internet", 
            "Techniques de commercialisations", 
            "Génie Biologique", 
            "Génie Électrique et Informatique Industrielle", 
            "Génie Mécanique et Productique", 
            "Gestion Administrative et Commerciale", 
            "Gestion des Entreprises et des Administrations", 
            "Informatique", 
            "Carrières Juridiques", 
            "Métiers du Livre", 
            "Carrières Sociales", 
            "Gestion Logistique et Transport", 
            "Qualité, Logistique Industrielle et Organisation", 
            "Réseaux et Télécommunications", 
            "Statistique et Informatique Décisionnelle", 
            "Techniques de Commercialisation", 
            "Techniques de Commercialisation (en apprentissage)"
        ]
    ]
]
    exclusions = [
    "Master Sciences Pour l'Ingénieur",
    "Doctorat Sciences Pour l'Ingénieur",
    "Licence Informatique"
]
    combinaisons_diplomes = generer_diplomes(diplomes, filieres, exclusions)
    for i in range(len(combinaisons_diplomes)):
        diplome = Diplome(combinaisons_diplomes[i][1], combinaisons_diplomes[i][0] + 1)
        diplome.add_diplome_bdd(conn)
        #diplome.ecrire_requete_dans_fichier("diplomes.sql")

def define_dico_diplome_inverse():
    diplomes = sql_operator.get_row("diplome", "")
    dico_diplomes_inverse = {}
    for diplome in diplomes:
        id_diplome, libelle_diplome, _ = diplome
        dico_diplomes_inverse[libelle_diplome] = id_diplome

    return dico_diplomes_inverse


def populate_etape():
    diplomes = define_dico_diplome()
    etapes = ["L1", "L2", "L3", "M1", "M2"]
    etapes_dict = {"L1": 1, "L2": 2, "L3": 3, "M1": 4, "M2": 5}
    
    exclusions = [
    "Master Sciences Pour l'Ingénieur",
    "Doctorat Sciences Pour l'Ingénieur",
    "Licence Informatique"
    ]
    i = 1
    combi = generer_etapes(diplomes, etapes, exclusions, etapes_dict)
    for result in combi:
        result.append(i)
        i += 1
        niveau = result[0]
        etape = result[1]
        resp = result[2]
        with open("sortie.txt", "a") as f:
            f.write(str(result) + "\n\n")
        #etape.add_etape_bdd(conn)

"""     dut = ["Génie Civil", "Métiers du Multimédia et de l'Internet", "Techniques de commercialisations", "Génie Biologique", "Génie Électrique et Informatique Industrielle", "Génie Mécanique et Productique", "Gestion Administrative et Commerciale", "Gestion des Entreprises et des Administrations", "Informatique", "Carrières Juridiques", "Métiers du Livre", "Carrières Sociales", "Gestion Logistique et Transport", "Qualité, Logistique Industrielle et Organisation", "Réseaux et Télécommunications", "Statistique et Informatique Décisionnelle", "Techniques de Commercialisation", "Techniques de Commercialisation (en apprentissage)", "Techniques de Commercialisation (en apprentissage)", "Techniques de Commercialisation (en apprentissage)"]
    niveau = ["DUT 1", "DUT 2", "BUT 1", "BUT 2", "BUT 3"]
    niveau_dict = {"DUT 1": 11, "DUT 2": 12, "BUT 1": 13, "BUT 2": 14, "BUT 3": 15}
    combin = generer_etapes(dut, niveau, [], niveau_dict)
    for etape in combin:
        etape = Etape(etape[1], etape[0], i)
        i += 1
        print(etape) """
        #etape.add_etape_bdd(conn)
        #etape.ecrire_requete_dans_fichier("etapes.sql")

def populate_etape_v2():
    i = 1
    nivl1 = ["L1", "L2", "L3"]
    nivel2 = ["M1", "M2"]
    etapes_dict = {"L1": 1, "L2": 2, "L3": 3, "M1": 4, "M2": 5}
    dico_dip = define_dico_diplome_inverse()

    for libelle, id_dip in dico_dip.items():
        dip_split = libelle.split()
        if dip_split[0] == "Licence":
            for niv in nivl1:
                dip_split[0] = niv
                niveau = etapes_dict[niv]
                etape = Etape(id_dip, " ".join(dip_split), niveau, i)
                etape.add_etape_bdd(conn)
                i += 1
        elif dip_split[0] == "Master":
            for niv in nivel2:
                dip_split[0] = niv
                niveau = etapes_dict[niv]
                etape = Etape(id_dip, " ".join(dip_split), niveau, i)
                etape.add_etape_bdd(conn)
                i += 1
        elif dip_split[0] == "Doctorat":
            etape = Etape(id_dip, " ".join(dip_split), 6, i)
            etape.add_etape_bdd(conn)
            i += 1

def genere_siret():
    numero_siren = ''.join([str(random.randint(0, 9)) for _ in range(9)])
    numero_sequentiel = ''.join([str(random.randint(0, 9)) for _ in range(5)])
    return numero_siren + numero_sequentiel

def populate_entreprise():
    nom = faker.company()
    adresse_entreprise = faker.address()
    entreprise = Entreprise(genere_siret(), nom, adresse_entreprise)
    entreprise.add_entreprise_bdd(conn)
    #entreprise.ecrire_requete_dans_fichier("entreprises.sql")

def populate_compte():
    prenom = faker.name().split()[0]
    nom = faker_it.name().split()[-1]
    compte = Compte(generate_random_string(), nom, prenom)
    print(compte)
    compte.add_compte_bdd(conn)
    #compte.ecrire_requete_dans_fichier("comptes.sql")

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

def populate_enseignant(i):    
        enseignant = Enseignant(i)
        enseignant.add_enseignant_bdd(conn)
        #enseignant.ecrire_requete_dans_fichier("enseignants.sql")

def attribuer_filiere_et_compter_etudiants(nb_etudiants, nb_filieres):
    attribution_filiere = {}
    compteur_etudiants_par_filiere = {filiere: 0 for filiere in range(1, nb_filieres + 1)}

    for id_etudiant in range(2502, 2502 + nb_etudiants):
        id_filiere = random.randint(1, nb_filieres)
        attribution_filiere[id_etudiant] = id_filiere
        compteur_etudiants_par_filiere[id_filiere] += 1

    return attribution_filiere, compteur_etudiants_par_filiere

def populate_etudiant(i):
    etudiant = Etudiant(i)
    etudiant.add_etudiant_bdd(conn)
    #etudiant.ecrire_requete_dans_fichier("etudiants.sql")

def populate_tuteur(nbr_tuteurs):
    for _ in range(nbr_tuteurs):
        tuteur = Tuteur(faker.name(), random.randint(1, 200))
        tuteur.add_tuteur_bdd(conn)
        #tuteur.ecrire_requete_dans_fichier("tuteurs.sql")

def get_l3m1m2():
    cur = conn.cursor()
    cur.execute("SELECT etudiant.id_etudiant FROM etudiant JOIN inscription ON inscription.id_etudiant = etudiant.id_etudiant JOIN etape ON etape.id_etape = inscription.id_etape WHERE etape.Niveau = 3 OR etape.Niveau = 4 OR etape.Niveau = 5 GROUP BY etudiant.id_etudiant")
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

def populate_inscription():
    etudiants = sql_operator.get_row("etudiant", "")
    etapes = sql_operator.get_row("etape", "")
    i = 0
    if i >= len(etudiants):
        return
    for etudiant in etudiants:
        id_etudiant = etudiant[0]
        for etape in etapes:
            id_etape = etape[0]
            annee = random.randint(2008, 2024)
            inscription = Inscription(id_etape, id_etudiant, annee)
            inscription.add_inscription_bdd(conn)
            id_etudiant  = random.randint(0, 4501)
            i += 1
            #inscription.ecrire_requete_dans_fichier("inscriptions.sql")

def get_date_inscription(id_etudiant, conn):
    """ Récupère la date d'inscription d'un étudiant. """
    cur = conn.cursor()
    cur.execute("SELECT annee FROM inscription WHERE id_etudiant = %s", (id_etudiant))
    result = cur.fetchone()
    cur.close()
    return result[0] if result else None


def generer_stage_non_chevauchant(id_etudiant, nb_entreprises, nb_tuteurs, stages_existants, conn):

    while True:
        date_inscription = get_date_inscription(id_etudiant, conn)
        id_entreprise = random.randint(1, nb_entreprises)
        id_tuteur = random.randint(1, nb_tuteurs)
        feedback_stage = faker.text()
        feedback_entreprise = faker.text()
        feedback_prof = faker.text()
        etat = random.choice(['En cours', 'Terminé', 'Planifié'])
        date_debut = faker.date_between(start_date=date_inscription, end_date='today')
        date_fin = date_debut + timedelta(days=random.randint(30, 180))  # Durée du stage entre 1 et 6 mois
        annee_debut = date_debut.year
        # Vérifier que le stage ne se chevauche pas et débute après l'inscription
        if annee_debut >= date_inscription and not any(d_fin > date_debut and d_debut < date_fin for d_debut, d_fin in stages_existants.get(id_etudiant, [])):
            note = random.randint(0, 20) if etat == 'Terminé' else -1
            stage = (id_etudiant, id_entreprise, id_tuteur, feedback_stage, feedback_entreprise, feedback_prof, etat, date_debut, date_fin, note)

            # Mise à jour des périodes de stage pour l'étudiant
            if id_etudiant not in stages_existants:
                stages_existants[id_etudiant] = []
            stages_existants[id_etudiant].append((date_debut, date_fin))

            return stage


def ajouter_stages(conn, nbr_iter, nb_entreprises, nb_tuteurs):
    l3m1m2 = get_l3m1m2()
    stages_existants = {}  # Dictionnaire pour suivre les périodes de stages des étudiants

    for _ in range(nbr_iter):
        for etud in l3m1m2:
            stage = generer_stage_non_chevauchant(etud[0], nb_entreprises, nb_tuteurs, stages_existants, conn)
            if stage:  # Vérifier si un stage a été généré
                obj_stage = Stage(stage[0], stage[1], stage[2], stage[3], stage[4], stage[5], stage[6], stage[7], stage[8], stage[9])
                obj_stage.add_stage_bdd(conn)
            else:
                print(f"Aucun stage généré pour l'étudiant {etud[0]}")


def reset_all_tables(tables):
    sql_operator.delete_all_data(tables)

def reset_all():
    reset_all_tables(tables)
    reset_ai_all_tables(tables)

def populate_all():

    #REPERENIVEAUPEUPLEMENT 1

    # Suppression des données existantes et remise à zéro des auto-increment
    reset_all()
    # Peuplement de la table composante
    populate_composante()
    # Peuplement de la table compte (ajout de 10000 comptes)
    for _ in range(10000):
        populate_compte()
    #Peuplement de la table entreprise (ajout de 400 entreprises)
    for _ in range(400):
        populate_entreprise()

    #REPERENIVEAUPEUPLEMENT 2

    # Peuplement de la table diplome
    populate_diplome()
    # Peuplement de la table enseignant (ajout de 500 enseignants)
    for i in range(500):
        populate_enseignant(i)
    #peuplement de la table etudiant (ajout de 5000 étudiants)
    for j in range(5000):
        populate_etudiant(j)

    #REPERENIVEAUPEUPLEMENT 3

    populate_etape_v2()
    populate_tuteur(400)

    #REPERENIVEAUPEUPLEMENT 4

    populate_inscription()

    #REPERENIVEAUPEUPLEMENT 5

    ajouter_stages(conn, 10000, 400, 400)

#############################################################################################################

ajouter_stages(conn, 10000, 400, 400)

sql.close_connection()