#Klassendefinitionen importieren
import sqlite3
import tkFont
from Tkinter import *
from datetime import date
from Notenverwaltung import *

#Verbindung zur Datenbank
conn = sqlite3.connect('BuchVerwaltung.sqlite')


noten = dict()
fachnoten = dict()
faecher = dict()

today = date.today()

#diese Daten kommen aus der Datenbank - hier Beispiele hart-codiert
noten['Semester'] = cmdTabelleSemesterAnzeigen()

fachnoten['Deutsch'] = cmdFachAnzeigen("Deutsch")
fachnoten['Franz'] = cmdFachAnzeigen('Franz')

faecher["Deutsch"] = cmdSollnoteAusrechnen("Deutsch")
faecher["Franz"] = cmdSollnoteAusrechnen("Franz")



#Ausgabe in der Console testen
text =  "Fach    \tSchnitt\tZielnote\tSollnote"
for fach in fachnoten:
    text += "\n" + fach + "\t" + str(cmdNotenschnittOhneFach(fach)) + "\t" + \
            str(cmdNurZielnote(fach)) + "\t" + \
            str(cmdNurSollnote(fach))

print text


#
### Funktion fuer den Push-Button
#
#def noteEingeben():
#    print("Neue Eingabe: " + str(eingabeFeld.get()) + " Neues Datum " + str(datumNeu.get()))



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







fenster.mainloop()

# Die Daten auf der Datenbank sichern
conn.commit()
# Verbindung zur Datenbank schliessen.
conn.close()