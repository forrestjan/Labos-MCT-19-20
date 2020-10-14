import random


def inlezen_spelers(bestandsnaam):
    fo = open(bestandsnaam, "r")
    lijst_spelers = []
    for speler in fo.readlines():
        lijst_spelers.append(speler.rstrip("\n"))
    fo.close()
    return lijst_spelers


def afprinten_spelers(naam_lijst, lijst_spelers):
    print(naam_lijst)
    for speler in lijst_spelers:
        print(speler)


def selecteer_random_spelers(lijst_spelers):
    opstelling = []
    while len(opstelling) != 11:
        gekozen_speler = random.choice(lijst_spelers)
        if gekozen_speler not in opstelling:
            opstelling.append(gekozen_speler)
    return opstelling


def opslaan_spelers(bestandsnaam, lijst_spelers):
    pass


anderslecht = inlezen_spelers("DRB/Spelers.txt")


lijst_geselecteerde_spelers = selecteer_random_spelers(anderslecht)
