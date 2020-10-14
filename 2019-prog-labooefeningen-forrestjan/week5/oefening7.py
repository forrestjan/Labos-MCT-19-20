def tel_voorkomen_woorden(zin):
    woorden = {}

    for woord in zin.lower().split(" "):
        if woord.isalpha():
            if woord not in woorden:
                woorden[woord] = 1
            else:
                woorden[woord] += 1

    return woorden


zinneke = "Ik heb geen zin in de zin van : ik heb geen zin in deze zin ."
print(f"{tel_voorkomen_woorden(zinneke)}")
