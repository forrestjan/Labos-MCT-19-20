from model.Boek import Boek

# mijn_boek = Boek()
# mijn_boek.titel = "python ADV"
# mijn_boek.auteur = "Johan V"
# mijn_boek.jaargang = 2019
# mijn_boek.uitgeverij = "Howest"
# mijn_boek.isbn = "1234-4321-1234-4321"
# print(mijn_boek)

b1 = Boek("Python for dummies", "Louis Kegels", "Arco", "125-875-5455")
print(f"Titel van boek 1: {b1.titel}")
b1.titel = "Python for dummies bis"
print("Volledige info boek 1")
print(b1)

b2 = Boek("Hoe leg ik een vijver in mijn tuin aan? Deel 1",
          "Johan Vannieuwenhuyse", "Aveve", "987-875-5455", 2016)
print("Volledige info boek 2")
print(b2)
