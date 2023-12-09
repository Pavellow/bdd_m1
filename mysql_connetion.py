from SQLConn import *

from Composante import *
from Etudiant import *
from Compte import *
from Diplome import *
from Etape import *
from Entreprise import *

from util  import *
from faker import Faker

faker = Faker('fr_FR')
faker_it  = Faker('it_IT')

host = "localhost"
user = "admin"
password = "admin"
db = "bdd_tp_test"

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
        composante.add_composante_bdd(conn) 

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
        diplome.add_diplome_bdd(conn)

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
        etape.add_etape_bdd(conn)

    dut = ["Génie Civil", "Métiers du Multimédia et de l'Internet", "Techniques de commercialisations", "Génie Biologique", "Génie Électrique et Informatique Industrielle", "Génie Mécanique et Productique", "Gestion Administrative et Commerciale", "Gestion des Entreprises et des Administrations", "Informatique", "Carrières Juridiques", "Métiers du Livre", "Carrières Sociales", "Gestion Logistique et Transport", "Qualité, Logistique Industrielle et Organisation", "Réseaux et Télécommunications", "Statistique et Informatique Décisionnelle", "Techniques de Commercialisation", "Techniques de Commercialisation (en apprentissage)", "Techniques de Commercialisation (en apprentissage)", "Techniques de Commercialisation (en apprentissage)"]
    niveau = ["DUT 1", "DUT 2", "BUT 1", "BUT 2", "BUT 3"]
    niveau_dict = {"DUT 1": 11, "DUT 2": 12, "BUT 1": 13, "BUT 2": 14, "BUT 3": 15}
    combin = generer_etapes(dut, niveau, [], niveau_dict)
    for etape in combin:
        etape = Etape(etape[1], etape[0])
        etape.add_etape_bdd(conn)

def populate_entreprise():
    nom = faker.company()
    entreprise = Entreprise(nom)
    entreprise.add_entreprise_bdd(conn)

def populate_etudiant():
    etudiant = Etudiant("", "")

def populate_compte():
    prenom = faker.name().split()[0]
    nom = faker_it.name().split()[-1]
    compte = Compte(generate_random_string(), nom, prenom)
    print(compte)
    compte.add_compte_bdd(conn)

""" for i in range(1000):
    populate_compte() """

""" for i in range(100):
    Entreprise(faker.company()).add_entreprise_bdd(conn) """

# Il y a actuellement 2001 comptes sur la bdd


sql.close_connection()