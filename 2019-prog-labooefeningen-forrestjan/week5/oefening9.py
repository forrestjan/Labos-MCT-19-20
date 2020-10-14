import random


def registreer_snelheidsmeting(dict):
    for key in dict.keys():
        dict[key] = random.randrange(10, 70)


def print_snelheden_pp(personen_straat):
    print("Gerigistreerde snelheden in de straat graaf karel de goedelaan zijn :")
    for key, value in personen_straat.items():
        print(f"{key}\t\t\t{value}")


def filter_overtreding(dict, max_snelheid):
    overtredingen = {}
    for key, value in dict.items():
        if value > max_snelheid:
            overtredingen[key] = value
    return overtredingen


def print_boetes(dict, max_snelheid):
    print("De te innen boetes zijn:")
    for key, value in dict.items():
        print(f"{key} reed {value - max_snelheid} Km/U te snel en krijgt een boete van {(value - max_snelheid) * 10}EUR")


personen_straat = {"Stijn": 0, "Dieter": 0, "Christophe": 0, "johan": 0}


registreer_snelheidsmeting(personen_straat)
print_snelheden_pp(personen_straat)

max_snelheid = int(input("Geef de maximaale toegelaten snelheid op"))

overtred = filter_overtreding(personen_straat, max_snelheid)

print(overtred)
print(print_boetes(overtred, max_snelheid))
