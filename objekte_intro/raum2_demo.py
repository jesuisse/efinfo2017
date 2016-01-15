# encoding: utf-8
__author__ = 'pax'

from objekte_intro.raum2 import Raum

# Definition aller Räume
raum1 = Raum("Kiesweg", "Du stehst auf einem Kiesweg.")
raum2 = Raum("Haus", "Im Haus ist es unheimlich schummerig. Morsche Balken knarren.")
raum3 = Raum("Kirschgarten", "Dutzende Kirschbäume blühen in diesem Garten, und das Gras steht kniehoch.")

raum1.verbinde('n', raum2)
raum2.verbinde('s', raum1)
raum1.verbinde('o', raum3)
raum3.verbinde('w', raum1)


raum1.anzeigen()
print
raum2.anzeigen()

