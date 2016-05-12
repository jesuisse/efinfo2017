import sqlite3
import SQLiteCommands
import Tkinter
import tkMessageBox
from Tkinter import *

conn = sqlite3.connect("NotenDB.sqlite")


def cmdNeueNoteSpeichern(note,fach,datum):
    conn.execute(SQLiteCommands.NeueNote,[note,fach,datum])




def cmdTabelleSemesterAnzeigen():
    conn.execute(SQLiteCommands.TabelleSemester)



def cmdFachAnzeigen(fach):
    conn.execute(SQLiteCommands.FachAnzeigen,[fach])


def cmdNotenschnittFach(fach):
    conn.execute(SQLiteCommands.Notenschnitt,[fach])


def cmdNotenschnittOhneFach(fach):
    conn.execute(SQLiteCommands.NotenschnittOhneFach,[fach])

def cmdZielnoteEingeben(fach,zielNote):
    ZielnoteEingeben = conn.execute(SQLiteCommands.Zielnote,[fach,zielNote])
    return ZielnoteEingeben

def cmdSollnoteAusrechnen(fach):
    SollnoteAnzeigen = conn.execute(SQLiteCommands.Sollnote,[fach])
    return SollnoteAnzeigen

def cmdNurSollnote(fach):
    NurSollnote = conn.execute(SQLiteCommands.NurSollnote,[fach])
    return NurSollnote

def cmdNurZielnote(fach):
    NurZielnote = conn.execute(SQLiteCommands.NurZielnote,[fach])
    return NurZielnote



def runCursor(cmd):
    cursor = cmd
    return cursor
#Fenster
fenster = Tk()
fenster.title("Neues Fenster")
fenster.geometry("800x700")

#Semester Anzeigen
def Tabelle():
    Fenster2 = Tk()
    Fenster2.title("Neues Semester")
    baseCursor = conn.cursor()
    baseCursor.execute("""SELECT Nr, Fach, Noten FROM Semester  order by fach""")
    Resultat = baseCursor.fetchmany(9)
    tst1 = list(Resultat)


    Lb1 = Listbox(Fenster2)
    Lb1.insert(1, "Nr|Note|Fach")
    Lb1.insert(2, tst1[0])
    Lb1.insert(3,tst1[1])
    Lb1.insert(4, tst1[2])
    Lb1.insert(5, tst1[3])
    Lb1.insert(6, tst1[4])
    Lb1.insert(7, tst1[5])
    Lb1.insert(8, tst1[6])
    Lb1.insert(9, tst1[7])
    Lb1.insert(10, tst1[8])


    Lb1.pack()



B = Tkinter.Button(fenster, text = "Noten Tabelle", command = Tabelle)
B.grid(row=10)


#Noten Anzeigen
def Text1():
    baseCursor = conn.cursor()
    baseCursor.execute("""SELECT Fach,Round(AVG(Noten), 2) AS "Durchschnitt", Zielnote,(Round(((SELECT COUNT(Noten)+1)*Zielnote)-(SELECT SUM(Noten)), 2)) AS "Sollnote" FROM Semester NATURAL JOIN Fach_Zielnote WHERE Fach LIKE "Franz"
""")
    Resultat = baseCursor.fetchmany(8)
    tst2 = list(Resultat)
    return tst2

def Text2():
    baseCursor = conn.cursor()
    baseCursor.execute("""SELECT Fach,Round(AVG(Noten), 2) AS "Durchschnitt", Zielnote,(Round(((SELECT COUNT(Noten)+1)*Zielnote)-(SELECT SUM(Noten)), 2)) AS "Sollnote" FROM Semester NATURAL JOIN Fach_Zielnote WHERE Fach LIKE "Deutsch"
""")
    Resultat = baseCursor.fetchmany(8)
    tst2 = list(Resultat)
    return tst2

#Wandelt liste aller Noten in einzelne Liste/Zeile um
Ergebniss = Text1()
Ergebniss2 = Text2()

def Schleife(i):
    for x in range(i,2):
        Zeile_x = Ergebniss[x]
        Rx = list(Ergebniss[x])
        Fach = Rx[0]
        Durchschnitt = Rx[1]
        Zielnote = Rx[2]
        Sollnote = Rx[3]
        var = (Fach,"|", Durchschnitt, "|", Zielnote, "|", Sollnote)
        return var


def Schleife2(i):
    for x in range(i,2):
        Zeile_x = Ergebniss2[x]
        Rx = list(Ergebniss2[x])
        Fach = Rx[0]
        Durchschnitt = Rx[1]
        Zielnote = Rx[2]
        Sollnote = Rx[3]
        var2 = (Fach,"|", Durchschnitt, "|", Zielnote, "|", Sollnote)
        return var2


Lb1 = Listbox(fenster, height= 4, width=50)
Lb1.insert(1, "Fach |Durchschnitt | Zielnote | Sollnote ")
Lb1.insert(2, Schleife(0))
Lb1.insert(3, Schleife2(0))

Lb1.grid(row=6)




#Knopf zum Speichern von allem
def infoSave():
    tkMessageBox.showinfo( "Saved", "Saved")
    note = neueNote.get()
    note = float(note)
    Zielnote = neuezielnote.get()
    Zielnote = float(Zielnote)
    datum = neuesDatum.get()
    fach = neuesFach.get()
    cursor = cmdNeueNoteSpeichern(note,fach,datum)
    cursor2 = cmdZielnoteEingeben(fach,Zielnote)
    conn.commit()

B = Tkinter.Button(fenster, text = "Save", command = infoSave)
B.grid(column=1,row=4)


#Neue Note eingeben


L1 = Label(fenster, text="Neue Note")
L1.grid(row=0)

neueNote = Entry(fenster, bd = 5)

L2 = Label(fenster, text="Fach")
L2.grid(row=1)

neuesFach = Entry(fenster, bd = 5)

L3 = Label(fenster, text="Datum")
L3.grid(row=2)

neuesDatum = Entry(fenster, bd = 5)

L6 = Label(fenster, text="Zielnote")
L6.grid(row=3)

neuezielnote = Entry(fenster, bd = 5)

neueNote.grid(column=1,row=0)
neuesFach.grid(column=1,row=1)
neuesDatum.grid(column=1,row=2)
neuezielnote.grid(column=1,row=3)


fenster.mainloop()

