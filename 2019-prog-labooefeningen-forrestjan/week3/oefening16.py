import random
import string


def rand_pwd(min_lengt, max_lengt):
    paswoord = ""
    pwd_lengt = random.randrange(min_lengt, max_lengt + 1)
    print(pwd_lengt)
    for getal in range(1, pwd_lengt):
        paswoord = paswoord+random.choice(string.ascii_letters)
    return paswoord


min_lengt = int(input("Geef een minimum lengte >"))
max_lengt = int(input("Geef een maximum lengte >"))

rand_pwd(min_lengt, max_lengt)
print(f"{rand_pwd}")
