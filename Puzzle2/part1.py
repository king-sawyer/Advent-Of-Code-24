"""
Puzzle 2 - Part 1
Add up the total number of rows that satisfy the following two rules:
- A row must be either ascending or descending
- Each number in the row must differ from the following number by at least one and no more than three
"""

def puzzle2Part1():

    "Utilizing readlines vs pandas as the data is stored in rows compared to columns"
    with open('data.txt', 'r') as file:
        data = file.readlines()

    "Converting each row to an array of integers stored in the parrent array: rows"
    rows = [list(map(int, row.split())) for row in data]

    "The number of rows that satisty both rules"
    safeRows = 0

    "Iterate over each row checking the first rule then the second if first rule is satisfied"
    for row in rows:
        ascOrDesc = checkAscendingOrDescending(row)
        if ascOrDesc:
            numDifferByOneTwoOrThree = checkNumDiffer(row)
            if numDifferByOneTwoOrThree:
                safeRows += 1


    print(safeRows)

"Checking the first rule"
def checkAscendingOrDescending(row):
    asc = True
    desc = True
    
    "Check if row is ascending or descending"
    for i in range(len(row) - 1):
        if row[i] < row[i+1]:
            asc = False
        elif row[i] > row[i+1]:
            desc = False

    if asc or desc:
        return True
    else: 
        return False
    
"Checking the second rule"
def checkNumDiffer(row):
    for i in range(len(row) - 1):
        differ = abs(row[i] - row[i+1])
        if differ not in (1, 2, 3):
            return False
    
    return True

puzzle2Part1()