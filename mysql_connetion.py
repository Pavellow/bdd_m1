from SQLConn import *

from Composante import *
from Etudiant import *
from Compte import *

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

def populate_diplome():
    diplomes = ["Licence", "Master", "Doctorat"]
    pass

def populate_etape():
    etapes = ["L1", "L2", "L3", "M1", "M2"]
    pass

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

sql.close_connection()
