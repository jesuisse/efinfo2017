
#Neue Note
NeueNote = """INSERT INTO Semester (Noten,Fach,Datum) VALUES (?,?,?)"""

#TabelleSemester
TabelleSemester = """SELECT * FROM Semester"""

#Bestimmtes Fach anzeigen
BestimmtesFach = """SELECT * FROM Semester WHERE Fach LIKE "fach" """

#Notenschnitt fuer bestimmtes Fach berechnen
Notenschnitt = """SELECT Fach,AVG(Noten) AS "Durchschnitt" FROM Semester WHERE Fach LIKE "fach" """

#Zielnote eingeben
Zielnote = """INSERT INTO Fach_Zielnote (Fach,Zielnote) VALUES ("fach",5.5)"""

#Sollnote ausrechnen
Sollnote = """SELECT Fach,Zielnote,(((COUNT(Noten)+1)*Zielnote)-(SELECT SUM(Noten))) AS "Sollnote" FROM Semester NATURAL JOIN Fach_Zielnote WHERE Fach LIKE "fach" """

#Alle Faecher anzeigen
AlleFaecher = """SELECT Fach,AVG(Noten) AS "Durchschnitt", Zielnote,(((SELECT COUNT(Noten)+1)*Zielnote)-(SELECT SUM(Noten))) AS "Sollnote" FROM Semester NATURAL JOIN Fach_Zielnote WHERE Fach LIKE "fach" """

