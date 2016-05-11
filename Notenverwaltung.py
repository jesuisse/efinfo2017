import sqlite3
import SQLiteCommands
import Tkinter
import tkMessageBox
from Tkinter import *

conn = sqlite3.connect("NotenDB.sqlite")


#Abfrage-Funktionen fuer die Datenbank

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

def cmdFachnamen():
    Fachnamen = conn.execute(SQLiteCommands.Fachnamen)
    return Fachnamen

def cmdNurNotenschnitt(fach):
    NurNotenschnitt = conn.execute(SQLiteCommands.NurNotenschnitt,[fach])

def runCursor(cmd):
    cursor = cmd
    return cursor


#GUI

fenster = Tk()
fenster.title("Neues Fenster")
fenster.geometry("500x600")

#GUI: Knopf zum Speichern von allem
def infoSave():
    tkMessageBox.showinfo( "Saved", "Saved")
    note = neueNote.get()
    note = float(note)
    datum = neuesDatum.get()
    fach = neuesFach.get()
    cursor = cmdNeueNoteSpeichern(note,fach,datum)
    conn.commit()

B = Tkinter.Button(fenster, text = "Save", command = infoSave)
B.grid(column=1,row=3)


#GUI: Neue Note eingeben


L1 = Label(fenster, text="Neue Note")
L1.grid(row=0)

neueNote = Entry(fenster, bd = 5)

L2 = Label(fenster, text="Fach")
L2.grid(row=1)

neuesFach = Entry(fenster, bd = 5)

L3 = Label(fenster, text="Datum")
L3.grid(row=2)

neuesDatum = Entry(fenster, bd = 5)

neueNote.grid(column=1,row=0)
neuesFach.grid(column=1,row=1)
neuesDatum.grid(column=1,row=2)






#Varaiablen vorbelegen
faecher = list()
zielnoten = dict()
sollnoten = dict()
durchschnitt = dict()

faecherAktualisieren = cmdFachnamen()

for fach in faecherAktualisieren:
    fache = str(fach)
    faecher.append(fache)
for fach in faecher:
    zielnoten[fach] = cmdNurSollnote(fach)
    sollnoten[fach] = cmdNurSollnote(fach)
    durchschnitt[fach] = cmdNurNotenschnitt(fach)




#
# Notenuebersicht
#
zeile = 1
titelRahmen = Frame(fenster)
titelRahmen.grid()  #Anordung der Elemente im Rahmen
Label(titelRahmen,text="Titel").grid(row=zeile, column=1)
zeile+=1
#Auflistung der Faecher
#Spaltenueberschriften fuer die Tabelle
notenRahmen = Frame(fenster, relief=RAISED, borderwidth=2)
notenRahmen.grid()
Label(notenRahmen, text="Fach").grid(row=zeile, column=1, sticky=W)
Label(notenRahmen, text="Schnitt").grid(row=zeile, column=2)
Label(notenRahmen, text="Zielnote").grid(row=zeile, column=3)
Label(notenRahmen, text="Sollnote").grid(row=zeile, column=4, sticky=W)





#Fuellen der Tabelle
zeile+=2
for fach in faecher:
    Label(notenRahmen, text=fach).grid(row=zeile, column=1, sticky=W)
    Label(notenRahmen, text=str(durchschnitt[fach]).grid(row=zeile, column=2))
    Label(notenRahmen, text=str(zielnoten[fach]).grid(row=zeile, column=3))
    Label(notenRahmen, text=str(sollnoten[fach]).grid(row=zeile, column=4, sticky=W))
    zeile += 1







fenster.mainloop()

