EF Informatik 2015-2017
=======================

Zur Terminologie
----------------

Falls du dieses Dokument liest und die Terminologie (Repo, Versionskontrolle,
Branch, Head, push, pull, commit, merge, Merge-Konflikt usw) noch nicht
verstehst: Keine Sorge! Wir werden diese Begriffe nach und nach einf�hren und besprechen.

Zu diesem Repository
--------------------

Dieses Repository enth�lt Quellcode und andere Dateien, die wir w�hrend
der zwei Jahre Informatikunterricht verwenden.

Wir benutzen das Repo als Verteilungs- und Austauschplatform f�r diese
Dateien. Das funktioniert so:

   1. Im master-Branch werden jeweils neue Dateien oder Korrekturen von bereits
      bestehenden Dateien bereitgestellt. Die Lehrperson ist die einzige, die
      commits in diesem Branch macht.

   2. Jeder Sch�ler bzw jede Sch�lerin klont das Repository (z.B. in der Schule auf
      die pers�nliche Dateiablage, zuhause auf dem Computer) und erstellt als erstes
      einen eigenen Branch.

   3. Wenn du deine Arbeit von einem deiner lokalen Repos ins Github-Repo pushst,
      dann immer nur in deinen eigenen Branch, *nie* in den master-Branch!

   4. Wer in den Master-branch pusht, bringt am n�chsten Freitag einen Kuchen mit!

Am einfachsten ist es also, gleich einen lokalen branch mit deinem Namen zu erstellen
und dann ausschliesslich in diesem branch zu arbeiten, nicht im master-branch.


Neuerungen im Master-Branch in den eigenen Branch einfliessen lassen
--------------------------------------------------------------------

Wenn es im master-branch im Github-Repo �nderungen oder neue Dateien gibt, dann
gehst du folgendermassen vor:

   1. Pull vom master-Branch im Github-Repo in deinen lokalen master-Branch
   2. Merge vom master-Branch in deinen eigenen Branch.


Im Normalfall sollte es keine Merge-Konflikte geben, weil �nderungen im master-Branch
vor allem neu hinzugef�gte Dateien sind.
