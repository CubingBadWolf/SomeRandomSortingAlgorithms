import random
import time
import os
import sys

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)
from List_Generators import *

data = RealisticListGen(1, 1000, 1000)
random.shuffle(data)

n = random.randint(1, 1000)


def LinearSearch(arr, item):
    comparisons = 0
    for i in range(0, len(arr)):
        comparisons += 1
        if arr[i] == item:
            return [i, comparisons]
    return [-1, comparisons]


if __name__ == "__main__":
    print(f'{data}\n\n\n')
    start = time.perf_counter()
    result = LinearSearch(data, n)
    end = time.perf_counter()
    if result[0] == -1:
        print(f'{n} not in list, it took {result[1]} comparisons\nElapsed time: {end-start} seconds') # I feel the time calculations is wrong.
    else:
        print(f'{n} found first at position {result} it took {result[1]} comparisons\nElapsed time: {end-start} seconds')
