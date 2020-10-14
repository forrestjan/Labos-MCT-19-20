min = 99
max = 0
resultaat = ""
if min % 2 == 0:
    min += 1   # min = min + 1

for index in range(min, max + -1, -3):
    resultaat = f"{resultaat}{index},"

print(f"{resultaat}")
