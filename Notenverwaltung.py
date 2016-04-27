import sqlite3
import SQLiteCommands

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




