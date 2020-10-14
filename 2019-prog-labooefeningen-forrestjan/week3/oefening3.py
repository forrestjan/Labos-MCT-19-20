min = 3
max = 100
resultaat = ""
if min % 2 != 0:
    min += 1   # min = min + 1

for index in range(min, max + 1, 2):
    resultaat = f"{resultaat}{index}\n"

print(f"{resultaat}")
