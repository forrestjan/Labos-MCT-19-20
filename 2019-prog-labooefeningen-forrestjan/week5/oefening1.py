klassen_mct = ("1mct", "2mct", "3mct")
klassen_devine = ("1devine", "2devine", "3devine")
elementen = ("test", True, 3.2, 1)

# klassen_mct[2] = '4mct' #typeerror: tuple object does not support assignment
# klassen_mct.append("3mit") #NameError: name 'elementen' is not defined

t4 = klassen_mct + klassen_devine
print(list(t4))

print(klassen_devine * 3)
