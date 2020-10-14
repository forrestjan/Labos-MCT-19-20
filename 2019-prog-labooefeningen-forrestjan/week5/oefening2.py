def print_tuple(soort, lijst):
    print(f"verzameling: {soort} ")
    for item in lijst:
        print(f"{item} staat op positie {lijst.index(item)}")


klassen_mct = ("1mct", "2mct", "3mct")
klassen_devine = ("1devine", "2devine", "3devine")

print_tuple("MCT", klassen_mct)
print_tuple("devine", klassen_devine)
