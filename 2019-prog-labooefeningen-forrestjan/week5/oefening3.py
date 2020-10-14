mct = {"1MCT": 1, "2MCT": 2, "3MCT": 2}
devine = {"Devine1": 12, "Devine2": 23, "Devine3": 33}

mct["1MIT"] = "66"

print(mct)

print(mct["1MCT"])
# of"
print(mct.get("1MCT", "no can do"))

if "1MIT" not in mct:
    mct["1MIT"] = "966"

if "4MCT" in mct:
    del(mct["4MCT"])

print(mct)
