#     if getallen1 == getallen2:
#         print("er is een getal gelijk in beide lijsten")
#     else:
#         print("er is geen gelijk getal in beide lijsten")
#
#
# getallen1 = [1, 5, 8, 5]
# getallen2 = [2, 3, 5, 6]


def zijn_totaal_verschillend(lijst1, lijst2,):
    for element in lijst1:
        if element in lijst2:
            return False
    return True


getallen1 = [1, 5, 8, 5]
getallen2 = [2, 3, 5, 6]

if zijn_totaal_verschillend(getallen1, getallen2):
    print("lijsten bevaten geen identiek item")
else:
    print("lijsten bevaten identieke items")
