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
    firstRule = 0

    "Iterate over each row checking the first rule then the second if first rule is satisfied"
    for row in rows:
        firstRule += checkAscendingOrDescending(row)

    print(firstRule)
        



"Checking the first rule"
def checkAscendingOrDescending(row):
    asc = {'number': [],
            'index': [],
            'row': row}
    desc = {'number': [],
            'index': [],
            'row': row}
    
    totalSafeRows = 0
    
    "Check if row is ascending or descending"
    for i in range(len(row) - 1):

        if row[i] <= row[i+1]:
            desc['index'].append(i+1)
            desc['number'].append(row[i+1])
            "check the current number with two numbers ahead"
            if i+2 < len(row) and row[i] <= row[i+2]:
                    desc['index'].append(i+2)
                    desc['number'].append(row[i+2])
        if row[i] >= row[i+1]:
            asc['index'].append(i+1)
            asc['number'].append(row[i+1])
            "check the current number with two numbers ahead"
            if i + 2 < len(row) and row[i] >= row[i+2]:
                    asc["index"].append(i+2)
                    asc['number'].append(row[i+2])


    if len(asc["index"]) < 2:
        #print(f"ASCENDING: {asc}")
        totalSafeRows += checkNumDiffer(asc)
    if len(desc['index']) < 2:
        #print(f"DESCENDING: {desc}")

        totalSafeRows += checkNumDiffer(desc)

    return totalSafeRows
    
    
"Checking the second rule"
def checkNumDiffer(row):
    differErrors = {'number': [],
                    'index': []}
    
    safeRows = 0
    
    
    for i in range(len(row['row']) - 1):
        differ = abs(row['row'][i] - row['row'][i+1])
        if differ not in (1, 2, 3):
            if i+2 < len(row['row']):
                nextDiffer = abs(row['row'][i] - row['row'][i+2])
                if nextDiffer in (1,2,3):
                    differErrors['index'].append(i+1)
                    differErrors['number'].append(row['row'][i+1])
                    i+=2
                else:
                    differErrors['index'].append(i+1)
                    differErrors['number'].append(row['row'][i+1])
                    differErrors['index'].append(i+2)
                    differErrors['number'].append(row['row'][i+2])
            else:
                differErrors['index'].append(i+1)
                differErrors['number'].append(row['row'][i+1])

                    
    if len(differErrors['index']) < 2:
        if len(differErrors['index']) == 1:
            print(f"Row: {row}")
            print(f"numbers that differ from the following not by 1,2,3: {differErrors['number']} index: {differErrors['index']}\n")

    if len(differErrors['index']) == 0 and len(row['index']) == 0:
        safeRows += 1
        print(f"Row is safe: {row['row']}")
    elif len(differErrors['index']) == 1 and len(row['index']) == 1:
        if differErrors['index'] == row['index']:
            # print(f"{differErrors['index']} == {row['index']}")
            print(f"Row is safe: {row['row']}")
            safeRows += 1
    elif len(differErrors['index']) == 1 and len(row['index']) == 0:
        print(f"Row is safe: {row['row']}")
        safeRows += 1
    elif len(differErrors['index']) == 0 and len(row['index']) == 1:
        print(f"Row is safe: {row['row']}")
        safeRows += 1
    print("\n")

    return safeRows

puzzle2Part1()