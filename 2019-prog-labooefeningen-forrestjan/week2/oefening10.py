def berekening(a,b, c=0, d=0):
    return a - b + c - d
#het resultaat van 12, 4, 8, 10
print(f"het resultaat is: {berekening(12, 4, 8, 10)}")

print(f"het resultaat is: {berekening(d=10, c=8, b=4, a=12,)}")

print(f"het resultaat is: {berekening(b=4, a=12)}")
