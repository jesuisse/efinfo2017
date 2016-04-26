import sqlite3
import SQLiteCommands

conn = sqlite3.connect("NotenDB.sqlite")


def cmdNeueNoteSpeichern(note,fach,datum):
    neueNote = conn.execute(SQLiteCommands.NeueNote,[note,fach,datum])
    return neueNote


def cmdTabelleSemesterAnzeigen():
    TabelleSemester = conn.execute(SQLiteCommands.TabelleSemester)
    return TabelleSemester

cmdNeueNoteSpeichern(5.4, "Deutsch", "25.04.2016")

