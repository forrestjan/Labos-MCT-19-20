def gen_pwd(naam, voornaam, geb_dat):
    subnaam = naam.lower().replace(" ", "")[0:3]
    subvoornaam = voornaam.upper().replace(" ", "")[0:2]
    subgeb_dat = f"{geb_dat[3:5]}{geb_dat[8:10]}"
    return f"{subnaam}{subvoornaam}{subgeb_dat}"


naam = input("geef uw achternaam op > ")
voornaam = input("geef uw voornaam op > ")
geb_dat = input("geef uw geboortedatum(dd-mm-yyyy) > ")
print(f"{gen_pwd(naam, voornaam, geb_dat)}")
