import random
import time
import os
import sys

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)
from List_Generators import *
from MergeSort import MergeSort as Merge
from LinearSearching import LinearSearch as Lin

data = RealisticListGen(1, 100, 100)
random.shuffle(data)

n = random.randint(1, 100)


def JumpSearching(arr, item):
    if not all(arr[n] <= arr[n + 1] for n in range(0, len(arr)-1)):
        Merge(arr)
        print(f'Sorted array: {arr}')

    timer_start = time.perf_counter()
    jump = int(len(arr)**0.5) # Sqrt(len(arr)) is the optimal jump sequence

    i = 0
    comparisons = 1
    while jump < item:
        comparisons += 1
        if arr[jump] >= item:
            break
        i = jump
        jump += int(len(arr)**0.5 )

    for i in range(i, len(arr)):
        comparisons += 1
        if arr[i] == item:
            timer_end = time.perf_counter()
            return [i, comparisons, timer_end-timer_start]
    timer_end = time.perf_counter()
    return [-1, timer_end-timer_start]


if __name__ == "__main__":
    start = time.perf_counter()
    result = JumpSearching(data, n)
    end = time.perf_counter()
    if result[0] == -1:
        print(f'{n} not in list\nElapsed Time {end - start} seconds without sorting the timer would be {result[1]}')
    else:
        print(f'{n} first found at index {result[0]} in {result[1]} comparisons \nElapsed Time {end - start} seconds without sorting the timer would be {result[2]}')