import random


def GenList(lower, upper):
    arr = []
    for i in range(lower, upper + 1):
        arr.append(i)
    return arr


# Has duplicates
def RealisticListGen(lower, upper, amount):
    arr = []
    for i in range(1, amount + 1):
        n = random.randint(lower, upper)
        arr.append(n)
    return arr
