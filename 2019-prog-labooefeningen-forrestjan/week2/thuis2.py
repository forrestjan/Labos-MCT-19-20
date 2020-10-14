def exclusief_naar_inclusief(excl_btw, btw_percentage):
    return (excl_btw * btw_percentage)

excl_btw = float(input("Hoeveel bedraagt het bedrag exclusief btw?"))

btw_percentage = float(input("Wat is het btw percentage?"))

incl_btw = exclusief_naar_inclusief(excl_btw, btw_percentage)

print(f"Het inclusief bedrag dat je moet betalen is: {incl_btw}")
