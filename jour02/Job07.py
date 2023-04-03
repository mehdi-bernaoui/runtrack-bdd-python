#import de mysql Connector

import mysql.connector

#definition base de données:
# éléments de connextion: host, user, pass, base de donnée.
db = mysql.connector.connect(
	host= "localhost",
	user = "root",
	password = "root",
	database = "Job07"
)


#création d'un curseur et exécution d'une requête sql
cur = db.cursor()
cur.execute("select * from employes where salaire > 3000")

#fetch des infos de la requête et print en ligne

res = cur.fetchall()
for line in res:
	print(line)
cur.close()


cur = db.cursor()
cur.execute("SELECT employes.id, employes.nom, prenom, services.nom, salaire FROM employes inner join services on employes.id_service = services.id;")

#fetch des infos de la requête et print en ligne

res = cur.fetchall()
for line in res:
	print(line)
cur.close()