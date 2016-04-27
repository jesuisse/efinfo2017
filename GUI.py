import sqlite3
import tkFont
from Tkinter import *
from datetime import date

#Datei mit den SQL Befehlen importieren
#import notenSQL
#Klassendefinitionen importieren
from SQLiteCommands import *

#Verbindung zur Datenbank
conn = sqlite3.connect('NotenDB.sqlite')
#Ein einfaches SQL ausfuehren
cursor = conn.execute("SELECT titel FROM buch WHERE buchid = '1'")
for row in cursor:
    print row[0]


#Varaiablen vorbelegen
VarNoten = dict()
VarFaecher = dict()

today = date.today()

#diese Daten kommen aus der Datenbank - hier Beispiele hart-codiert
VarNoten['Deutsch'] = FachNoten('Deutsch', [4.5, 4.75])
VarNoten['Informatik'] = FachNoten('Informatik', [5, 5.5])

VarFaecher['Deutsch'] = FachDefn('Deutsch', 4, 5)
VarFaecher['Informatik'] = FachDefn('Informatik', 4.5, 5)

#Ausgabe in der Console testen
text =  "Fach    \tSchnitt\tMin.\tNoten"
for fach in VarNoten:
    text += "\n" + fach + "\t" + str(VarNoten[fach].durchschnitt) + "\t" + \
            str(VarFaecher[fach].mindestNote(len(VarNoten[fach].notenliste), VarNoten[fach].durchschnitt)) + "\t" + \
            str(VarNoten[fach].notenliste)

print text

#
### Funktion fuer den Push-Button
#
def noteEingeben():
    print("Neue Eingabe: " + str(eingabeFeld.get()) + " Neues Datum " + str(datumNeu.get()))

#
# GUI GUI GUI
#
### Neues Fenster
#
fenster = Tk()
fenster.title("Neues Fenster")
fenster.geometry("500x600")

# Schriftarten definieren
titelFont1 = tkFont.Font(family="Helvetica", size=14, weight=tkFont.BOLD)
titelFont2 = tkFont.Font(family="Helvetica", size= 11, weight=tkFont.BOLD, underline=1)
buttonFont = tkFont.Font(family="Helvetica", size= 10, weight=tkFont.BOLD)

#
# Notenuebersicht
#
zeile = 1
titelRahmen = Frame(fenster)
titelRahmen.grid()  #Anordung der Elemente im Rahmen
Label(titelRahmen,text="Titel", font=titelFont1).grid(row=zeile, column=1)
zeile+=1
#Auflistung der Noten
#Spaltenueberschriften fuer die Tabelle
notenRahmen = Frame(fenster, relief=RAISED, borderwidth=2)
notenRahmen.grid()
Label(notenRahmen, text="Fach", font=titelFont2).grid(row=zeile, column=1, sticky=W)
Label(notenRahmen, text="Schnitt", font=titelFont2).grid(row=zeile, column=2)
Label(notenRahmen, text="Min/Ziel", font=titelFont2).grid(row=zeile, column=3)
Label(notenRahmen, text="Noten", font=titelFont2).grid(row=zeile, column=4, sticky=W)

#Fuellen der Tabelle
zeile+=2
for fach in sorted(VarNoten):
    Label(notenRahmen, text=fach).grid(row=zeile, column=1, sticky=W)
    Label(notenRahmen, text=str(VarNoten[fach].durchschnitt)).grid(row=zeile, column=2)
    Label(notenRahmen, text=str(VarFaecher[fach].mindestNote(len(VarNoten[fach].notenliste), VarNoten[fach].durchschnitt))+"/"+
                            str(VarFaecher[fach].zielnote)).grid(row=zeile, column=3)
    Label(notenRahmen, text=str(VarNoten[fach].notenliste)).grid(row=zeile, column=4, sticky=W)
    zeile += 1

#
# Eingabe Rahmen
#  Im Rahmen wird eine Auswahl des Faches, zwei Eingabefelder und ein Knopf, um die Aktion zu starten gezeichnet
#
eingabeRahmen = Frame(fenster, borderwidth=2, relief=RAISED)
eingabeRahmen.grid()

#Titelzeile
zeile = 1
Label(eingabeRahmen,text="Neues eingeben", font=titelFont1).grid(row=zeile, column=1)
zeile += 1

#Knoepfe zum Auswaehlen eines Faches
fach = StringVar()
for f in sorted(VarFaecher):
    knopf = Radiobutton(eingabeRahmen, text = f, variable = fach, value = f)
    knopf.grid(row=zeile, column=1, sticky=W)
    zeile += 1
#Um sicherzustellen, dass nur ein Knopf aktiviert ist, wird der Letzte selektiert
knopf.select()

#Eingabefeld
zeile = 2
Label(eingabeRahmen,text="Eingabe: ").grid(row=zeile,column=4)
eingabeFeld = Entry(eingabeRahmen, bd=5)
eingabeFeld.grid(row=zeile,column=5)

#Eingabefeld fuer eine Datumseingabe. Das Feld wird mit einem Default Wert vorbelegt.
zeile += 1
Label(eingabeRahmen,text="Datum: ").grid(row=zeile,column=4)
datumNeu = Entry(eingabeRahmen, bd=5)
datumNeu.insert(0, str(today))
datumNeu.grid(row=zeile,column=5)

#Aktion (command) durch Druecken auf den Knopf starten
#   Die Funktion, welche dem command uebergeben wird, muss vorgaengig definiert sein.
zeile += 1
noteNeuButton = Button(eingabeRahmen, text="Durchfuehren", font=buttonFont, command=noteEingeben).grid(row=zeile,column=5)


# GUI wartet auf Benutzeraktivitaet
fenster.mainloop()

# Die Daten auf der Datenbank sichern
conn.commit()
# Verbindung zur Datenbank schliessen.
conn.close()
