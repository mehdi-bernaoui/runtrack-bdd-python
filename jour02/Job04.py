#import de mysql Connector

import mysql.connector

#definition base de données:
# éléments de connextion: host, user, pass, base de donnée.
db = mysql.connector.connect(
	host= "localhost",
	user = "root",
	password = "root",
	database = "laplateforme"
)


#création d'un curseur et exécution d'une requête sql
cur = db.cursor()
cur.execute("SELECT nom, capacite FROM salles")

#fetch des infos de la requête et print en ligne

res = cur.fetchall()
for line in res:
	print(line)
cur.close()