import pandas as pd
import numpy as np

def puzzle1Part1():
    data = pd.read_csv('data.txt', sep="   ", engine='python', header=None)

    list1 = data[0].to_numpy()
    list2 = data[1].to_numpy()

    sortedList1 = np.sort(list1)
    sortedList2 = np.sort(list2)

    distance = 0

    for i in range(len(sortedList1)):
        distance += abs(sortedList1[i] - sortedList2[i])
    
    return distance

print(puzzle1Part1())