def tel_elementen(lijst, min, max):
    aantal = 0
    for element in lijst:
        if min <= element <= max:
            aantal += 1
    return aantal


lijst1 = [10, 20, 30, 40, 40, 40, 70, 80, 99]
lijst2 = ['a', 'b', 'c', 'd', 'e', 'f']

print(
    f"Het aantal elementen tussen 40 en 100 bedraagt: {tel_elementen(lijst1, 40, 100)}")
print(
    f"het aantal elementes tussen a en e bedraagt: {tel_elementen(lijst2, 'a', 'e')}")
