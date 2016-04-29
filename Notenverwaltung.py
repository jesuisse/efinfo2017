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




#neue note eingeben











fenster = Tk()
fenster.title("Neues Fenster")
fenster.geometry("500x600")

#Knopf zum Speichern von allem
def noteSave():
    tkMessageBox.showinfo( "Saved", "Saved")
    note = neueNote.get()
    note = float(note)
    cursor = cmdNeueNoteSpeichern(note,"Deutsch","29.04.2016")
    conn.commit()

B = Tkinter.Button(fenster, text = "Save", command = noteSave)
B.pack()


#Neue Note eingeben
L1 = Label(fenster, text="Neue Note")
L1.pack(side = LEFT)
neueNote = Entry(fenster, bd = 5)

L2 = Label(fenster, text="Fach")
L2.pack(side = LEFT)
fach = Entry(fenster, bd = 5)

L3 = Label(fenster, text="Datum")
L3.pack(side = LEFT)
datum = Entry(fenster, bd = 5)

neueNote.pack(side = RIGHT)
fach.pack(side = RIGHT)
datum.pack(side = RIGHT)

fenster.mainloop()

