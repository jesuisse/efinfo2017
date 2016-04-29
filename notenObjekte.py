#Klassen fuer die Verwaltung der Noten

#Klasse enthaelt die Noten pro Fach
#  Attribute:
#     fach: Name des Fachs (string)
#     notenliste: Eine Liste der erreichten Noten (liste)
#     durchschnitt: Die Durchschnittsnote des Fachs
class FachNoten(object):
    def __init__(self, fach, notenliste):
        self.fach = fach
        self.notenliste = notenliste
        if len(notenliste) > 0:
            self.durchschnitt = round(sum(notenliste) / len(notenliste),1)

#Klasse enthaelt die Definition des Fachs
#  Attribute:
#     fach: Name des Fachs (string)
#     zielnote: Die angestrebte Durchschnittsnote fuer dieses Fach (flaot)
#     minimalnote: Die Minimalnote um das Fach zu bestehen (float)
#  Methoden
#     mindestNote: Berechnet die kleinste Note, die Ausreicht um die Zielnote zu erreichen
#                  aufgrund der Anzahl Noten und des Notendurchschnitts
class FachDefn(object):
    def __init__(self, fach, zielnote, minimalnote):
        self.fach = fach
        self.zielnote = zielnote
        self.minimalnote = minimalnote

    def mindestNote(self, anzNoten, durchschnitt):
        return round(self.zielnote * (1 + anzNoten) - durchschnitt * anzNoten, 1)