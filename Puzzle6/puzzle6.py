WIDTH = 0
HEIGHT = 0

import sys
sys.setrecursionlimit(50000)

def part_1(data, start_position, direction, visited_locations) -> int:

    next_col = next_row = 1
    next_direction = ''

    match direction:
        case 'u':
            next_col = 0
            next_row = -1
            next_direction = 'r'
        case 'r': 
            next_col = 1
            next_row = 0
            next_direction = 'd'
        case 'd':
            next_col = 0
            next_row = 1
            next_direction = 'l'
        case 'l':
            next_col = -1
            next_row = 0
            next_direction = 'u'

    new_start_position = [start_position[0] + next_row, start_position[1] + next_col]

    if (new_start_position[0]) >= HEIGHT or (new_start_position[0]) < 0 or (new_start_position[1]) >= WIDTH or (new_start_position[1]) < 0:
        return 1
    
    visited_locations[start_position[0]][start_position[1]] = 'X'

    # If next position is an #
    if data[new_start_position[0]][new_start_position[1]] == '#':
        
        return part_1(data, start_position, next_direction, visited_locations)
    # Move
    else:
        
        if visited_locations[new_start_position[0]][new_start_position[1]] == 'X':
            return part_1(data, new_start_position, direction, visited_locations) 
        else:
            return part_1(data, new_start_position, direction, visited_locations) + 1



def part_2() -> bool:
    

    return False

def main() -> bool:
    with open('data.txt', 'r') as file:
            data = [line.strip() for line in file.readlines()]

    global WIDTH 
    global HEIGHT 

    WIDTH = len(data[0])
    HEIGHT = len(data)

    direction = 'u'
    starting_position = []
    part_1_result = 0
    visited_locations = [['.' for _ in range(WIDTH)] for _ in range(HEIGHT)]

    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == '^':
                 starting_position = [i,j]



    part_1_result = part_1(data, starting_position, direction, visited_locations)

    print(part_1_result)

    return False

main()