def verhoog_waarde_key(score):
    scores[score] += 1


scores = {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0}

print("Geef de verschillende evaluatiecijfers door (5,4,3,2,1,0)")

score = input("Geef een nieuwe score op > ")

while score != "":
    verhoog_waarde_key(score)
    score = input("Geef een nieuwe score op >  ")


for key, value in scores.items():
    print(f"{value} studenten scoorde(n) {key} op 51")
