# encoding: utf-8
__author__ = 'pax'


# Definition aller Räume
raum1 = ["Kiesweg", "Du stehst auf einem Kiesweg.", []]
raum2 = ["Haus", "Im Haus ist es unheimlich schummerig. Morsche Balken knarren.", []]
raum3 = ["Kirschgarten", "Dutzende Kirschbäume blühen in diesem Garten, in dem offenbar schon lange niemand mehr war, denn das Gras steht kniehoch.", []]


def macheVerbindung(raumA, richtung, raumB):
    """Erzeugt eine Verbindung von A in Richtung richtung nach B"""
    raumA[2].append((richtung, raumB))

# Verbindungen zwischen Räumen definieren
macheVerbindung(raum1, "n", raum2)
macheVerbindung(raum2, "s", raum1)
macheVerbindung(raum1, "o", raum3)
macheVerbindung(raum3, "w", raum1)


# Funktionen zum abfragen einzelner Eigenschaften eines Raums
def raumName(raum):
    """Liefert den Namen eines Raumes"""
    return raum[0]

def raumBeschreibung(raum):
    """Liefert die Beschreibung eines Raumes"""
    return raum[1]

def raumVerbindungen(raum):
    """Liefert die Verbindungen zu anderen Räumen"""
    return raum[2]

def raumAnzeigen(raum):
    """Zeigt einen Raum auf der Konsole an."""
    print raumName(raum)
    print 30*"-"
    print raumBeschreibung(raum)

    for verbindung in raumVerbindungen(raum):
        print "In Richtung " + verbindung[0] + " liegt " + raumName(verbindung[1])


raumAnzeigen(raum1)
print
raumAnzeigen(raum2)
