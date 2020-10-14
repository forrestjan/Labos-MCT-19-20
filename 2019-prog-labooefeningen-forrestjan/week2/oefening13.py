def geef_celsius(t_in_fahrenheit):
    return (t_in_fahrenheit - 32) * 5 / 9


def geef_fahrenheit(t_in_celcius):
    return (t_in_celcius * 9 / 5) + 32


eenheid = input(f"geef uw eenheid op < [C:celcius, F:Fahrenheit] >")
if str.upper(eenheid) == "C":
    temp = float(input("geef een temperatuur in celcius in > "))
    new_temp = geef_fahrenheit(temp)
    print(f"de temperatuur in farhenheit bedraagt {new_temp:.2f}")
elif str.upper(eenheid) == "F":
    temp = float(input("geef een temperatuur in fahrenheit in > "))
    new_temp = geef_celsius(temp)
    print(f"de temperatuur in celcius bedraagt {new_temp:.2f}")
else:
    print("deze keuze is onbekend")