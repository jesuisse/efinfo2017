# encoding: utf-8
__author__ = 'pax'

"""
Aufgabe: Sorge dafür, dass die unit tests in raum3_test.py
         fehlerlos durchlaufen. Du musst dazu nur dieses
         Python-Programm um eine einzige Methode erweitern.
"""

class Raum(object):
    """
    Ein Raum hat einen Titel, eine Beschreibung und
    eine (anfangs leere) Liste mit Verbindungen zu
    anderen Räumen. Er weiss, wie er Verbindungen
    zu anderen Räumen herstellen kann und wie er
    sich darstellen kann.
    """

    def __init__(self, name, beschreibung):
        """
        Konstruiert einen neuen Raum.
        :param name: Der Name des Raums
        :param beschreibung: Die Beschreibung.
        """
        self.name = name
        self.beschreibung = beschreibung
        self.verbindungen = []

    def verbinde(self, richtung, ziel):
        """
        Verbindet diesen Raum mit einem anderen Raum.
        :param richtung: Richtung als String ('n', 'w' etc)
        :param ziel: ein anderes Raum-Objekt
        """
        self.verbindungen.append((richtung, ziel))

    def finde_raum_in_richtung(self, richtung):
        """
        Findet den Raum, zu dem aus diesem Raum in eine
        bestimmte Richtung eine Verbindung existiert.
        :param richtung. Richtung als String ('n', 'w' etc)
        :return: Der Raum, der in dieser Richtung liegt, oder None
        """
        for zielrichtung, zielraum in self.verbindungen:
            if richtung == zielrichtung:
                return zielraum
        return None

    def anzeigen(self):
        """
        Zeigt einen Raum auf der Konsole an.
        """
        print self.name
        print 30*"-"
        print self.beschreibung
        for verbindung in self.verbindungen:
            print "In Richtung " + verbindung[0] + " liegt " + verbindung[1].name

