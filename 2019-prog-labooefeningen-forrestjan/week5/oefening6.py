def voeg_nieuw_element_toe(key, value, howest):
    if "1IPO" not in howest:
        howest = {"1IPO": 51}
    if "2IPO" not in howest:
        howest = {"2IPO": 10}


def print_dict(soort, elementen):
    print(f"verzameling: {soort} ")
    for key, value in elementen.items():
        print(f"key: {key} --> value: {value}")


klassen_mct = {"1mct": 101, "2mct": 88, "3mct": 77}
klassen_devine = {"1devine": 123, "2devine": 98, "3devine": 55}
howest = {}
howest.update(klassen_mct)
howest.update(klassen_devine)


print_dict("howest", howest)


# def print_dict(naam_verzameling, elementen):

#def voeg_nieuw_element_toe(key,value,dingske):#
#    if key not in dingske.keys():
#        dict[key] = value
#        print(f{keys} " toegevoegd")
#    else:
#        print(f"{key}bestaat all")
