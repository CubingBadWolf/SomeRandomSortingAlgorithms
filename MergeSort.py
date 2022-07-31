import random
import time
from List_Generators import *

data = RealisticListGen(1, 1000, 1000)
random.shuffle(data)


def MergeSort(arr):
    if len(arr) > 1: # If len(arr) = 1 then it contains itself and is sorted by definition and can be merged
        mid = len(arr)//2 # Integer division
        # Split arr into left and right array's
        left = arr[:mid]
        right = arr[mid:]

        # Calls itself recursively
        MergeSort(left)
        MergeSort(right)

        i = j = k = 0 # i = index left arr, j = index right arr, k = merged arr index

        # If there are items in both lists check if the item in left is smaller than the one in right. 
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                # Adds number in left into the merged arr
                arr[k] = left[i]
                i += 1
            else:
                # Adds the number in right into the merged arr
                arr[k] = right[j]
                j += 1
            k += 1
        
        # If there is only items left in the left arr 
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        
        # If there is only items in the left arr
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
        # Arr is sorted
        return arr
    else:
        return arr


if __name__ == "__main__":
    print(f'{data}\n\n\n')
    start = time.perf_counter()
    result = MergeSort(data)
    end = time.perf_counter()
    print(f'{result}\n Elapsed Time: {end-start} seconds')