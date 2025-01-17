import pandas as pd
import numpy as np
from collections import Counter

"""
Puzzle Description: 
Calculate a total similarity score by adding up each number in the left list after multiplying it by the number of times that number appears in the right list.
"""

def puzzle1Part2():

    data = pd.read_csv('data.txt', sep="   ", engine='python', header=None)

    list1 = data[0].to_numpy()
    list2 = data[1].to_numpy()

    sortedList1 = np.sort(list1)
    sortedList2 = np.sort(list2)

    similarity = 0

    "To get the total number of occurances for each value in the second array I am utilizing a Counter which is a a dict subclass. It returns a Counter containing each value and the total number of occurances of the value in the array"
    occurrances = Counter(sortedList2)

    "I iterate over each value in the first list then search the occurances Counter by using the first lists current value as the key to Counter to get the total occurances. Then I multiply that by the first lists current value"
    for i in range(len(sortedList1)):
        similarity += ((occurrances[sortedList1[i]]) * sortedList1[i] )


    return similarity

print(puzzle1Part2())