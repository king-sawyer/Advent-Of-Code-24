import pandas as pd
import numpy as np

"""
Puzzle Description:
Pair up the numbers and measure how far apart they are. Pair up the smallest number in the left list with the smallest number in the right list, then the second-smallest left number with the second-smallest right number, and so on  Within each pair, figure out how far apart the two numbers are and add up all of those distances.
"""

def puzzle1Part1():
    "Utilizing pandas to read the data file"
    data = pd.read_csv('data.txt', sep="   ", engine='python', header=None)

    "Utilizing numpy to convert the data file to an array"
    list1 = data[0].to_numpy()
    list2 = data[1].to_numpy()

    "Sorting both lists utilizing numpy.sort()"
    sortedList1 = np.sort(list1)
    sortedList2 = np.sort(list2)

    distance = 0

    "Iterating over the first list and adding the absolute value(total distance) to distance which is then returned"
    for i in range(len(sortedList1)):
        distance += abs(sortedList1[i] - sortedList2[i])
    
    return distance

print(puzzle1Part1())