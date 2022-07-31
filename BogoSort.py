import random
import time
import os
import sys

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)
from List_Generators import *


data = GenList(1, 10, )
random.shuffle(data)


def BogoSort(arr):
    shuffles = 0
    while not all(arr[i] <= arr[i + 1] for i in range(0, len(arr) - 1)):
        shuffles += 1
        random.shuffle(arr)
    return [arr, shuffles]


if __name__ == "__main__":
    print(f'{data}\n\n\n')
    
    start = time.perf_counter()
    outcome = BogoSort(data)
    end = time.perf_counter()

    print(outcome[0])
    print(f'There were {outcome[1]} shuffles. It took {end - start} seconds')
