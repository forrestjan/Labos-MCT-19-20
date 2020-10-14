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


lees_bestand_in("DRB/tekst.txt")
