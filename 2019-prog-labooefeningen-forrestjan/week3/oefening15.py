def analyseer_email(mail):
    vnd_aap = mail.find("@")
    vnd_pnt = str.find(mail, ".")

    voornaam = mail[0:vnd_pnt].replace(".", " ")
    naam = mail[vnd_pnt+1:vnd_aap]

#   voornaam = f"{voornaam[0].upper()}{voornaam[1:]}"
#   naam = f"{naam[0].upper}{naam[1:]}"

    return f"{voornaam.capitalize()} {naam.capitalize()}"
#    naam = [.:@]


mail = input("geef uw howest mail >")
print(analyseer_email(mail))
