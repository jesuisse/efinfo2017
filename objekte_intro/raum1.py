# encoding: utf-8
__author__ = 'pax'

class Raum(object):
    """
    Ein Raum hat einen Titel, eine Beschreibung und
    eine (anfangs leere) Liste mit Verbindungen zu
    anderen Räumen.
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
