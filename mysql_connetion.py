from SQLConn import *

from Composante import *
from Etudiant import *

host = "localhost"
user = "admin"
password = "admin"
db = "bdd_tp_test"

sql = SQLConn(host, user, password, db)
conn = sql.connect_to_bdd()

etudiant = Etudiant()