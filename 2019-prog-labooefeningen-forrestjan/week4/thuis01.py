def zijn_gelijk(lista, listb):
    for element in lista:
        if element in listb:
            return True
        else:
            return False


lista = [10, 14, 2, 3, -10]

# listb = [-10, 3, 2, 10, 14]
listb = [0, 8, 7, 11, 17]

if zijn_gelijk(lista, listb):
    print("gelijk = true")
else:
    print("gelijk = false")
