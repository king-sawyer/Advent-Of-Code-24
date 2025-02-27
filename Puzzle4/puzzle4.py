from typing import List

WIDTH = 0
HEIGHT = 0

def part_1(data: List[str]) -> int:


    check_string = ['M', 'A', 'S']
    x_array = []
    words_found = 0

    lines = {
        "right":                [(0, 1), (0,1), (0,1)],
        "left":                 [(0,-1), (0,-1), (0,-1)],
        "up":                   [(1,0), (1,0), (1,0)],
        "down":                 [(-1,0), (-1,0), (-1,0)],
        "up-diagonal-right":    [(1,1), (1,1), (1,1)],
        "down-diagonal-right":  [(-1,1),(-1,1),(-1,1)],
        "up-diagonal-left":     [(1,-1), (1,-1), (1,-1)],
        "down-diagonal-left":   [(-1,-1),(-1,-1),(-1,-1)]
    }

    # Extract x locations
    for i, row in enumerate(data):
        for j in range(len(row)):
            if row[j] == 'X': x_array.append([i, j])

    for x_location in x_array:
        for direction in lines.values():
            words_found += check_adjacent(x_location[0], x_location[1], direction, 0, data, check_string, string_index=0)

    return words_found

def part_2(data: List[str]) -> int:

    check_string = [['M', 'M', 'S', 'S'],
                    ['M', 'S', 'S', 'M'],
                    ['S', 'S', 'M', 'M'],
                    ['S', 'M', 'M', 'S']]
    
    lines = [(-1,-1), (0,2), (2,0), (0,-2)]

    a_array = []
    words_found = 0


    # Extract a locations
    for i, row in enumerate(data):
        for j in range(len(row)):
            if row[j] == 'A':
                a_array.append([i, j])

    for substring in check_string:
        for a_location in a_array:
            words_found += check_adjacent(a_location[0], a_location[1], lines, 0, data, substring, string_index=0)

    return words_found



def check_adjacent(current_row, current_col, line, line_index, data, check_string, string_index) -> bool:
    
    if line_index > len(line):
        return False
    
    if string_index == len(check_string):
        return True

    next_row, next_col = line[line_index]
    check_row = current_row + next_row
    check_col = current_col + next_col

    if 0 <= check_row < HEIGHT and 0 <= check_col < WIDTH:

        if data[check_row][check_col] == check_string[string_index]:
            return check_adjacent(check_row, check_col, line, line_index +1, data, check_string, string_index+1)
    
        
            
    return False
    

def main() -> int:
    with open('data.txt', 'r') as file:
            data = [line.strip() for line in file.readlines()]

    global WIDTH 
    global HEIGHT 

    WIDTH = len(data[0])
    HEIGHT = len(data)
    

    print(f"Part 1: {part_1(data)}")
    print(f"Part 2: {part_2(data)}")

    return 0

main()

