import random
import os
import sys
import time

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)
from List_Generators import *
from MergeSort import MergeSort

data = RealisticListGen(1, 1000, 1000)
random.shuffle(data)
n = random.randint(1, 1000)


def BinarySearching(arr, item, start, end, comparisons):
    # If array is not sorted sort it.
    if not all(arr[i] <= arr[i+1] for i in range(0, len(arr)- 1)):
        MergeSort(arr)
        print(f'Sorted Array: {arr}')

    timer_start = time.perf_counter()
    mid = (start + end) // 2
    comparisons += 1
    if start < end:
        if item == arr[mid]:
            timer_end = time.perf_counter()
            return [mid, comparisons, timer_end-timer_start]
        elif item < arr[mid]:
            return BinarySearching(arr, item, start, mid-1, comparisons)
        elif item > arr[mid]:
            return BinarySearching(arr, item, mid+1, end, comparisons)
    else:
        timer_end = time.perf_counter()
        return [-1, comparisons, timer_end-timer_start]


if __name__ == "__main__":
    print(f'{data}\n\n\n')
    start = time.perf_counter()
    result = BinarySearching(data, n, 0, len(data), 0)
    end = time.perf_counter()
    if result[0] == -1:
        print(f'{n} not in list. With {result[1]} comparisons\nElapsed time: {end-start} seconds without sorting the timer would be {result[2]}')
    else:
        print(f'{n} was found first at position {result[0]}. With {result[1]} comparisons\nElapsed time: {end-start} seconds without sorting the timer would be {result[2]}')
