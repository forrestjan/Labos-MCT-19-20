min = 200
max = 308
resultaat = ""


for index in range(min, max + -1):
    if index % 7 == 0 and index % 5 != 0:
        resultaat = f"{resultaat}{index}\n"

print(f"{resultaat}")
