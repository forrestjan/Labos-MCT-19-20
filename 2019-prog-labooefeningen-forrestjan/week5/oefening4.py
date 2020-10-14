def print_dict(soort, elementen):
    print(f"verzameling: {soort} ")
    for key, value in elementen.items():
        print(f"key: {key} --> value: {value}")


klassen_mct = {"1mct": 101, "2mct": 88, "3mct": 77}
klassen_devine = {"1devine": 123, "2devine": 98, "3devine": 55}

print_dict("MCT", klassen_mct)
print_dict("devine", klassen_devine)
