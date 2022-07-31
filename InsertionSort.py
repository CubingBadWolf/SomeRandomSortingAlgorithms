import random
import os
import sys

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)
from List_Generators import *


data = RealisticListGen(1, 100, 10)
random.shuffle(data)


def InsertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            
        # Place key at after the element just smaller than it.
        arr[j + 1] = key
    return arr


if __name__ == "__main__":
    print(f'{data}\n\n\n')

    print(InsertionSort(data))
