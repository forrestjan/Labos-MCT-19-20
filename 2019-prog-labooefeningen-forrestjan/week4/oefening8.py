import random

maanden = ["januarie", "februarie", "maart", "april", "mei", "juni",
           "julie", "augustus", "september", "october", "november", "december"]
getallen = [100, 200, 300, 5, 9, 24, 69, 420, 21]


def kies_element(lijst):
    return random.choice(lijst)


print(f"De gekozen maand is {kies_element(maanden)}")
print(f"Het gekoazen getall is {kies_element(getallen)}")
