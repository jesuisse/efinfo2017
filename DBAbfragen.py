import sqlite3
conn = sqlite3.connect("C:/Users/17dte.GYMBIEL.001/Desktop/NotenDB.db")
sqlIns = "Insert into Fach Values('Zielnote',?)"
conn.execute(sqlIns,(5,))
cursor = conn.execute("Select* from Fach")


