import random
import os
import sys

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)
from List_Generators import *


data = RealisticListGen(1, 100, 40)
random.shuffle(data)


def SelectionSort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i + 1, len(arr)):
            if arr[min] > arr[j]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr


if __name__ == "__main__":
    print(f'{data}\n\n\n')

    print(SelectionSort(data))