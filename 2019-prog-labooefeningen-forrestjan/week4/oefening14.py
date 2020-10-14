def geef_gemeenschapelijke_elementen(lijst1, lijst2):
    zelfde_waarde = []
    for element in lijst1:
        if element in lijst2 and element not in zelfde_waarde:
            zelfde_waarde.append(element)
    zelfde_waarde.sort()
    return zelfde_waarde


lijst1 = [78, 4, 5, 6, 4]
lijst2 = [89, 78, 4]

print(
    f"de gemeenschapelijke elementen zijn: {geef_gemeenschapelijke_elementen(lijst1, lijst2)}")

lijst3 = ['tamara', 'delfien', 'elke', 'martijn']
lijst4 = ['natasja', 'mieke', 'tamara', 'elke', 'carine']

print(
    f"de gemeenschapelijke elementen zijn: {geef_gemeenschapelijke_elementen(lijst3, lijst4)}")
