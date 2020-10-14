def vertaal_maandnummer_naar_str(maandnummer):
    if maandnummer == 1 :
        return "januarie"
    elif maandnummer == 2 :
        return "februarie"
    elif maandnummer == 3 :
        return "maart"
    elif maandnummer == 4 :
        return "april"
    elif maandnummer == 5 :
        return "mei"
    elif maandnummer == 6 :
        return "juni"
    elif maandnummer == 7 :
        return "juli"
    elif maandnummer == 8 :
        return "augustus"
    elif maandnummer == 9 :
        return "september"
    elif maandnummer == 10 :
        return "oktober"
    elif maandnummer == 11 :
        return "november"
    elif maandnummer == 12 :
        return "december"
    else:
        return print("ongeldige maand")

maandnummer = int(input("geef een maandnummer op > "))

print(f"de overeenkomende maand van {maandnummer} is {vertaal_maandnummer_naar_str(maandnummer)}")