# importeer de correcte dataklasse
from model.Bier import Bier


def test1():
    try:
        bier = Bier("NMCT-Blond", "Howest", "25.0", "blond")
        print(bier)
    except Exception as ex:
        print(f"foutje {ex}")




test1()


def test2():
    pass


# test2()
