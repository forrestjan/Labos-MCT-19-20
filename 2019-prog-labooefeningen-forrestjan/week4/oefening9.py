import random

maanden = ["januarie", "februarie", "maart", "april", "mei", "juni",
           "julie", "augustus", "september", "october", "november", "december"]
getallen = [100, 200, 300, 5, 9, 24, 69, 420, 21]


def max_min_uit_lijst(lijst):
    return f"max:{max(lijst)} en min:{min(lijst)}"


print(f"De gekozen maand is {max_min_uit_lijst(maanden)}")
print(f"Het gekoazen getall is {max_min_uit_lijst(getallen)}")
