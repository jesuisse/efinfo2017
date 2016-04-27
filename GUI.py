import sqlite3
import tkFont
from Tkinter import *
from datetime import date

#Datei mit den SQL Befehlen importieren
#import notenSQL
#Klassendefinitionen importieren
from notenObjekte import *

#Verbindung zur Datenbank
conn = sqlite3.connect('BuchVerwaltung.sqlite')
#Ein einfaches SQL ausfuehren
cursor = conn.execute("SELECT titel FROM buch WHERE buchid = '1'")
for row in cursor:
    print row[0]


#Varaiablen vorbelegen
noten = dict()
faecher = dict()

today = date.today()

#diese Daten kommen aus der Datenbank - hier Beispiele hart-codiert
noten['Deutsch'] = FachNoten('Deutsch', [4.5, 4.75])
noten['Informatik'] = FachNoten('Informatik', [5, 5.5])

faecher['Deutsch'] = FachDefn('Deutsch', 4, 5)
faecher['Informatik'] = FachDefn('Informatik', 4.5, 5)

#Ausgabe in der Console testen
text =  "Fach    \tSchnitt\tMin.\tNoten"
for fach in noten:
    text += "\n" + fach + "\t" + str(noten[fach].durchschnitt) + "\t" + \
            str(faecher[fach].mindestNote(len(noten[fach].notenliste), noten[fach].durchschnitt)) + "\t" + \
            str(noten[fach].notenliste)

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
for fach in sorted(noten):
    Label(notenRahmen, text=fach).grid(row=zeile, column=1, sticky=W)
    Label(notenRahmen, text=str(noten[fach].durchschnitt)).grid(row=zeile, column=2)
    Label(notenRahmen, text=str(faecher[fach].mindestNote(len(noten[fach].notenliste), noten[fach].durchschnitt))+"/"+
                            str(faecher[fach].zielnote)).grid(row=zeile, column=3)
    Label(notenRahmen, text=str(noten[fach].notenliste)).grid(row=zeile, column=4, sticky=W)
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
for f in sorted(faecher):
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
