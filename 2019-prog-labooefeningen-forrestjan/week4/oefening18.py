def print_loon_vn_list(lijst, functie):
    for loon in lijst:
        print(f"{functie}:\t{loon:.2f}")


bruto_arbeider = []
bruto_bediende = []
bruto_kader = []

aantal_werknemer = int(input("hoeveel werknemers wens je in te geven >"))

for werknemer in range(0, aantal_werknemer):
    functie = str.upper(input(
        "Is de werknemer een A:arbeider, B:bediende, K:kadserlid > "))
    bruto = float(input("Hoeveel verdient deze werknemer? > "))

    if functie == 'A':
        bruto_arbeider.append(bruto)
    elif functie == 'B':
        bruto_bediende.append(bruto)
    elif functie == 'K':
        bruto_kader.append(bruto)
    else:
        print("geef een geldige werknemer in, enkel A,B of K")

print("overzicht: ")
print_loon_vn_list(bruto_arbeider, "A")
print_loon_vn_list(bruto_bediende, "B")
print_loon_vn_list(bruto_kader, "K")


print(f"Aantal arbeiders: {len(bruto_arbeider)}")
print(f"Aantal bediende: {len(bruto_bediende)}")
print(f"Aantal kader: {len(bruto_kader)}")

bruto_totaal = bruto_arbeider+bruto_bediende+bruto_kader
print(f"Aantal werknemers:{len(bruto_totaal)}")

print(f"Totaal brutoloon:{sum(bruto_totaal)}")
