import os
import sys
file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

import matplotlib.pyplot as plt
import time
import numpy as np
import random
from MergeSort import MergeSort
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

#thisx = []
#for n in range(1, 101):
#    for p in range(1, 101):
#        thisx.append(n)
#    plt.scatter(thisx, y_vals[n-1], label="average results", color="green", marker="*", s=30)
#    thisx.clear()'''

plt.scatter(x_vals, y_vals, label="average results", color="green", marker="*", s=30)
# x-axis label
plt.xlabel('number of elements')
# frequency label
plt.ylabel('time in seconds')
# plot title
plt.title('Time of merge sort in seconds per number of elements!')
# function to show the plot
plt.show()