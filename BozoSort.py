import random
import os
import sys

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)
from List_Generators import *


data = RealisticListGen(1, 100, 10)
random.shuffle(data)



def BozoSort(arr):
    swaps = 0
    while not all(arr[i] <= arr[i + 1] for i in range(0, len(arr) - 1)):
        a = random.randint(0, len(arr) - 1)
        b = random.randint(0, len(arr) - 1)
        while a == b:
            b = random.randint(0, len(arr) - 1)
        swaps += 1
        arr[a], arr[b] = arr[b], arr[a]
    return [arr, swaps]


if __name__ == "__main__":
    print(f'{data}\n\n\n')
    outcome = BozoSort(data)
    print(outcome[0])
    print(f'There were {outcome[1]} swaps')