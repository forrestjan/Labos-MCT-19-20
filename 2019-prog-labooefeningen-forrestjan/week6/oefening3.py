def vul_bestand_aan(bestandsnaam):
    fo = open(bestandsnaam, "a")
    lijn = input("Geef een regel of druk op Enter om te stoppen >")
    while lijn != "":
        fo.write(f"{lijn}\n")
        lijn = input("Geef een regel of druk op Enter om te stoppen >")

    fo.close()

# if os.path.exists("Week06/temp.txt"):
#     lees_bestand_in("Week06/temp.txt")

# else:
#     schrijf_input_naar_bestand("Week06/temp.txt")


vul_bestand_aan("week06/DRB/temp.txt")
