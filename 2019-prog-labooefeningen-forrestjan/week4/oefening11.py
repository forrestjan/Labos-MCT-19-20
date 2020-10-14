from statistics import mean


def gemideld_num_list(lijst):
    return mean(lijst)
    # return sum(lijst) / len(lijst)


getallen = [100, 200, 300, 400, 500]
print(f"De som van de getallen is {gemideld_num_list(getallen)}")
