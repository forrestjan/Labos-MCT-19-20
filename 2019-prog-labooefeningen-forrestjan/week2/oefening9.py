def maak_verwelkoming_klas(naam, klasgroep = "1MIT1"):
    return f"welkom {naam} in {klasgroep}"
naam = input("wat is uw naam? >")
groep = input("wat is uw groep? >")

resultaat = maak_verwelkoming_klas(naam, groep)
print(resultaat)

tweede_resultaat = maak_verwelkoming_klas(naam)
print(tweede_resultaat)