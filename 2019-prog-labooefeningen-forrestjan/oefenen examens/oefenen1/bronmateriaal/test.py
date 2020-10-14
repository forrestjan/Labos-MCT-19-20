





def test1():
    locatie = Locatie("Graaf Karel de Goedelaan",
                      "Kortrijk", 50.824713, 3.251357)
    print(locatie)

    controle = Controle(locatie, 2019, 1)
    print(controle)

    snelheidscontrole = Snelheidscontrole(locatie, 2019, 1, 5, 500, 123)
    print(snelheidscontrole)
    print(snelheidscontrole.info())

test1()






def print_snelheidscontroles(list_snelheidscontroles):
    for snelheidscontrole in list_snelheidscontroles:
        print(snelheidscontrole.info())


def test2():
    list_snelheidscontroles = SnelheidscontroleRepository.inlezen_controles()
    print(f"Aantal snelheidscontroles in 2012: {Snelheidscontrole.geef_totaal_aantal_controles()}")
    list_snelheidscontroles.sort()
    print_snelheidscontroles(list_snelheidscontroles)

test2()






def test3():
    list_snelheidscontroles = SnelheidscontroleRepository.inlezen_controles()
    gezochtestraat = "rogge"
    resultaat = SnelheidscontroleRepository.zoek_deel_straat(
        list_snelheidscontroles, gezochtestraat)
    print("Zoekresultaat:")
    print_snelheidscontroles(resultaat)

    filter_resultaat = SnelheidscontroleRepository.filter_overtredingsgraad(
        list_snelheidscontroles, 30, 35)
    print_snelheidscontroles(filter_resultaat)    

test3()





def test4():
    list_snelheidscontroles = SnelheidscontroleRepository.inlezen_controles()

    vraag = "\nKies uit volgende menu-items:\np = print snelheidscontroles, z = zoek straat, g = gevaren straten, v = verlaat programma:>"

    actie = input(vraag)
    while actie != "v":
        if actie == "p":
            print_snelheidscontroles(list_snelheidscontroles)
        elif actie == "z":
            gezochtestraat = input("Geef (een deel van) de straatnaam op:>")
            print("Resultaat van zoekopdracht:")
            resultaat = SnelheidscontroleRepository.zoek_deel_straat(
                list_snelheidscontroles, gezochtestraat)
            print_snelheidscontroles(resultaat)
        elif actie == "g":
            min = float(input("Geef de minimum overtredingsgraad op:>"))

            resultaat = SnelheidscontroleRepository.filter_overtredingsgraad(
                list_snelheidscontroles, min)
            print("Resultaat van filteropdracht:")
            for straat in resultaat:
                print(f"{straat}")

        actie = input(vraag)


test4()
