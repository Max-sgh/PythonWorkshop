class Tisch(object):
    def __init__(self, tischnr):
        # Liste zum Speichern des bestellten Essens: [name, preis, anzahl]
        self.essen = []
        self.tischnr = tischnr

    def essen_hinzufügen(self, name, preis):
        # Alle bestellen Essen durchsuchen, um bei einem Treffer lediglich die Anzahl
        # zu erhöhen

        # Keine vorhandene Bestellung gefunden
        # -> neues Essen dem Tisch hinzufügen
        self.essen.append([name, preis, 1])

    def zurücksetzen(self):
        # alle bestellten Essen durch überschreiben der Liste, mit einer leeren
        # Liste, löschen
        pass

    def rechnung_ausgeben(self):
        # Rechnung ausgeben
        #  - über alle Essenselemente (self.essen) iterieren und
        #    Preis (self.essen[2]) aufsummieren
        #  - einzelne Positionen je Zeile ausgeben
        #  - Summe ausgeben
        pass


if __name__ == "__main__":
    tische = []
    # Tische erzeugen

    essen = {"steak": 5.95, "pommes": 3.95, "apfel": 2}

    while True:
        # Aktuelle Eingabe über den input Befehl holen
        befehl = input("Eingabe: ")
        try:
            # Eingabe in Befehl und Argumente spalten; Trennung erfolgt hier über ein Leerzeichen
            pass
        except:
            # Fehler ausgeben und auf nächste Eingabe warten
            print(
                "Fehler in der Eingabe! Bitte Befehl und Argumente mit Leerzeichen trennen")
            continue

        try:
            # Variable aktion definieren und befehl darin speichern
            # (0tes Element des befehls)
            pass
        except:
            print("Bitte geben Sie einen auzuführenden Befehl an!")
            continue

        try:
            # Variable tischnr definieren und nummer darin speichern
            # (1tes Element des befehls)
            pass
        except:
            print("Bitte geben Sie eine Tischnummer an!")
            continue

        tisch = None
        # Iteration über alle Tische und nach Tischnummer vergleichen
        # Wenn der Tisch gefunden wurde, in Variable tisch speichern

        if tisch == None:
            print("Fehler! Tisch #" + str(tischnr) +
                  "konnte nicht gefunden werden!")
            continue

        #
        # aktion prüfen auf "bestelle", "rechnung" und "löschen"
        # jeweilige Methode des Tisches aufrufen
        # Wenn nichts verfügbar ist, Fehlermeldung ausgeben.
        #
