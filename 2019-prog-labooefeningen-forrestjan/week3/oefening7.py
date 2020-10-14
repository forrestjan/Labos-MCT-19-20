def print_lijst_parameters(startwaarde, stapgroote, aantal_getallen):
    stopwaarde = startwaarde + stapgrootte * aantal_getallen
    for index in range(startwaarde, stopwaarde, stapgrootte):
        print(f"{index}")


# pass laat de functie paseren zonder hij iets doet
startwaarde = int(input("geef een startwaarde > "))
stapgrootte = int(input("geef een positieve stapgroote > "))
aantal_getallen = int(input("geef het aantal af te printen getallen > "))

print_lijst_parameters(startwaarde, stapgrootte, aantal_getallen)
