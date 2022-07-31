import time
import os
import sys
import random

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)
from List_Generators import *


data = RealisticListGen(1, 1000, 1000)
random.shuffle(data)


def BubbleSort(elements):
    """Uses bubble sort to sort array counts swaps and cycles"""
    comparisons = total_swaps = cycles = 0
    while True:
        swaps = 0
        for i in range(len(elements) - 1):
            if elements[i] > elements[i + 1]:
                comparisons += 1
                elements[i], elements[i + 1] = elements[i + 1], elements[i]
                swaps += 1
                total_swaps += 1
            else:
                comparisons += 1
        cycles += 1
        if swaps == 0:
            return [elements, comparisons, total_swaps, cycles]


if __name__ == "__main__":
    print(f'{data}\n\n\n')
    start = time.perf_counter()
    outcome = BubbleSort(data)
    end = time.perf_counter()
    print(outcome[0])
    print(f'There was {outcome[1]} comparisons, {outcome[2]} swaps, in {outcome[3]} cycles \n It took {end-start} seconds')
