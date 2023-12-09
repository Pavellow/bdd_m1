from SQLConn import *

from Composante import *

host = "localhost"
user = "admin"
password = "admin"
db = "bdd_tp_test"

sql = SQLConn(host, user, password, db)
sql.connect()

composante = Composante()

test = "a"