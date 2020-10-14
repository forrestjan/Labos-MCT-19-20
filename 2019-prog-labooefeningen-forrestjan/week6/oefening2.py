import os


def lees_bestand_in(bestandsnaam):
    fo = open(bestandsnaam)
    line = fo.readline()
    regelnr = 1
    while line != "":
        line = line.rstrip()
        print(f"regel {regelnr}: {line}")
        regelnr += 1
        line = fo.readline()
    fo.close()


def schrijf_input_naar_bestand(bestandsnaam):
    fo = open(bestandsnaam, "w")
    lijn = input("Geef een regel of druk op enter om te stoppen >")
    while lijn != "":
        fo.write(f"{lijn}\n")
        lijn = input("geef een zin op>")


if os.path.exists("DRB/temp.txt"):
    lees_bestand_in("DRB/temp.txt")
else:
    schrijf_input_naar_bestand("DRB/temp.txt")
