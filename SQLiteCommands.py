
#Neue Note
NeueNote = """INSERT INTO Semester (Noten,Fach,Datum) VALUES (?,?,?)"""


#Alle Fachnamen anzeigen
Fachnamen = """SELECT Fach FROM Fach_Zielnote"""

#TabelleSemester
TabelleSemester = """SELECT * FROM Semester"""

#Bestimmtes Fach anzeigen
FachAnzeigen = """SELECT * FROM Semester WHERE Fach LIKE ? """

#Notenschnitt fuer bestimmtes Fach berechnen
Notenschnitt = """SELECT Fach,AVG(Noten) AS "Durchschnitt" FROM Semester WHERE Fach LIKE ? """

#Nur Notenschnitt
NurNotenschnitt = """SELECT AVG(Noten) AS "Durchschnitt" FROM Semester WHERE Fach like ? """

#Notenschnitt fuer bestimmtes Fach berechnen ohne Fachanzeige
NotenschnittOhneFach = """SELECT AVG(Noten) AS "Durchschnitt" FROM Semester WHERE Fach LIKE ? """

#Zielnote fuer Fach eingeben
Zielnote = """INSERT INTO Fach_Zielnote (Fach,Zielnote) VALUES (?,?)"""

#Sollnote ausrechnen und alles anzeigen
Sollnote = """SELECT Fach,Zielnote,(((COUNT(Noten)+1)*Zielnote)-(SELECT SUM(Noten))) AS "Sollnote" FROM Semester NATURAL JOIN Fach_Zielnote WHERE Fach LIKE ? """

#Nur Sollnote anzeigen
NurSollnote = """SELECT (((COUNT(Noten)+1)*Zielnote)-(SELECT SUM(Noten))) AS "Sollnote" FROM Semester NATURAL JOIN Fach_Zielnote WHERE Fach LIKE ?"""

#Nur Zielnote anzeigen
NurZielnote = """SELECT Zielnote FROM Semester NATURAL JOIN Fach_Zielnote WHERE Fach LIKE ? """

#Alle Faecher anzeigen
#AlleFaecher = """SELECT Fach,AVG(Noten) AS "Durchschnitt", Zielnote,(((SELECT COUNT(Noten)+1)*Zielnote)-(SELECT SUM(Noten))) AS "Sollnote" FROM Semester NATURAL JOIN Fach_Zielnote WHERE Fach LIKE "fach" """


