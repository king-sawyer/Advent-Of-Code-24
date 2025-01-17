import pandas as pd
import numpy as np
from collections import Counter

def puzzle1Part2():

    data = pd.read_csv('data.txt', sep="   ", engine='python', header=None)

    list1 = data[0].to_numpy()
    list2 = data[1].to_numpy()

    sortedList1 = np.sort(list1)
    sortedList2 = np.sort(list2)

    similarity = 0

    occurrances = Counter(sortedList2)

    for i in range(len(sortedList1)):
        similarity += ((occurrances[sortedList1[i]]) * sortedList1[i] )


    return similarity

print(puzzle1Part2())