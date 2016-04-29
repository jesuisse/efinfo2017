import sqlite3
import SQLiteCommands
import Tkinter
import tkMessageBox
from Tkinter import *

conn = sqlite3.connect("NotenDB.sqlite")


def cmdNeueNoteSpeichern(note,fach,datum):
    neueNote = conn.execute(SQLiteCommands.NeueNote,[note,fach,datum])
    return neueNote


def cmdTabelleSemesterAnzeigen():
    TabelleSemester = conn.execute(SQLiteCommands.TabelleSemester)
    return TabelleSemester

def cmdFachAnzeigen(fach):
    BestimmtesFachAnzeigen = conn.execute(SQLiteCommands.FachAnzeigen,[fach])
    return BestimmtesFachAnzeigen

def cmdNotenschnittFach(fach):
    NotenschnittAnzeigen = conn.execute(SQLiteCommands.Notenschnitt,[fach])
    return NotenschnittAnzeigen

def cmdNotenschnittOhneFach(fach):
    NotenschnittAnzeigen = conn.execute(SQLiteCommands.NotenschnittOhneFach,[fach])
    return NotenschnittAnzeigen

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




#neue note eingeben
neueNote = eingabe.get()



cursor = runCursor(cmdFachAnzeigen("Franz"))
for row in cursor:
    print row









fenster = Tk()
fenster.title("Neues Fenster")
fenster.geometry("500x600")

#Knopf zum Speichern von allem
def infoSave():
    tkMessageBox.showinfo( "Saved", "Saved")
B = Tkinter.Button(fenster, text = "Save", command = infoSave)
B.pack()


#Neue Note eingeben
L1 = Label(fenster, text="Neue Note")
L1.pack(side = LEFT)
neueNote = Entry(fenster, bd = 5)

neueNote.pack(side = RIGHT)

fenster.mainloop()

