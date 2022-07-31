import random
import os
import sys


file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)
from List_Generators import *


data = GenList(1, 10,)
random.shuffle(data)

n = random.randint(1, 10)


def BogoSearching(arr, item):
    i = random.randint(0, len(arr) -1)
    while arr[i] != item:
        i = random.randint(0, len(arr) - 1)
    return i

if __name__ == "__main__":
    result = BogoSearching(data, n)
    print(f'{n} is found at index {result}')