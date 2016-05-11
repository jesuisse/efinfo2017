import Tkinter
import sqlite3
import tkMessageBox
from Tkinter import *

import SQLiteCommands

conn = sqlite3.connect("NotenDB.sqlite")


def cmdNeueNoteSpeichern(note,fach,datum):
    conn.execute(SQLiteCommands.NeueNote, [note, fach, datum])




def cmdTabelleSemesterAnzeigen():
    conn.execute(SQLiteCommands.TabelleSemester)


def cmdFachAnzeigen(fach):
    conn.execute(SQLiteCommands.FachAnzeigen, [fach])


def cmdNotenschnittFach(fach):
    conn.execute(SQLiteCommands.Notenschnitt, [fach])


def cmdNotenschnittOhneFach(fach):
    conn.execute(SQLiteCommands.NotenschnittOhneFach, [fach])

def cmdZielnoteEingeben(fach,zielNote):
    ZielnoteEingeben = conn.execute(SQLiteCommands.Zielnote, [fach, zielNote])
    return ZielnoteEingeben

def cmdSollnoteAusrechnen(fach):
    SollnoteAnzeigen = conn.execute(SQLiteCommands.Sollnote, [fach])
    return SollnoteAnzeigen

def cmdNurSollnote(fach):
    NurSollnote = conn.execute(SQLiteCommands.NurSollnote, [fach])
    return NurSollnote

def cmdNurZielnote(fach):
    NurZielnote = conn.execute(SQLiteCommands.NurZielnote, [fach])
    return NurZielnote



def runCursor(cmd):
    cursor = cmd
    return cursor




#neue note eingeben











fenster = Tk()
fenster.title("Neues Fenster")
fenster.geometry("500x600")

#Knopf zum Speichern von allem
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

neueNote.grid(column=1,row=0)
neuesFach.grid(column=1,row=1)
neuesDatum.grid(column=1,row=2)

fenster.mainloop()

