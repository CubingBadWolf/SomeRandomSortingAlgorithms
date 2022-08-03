import os
import sys
file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

import matplotlib.pyplot as plt
import time
import numpy as np
import random
from MergeSort import MergeSort
from JumpSearching import JumpSearching as JumpSearch
from List_Generators import GenList

x_vals = []
y_vals = []
times = []
for i in range(1, 101):
    x_vals.append(i)
    data = GenList(1, i)
    random.shuffle(data)
    times.clear()
    for n in range(1, 101):
        start = time.perf_counter()
        MergeSort(data)
        end = time.perf_counter()
        times.append(end-start)
    y_vals.append(sum(times)/len(times))

plt.scatter(x_vals, y_vals, label="average results", color="green", marker="*", s=30)

plt.xlabel('number of elements')

plt.ylabel('time in seconds')

plt.title('Time of merge sort in seconds per number of elements!')

plt.show()
SearchX = []
SearchY = []
SearchTime = []


for v in data:
    data = GenList(1, 100)
    SearchX.append(v)
    for w in range(1, 101):
        start = time.perf_counter()
        JumpSearch(data, w)
        end = time.perf_counter()
        SearchTime.append(end-start)
    SearchY.append(sum(SearchTime)/len(SearchTime))


plt.scatter(SearchX, SearchY, label="average results", color="green", marker="*", s=30)

plt.xlabel('Target Element')
plt.ylabel('Time in seconds')
plt.title('Time of Search for each element averaged 100 times in a 100 element array')
plt.show()