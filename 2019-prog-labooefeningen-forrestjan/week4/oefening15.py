def verwijder_dubbels(lijst):
    nieuwe_lijst = []
    for element in lijst:
        if element not in nieuwe_lijst:
            nieuwe_lijst.append(element)
    return nieuwe_lijst

    #geen_dubbel_elem = []
    # for element in lijst1:
    #    if element not in geen_dubbel_elem:
    #        geen_dubbel_elem.append(element)
#
    # geen_dubbel_elem.sort()
    # return geen_dubbel_elem


lijst1 = ['A', 89, 78, 4, 'A', 'test', 4]

print(f"de lijst zonder dubbels is :{verwijder_dubbels(lijst1)}")
