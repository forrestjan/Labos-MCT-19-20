min = 10
max = 129
resultaat = ""
if min % 2 == 0:
    min += 1   # min = min + 1

for index in range(min, max + 1, 2):
    resultaat = f"{resultaat}{index},"

print(f"{resultaat}")
