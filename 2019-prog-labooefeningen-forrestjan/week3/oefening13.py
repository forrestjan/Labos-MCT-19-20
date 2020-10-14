

def swap(a, b):
    new_a = b[0:2] + a[2:3]
    new_b = a[0:2] + b[2:3]
    return f"{new_a} {new_b}"
# haakjes () bij een return waarde zijn niet noodzakelijk


print(f"{swap('abc', 'xyz')}")
