"""
Puzzle 2 - Part 1
Add up the total number of rows that satisfy the following two rules:
- A row must be either ascending or descending
- Each number in the row must differ from the following number by at least one and no more than three
"""

def puzzle2Part1():

    "Utilizing readlines vs pandas as the data is stored in rows compared to columns"
    with open('datacpy.txt', 'r') as file:
        data = file.readlines()

    "Converting each row to an array of integers stored in the parrent array: rows"
    rows = [list(map(int, row.split())) for row in data]

    "The number of rows that satisty both rules"
    firstRule = 0
    asc = 0
    desc = 0
    neither = 0

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
        for j in range(i + 1, len(row)):
            if row[i] > row[j]:
                asc['index'].append(i)
                asc['number'].append(row[i])
                break
                
            
            if row[i] < row[j]:
                desc['index'].append(i)
                desc['number'].append(row[i])
                break
                




    if len(asc["index"]) < 2:
       
        totalSafeRows += checkNumDiffer(asc)
    elif len(desc['index']) < 2:
        
            
        totalSafeRows += checkNumDiffer(desc)
    else:
        print(f"Neither row: {row}")
        #return "neither"


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
                if nextDiffer in (1,2,3) and i != 0:
                    differErrors['index'].append(i+1)
                    differErrors['number'].append(row['row'][i+1]) 
                    differErrors['index'].append(i+2)
                    differErrors['number'].append(row['row'][i+2]) 
                else:
                    differErrors['index'].append(i)
                    differErrors['number'].append(row['row'][i])
            else:
                differErrors['index'].append(i+1)
                differErrors['number'].append(row['row'][i+1])

    # 8 6 4 4 1

   
                
                    

    if len(differErrors['index']) == 0 and len(row['index']) == 0:
        safeRows += 1
        print(f"Row is safe: {row['row']} - No ascending/descending errors and no differ errors")
    elif len(differErrors['index']) == 1 and len(row['index']) == 1:
        if differErrors['index'] == row['index']:
            print(f"Row is safe: {row['row']} - One error in the same index")
            print(f"numbers: {differErrors['number']} Indexes: {differErrors['index']}\n")
            safeRows += 1
    elif len(differErrors['index']) == 1 and len(row['index']) == 0:
        print(f"Row is safe: {row['row']} - one differ error")
        print(f"numbers: {differErrors['number']} Indexes: {differErrors['index']}\n")
        safeRows += 1
    elif len(differErrors['index']) == 0 and len(row['index']) == 1:
        print(f"Row is safe: {row['row']} - one ascending/descending error")
        print(f"numbers: {row['number']} Indexes: {row['index']}\n")
        safeRows += 1
    else:
        print(f"\nRow is not safe: {row['row']}")
        print(f"Differ errors: {differErrors}")
        print(f"Ascending/Descending errors: {row['number']} Indexes: {row['index']}\n")


    return safeRows

puzzle2Part1()