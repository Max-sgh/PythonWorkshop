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
        print("-"*20 + "Rechnung für Tisch #" + str(self.tischnr) + "-"*20)
        länge = len("-"*20 + "Rechnung für Tisch #" +
                    str(self.tischnr) + "-"*20)
        summe = 0
        for e in self.essen:
            name = e[0]
            länge_name = len(name)
            preis = e[1]
            anzahl = e[2]
            länge_anzal = len(str(anzahl))
            print(name + " "*(30-länge_name) + " x" + str(anzahl) + " " *
                  (5-länge_anzal) + "%.2f" % round(preis, 2) + "€" + " "*10 + "%.2f" % round(anzahl*preis, 2))
            summe += anzahl*preis
        print("-"*länge)
        print(" "*40 + "Summe:      %.2f" % round(summe, 2))


if __name__ == "__main__":
    tische = []
    # Tische erzeugen
    t1 = Tisch(1)
    t2 = Tisch(2)
    tische.append(t1)
    tische.append(t2)

    essen = {"steak": 5.95, "pommes": 3.95, "apfel": 2}

    while True:
        # Aktuelle Eingabe über den input Befehl holen
        befehl = input("Eingabe: ")
        try:
            # Eingabe in Befehl und Argumente spalten; Trennung erfolgt hier über ein Leerzeichen
            befehl = befehl.split(" ")
        except:
            # Fehler ausgeben und auf nächste Eingabe warten
            print(
                "Fehler in der Eingabe! Bitte Befehl und Argumente mit Leerzeichen trennen")
            continue

        try:
            aktion = befehl[0].lower()
        except:
            print("Bitte geben Sie einen auzuführenden Befehl an!")
            continue

        try:
            tischnr = int(befehl[1])
        except:
            print("Bitte geben Sie eine Tischnummer an!")
            continue

        tisch = None
        for t in tische:
            if t.tischnr == tischnr:
                tisch = t

        if tisch == None:
            print("Fehler! Tisch #" + str(tischnr) +
                  "konnte nicht gefunden werden!")
            continue

        if aktion == "bestellen" or aktion == "b":
            # bestelltes Essen dem Tisch hinzufügen
            print("Buche " + befehl[2].lower() + " auf Tisch #" + str(tischnr))
            try:
                preis = essen[befehl[2].lower()]
            except:
                print("Essen konnte nicht gefunden werden!")
                continue
            pass

        elif aktion == "rechnung" or aktion == "r":
            # Rechnung für den Tisch ausgeben
            pass

        elif aktion == "löschen" or aktion == "l":
            # Tisch zurücksetzen
            print("Setze Bestellungen auf Tisch #" +
                  str(tischnr) + " zurück...")
            pass

        else:
            print("Bitte geben Sie einen validen Befehl an!")
