"""
Puzzle 2
Description:
Part 1:
   Add up the total number of rows that satisfy the following two rules:
   - A row must be either ascending or descending
   - Each number in the row must differ from the following number by at least one and no more than three
Part 2:
   - Above rules apply however a row is considered safe if removing one integer results in the row being made safe

Personal notes:
Part 2 really challenged me. I kept getting stuck with figuring out what number to remove. 
My attempts involved comparing each index with the following two numbers, checking the first/last, and other very inefficient methods.
I ended up watching a video made by a youtuber named 0xdf who recommended putting part 1 in a function then 
calling that funciton in a part 2 function.

Things that I learned about python:
all() - returns true if all elements of a given iterable are true
zip() - returns a zip object which is an iterator of tuples -> [1, 2, 3] [7, 8, 9] => [(1,7), (2,8), (3,9)]
list slicing [start:end:step] -> a = [1, 2, 3, 4, 5] => print(a[2:]) -> [3, 4, 5]
"""

def puzzle_2():

    with open('data.txt', 'r') as file:
        data = file.readlines()

    rows = [list(map(int, row.split())) for row in data]

    part_1_result = 0
    part_2_result = 0

    for row in rows:
        part_1_result += part_1(row)
        part_2_result += part_2(row)

    print(f"Origional row:\n{rows[0]}")
    print("row with [:i]")
    for i in range(len(rows[0])):
        #print(rows[0][:i] + rows[0][i+1:])
        print(rows[0][:i])
    print('\n')
    print("row with [i+1:]")
    for i in range(len(rows[0])-1):
        #print(rows[0][:i] + rows[0][i+1:])
        print(rows[0][i+1:])
    print('\n')
    print("row with [i+1:]")
    for i in range(len(rows[0])-1):
        print(rows[0][:i] + rows[0][i+1:])

    print(f"Part 1: {part_1_result}")
    print(f"Part 2: {part_2_result}")
        
def part_1(row) -> bool:
    number_pairs = list(zip(row, row[1:]))
    diffs = [abs(x1-x2) for x1, x2 in number_pairs]
    if not all(1 <= d <= 3  for d in diffs):
         return False
    if all(x1 < x2 for x1, x2 in number_pairs):
        return True
    if all(x1 > x2 for x1, x2 in number_pairs):
        return True
    
    return False
    
def part_2(row) -> bool:
    if part_1(row):
        return True
    for i in range(len(row)):
        if part_1(row[:i] + row[i+1:]):
            return True
    return False
    
puzzle_2()