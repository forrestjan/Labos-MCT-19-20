def print_list(soort, lijst):
    print(f"verzameling: {soort} ")
    for item in lijst:
        print(f"{item} staat op positie {lijst.index(item)}")


lijst = [12, 45, -9, -15]
print_list = ("gehele getallen", lijst)

lijst = ["maandag", "moet", "ik", "s'avonds",
         "ook", "iets", "doen", "voor", "school"]
print(f"DRINGEND TO DO", lijst)
