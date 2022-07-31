import random
import os
import sys

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)
from List_Generators import *

data = RealisticListGen(1, 100, 10)
random.shuffle(data)
print(f'{data}\n\n\n')


def ShellSort(arr):
    pass
