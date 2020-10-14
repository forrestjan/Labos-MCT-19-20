nieuwe_list_getallen = []

for getal in range(1, 483, 13):
    nieuwe_list_getallen.append(getal)
print(f"{nieuwe_list_getallen}")

# draai de lijst om ////nieuwe_list_getallen = nieuwe_list_getallen.omgekeerd()
nieuwe_list_getallen.reverse()
print(f"{nieuwe_list_getallen}")

# verwijder eerste item
nieuwe_list_getallen.remove(482)
print(f"{nieuwe_list_getallen}")
