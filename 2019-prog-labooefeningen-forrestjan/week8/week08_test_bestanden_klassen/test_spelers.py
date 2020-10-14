from model.Speler import Speler
from model.Geboortedatum import Geboortedatum


def test_oef1():
    # aanspreken van een public static variabele (attribute)
    Speler.naam_ploeg = "Rode duivels"

    sp1 = Speler("Thibault", "Cortous", "keeper", 8, 0)
    sp2 = Speler("Vincent", "Kompany", "aanvaller", 8, 3)
    # par 4 en 5 worden niet opgegeven, zie default par in classe __init__()
    sp3 = Speler("Axel", "Witsel", "aanvaller")

    print(sp1)
    print(sp2)
    print(sp3)

    print("\nVincent scoort!")
    sp2.maak_doelpunt()
    print(sp2)

    print("\nAxel scoort!")
    sp3.maak_doelpunt()
    print(sp3)

    print(
        f"Het doelpunten saldo van { Speler.naam_ploeg } is { Speler.get_doelpunten_saldo_ploeg()}")


# test_oef1()


def test_spelers_oef3():
    sp1 = Speler("Thibault", "Cortous", "keeper",
                 8, 0, Geboortedatum(11, 5, 1992))
    sp2 = Speler("Vincent", "Kompany", "aanvaller",
                 8, 3, Geboortedatum(10, 4, 1986))
    sp3 = Speler("Axel", "Witsel", "aanvaller")

    print("\nDe geboortedata van de spelers zijn:")
    for speler in [sp1, sp2, sp3]:
        print(f"{speler} -> gebootedatum: {speler.geboortedatum}")


test_spelers_oef3()
