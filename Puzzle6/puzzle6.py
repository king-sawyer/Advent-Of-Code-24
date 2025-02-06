WIDTH = 0
HEIGHT = 0

def part_1(data, start_position, direction) -> bool:

    if start_position[0] < WIDTH or start_position[1] < HEIGHT:
        return True

    next_x, next_y = 1
    next_direction = ''

    match direction:
        case 'u':
            next_x = 0
            next_y = 1
            next_direction = 'r'
        case 'r': 
            next_x = 1
            next_y = 0
            next_direction = 'd'
        case 'd':
            next_x = 0
            next_y = -1
            next_direction = 'l'
        case 'l':
            next_x = -1
            next_y = 0
            next_direction = 'u'

    # If next position is an x
    # If next position is out of bounds
    # otherwise move forward

    return False

def part_2() -> bool:
    

    return False

def main() -> bool:
    with open('ex.txt', 'r') as file:
            data = [line.strip() for line in file.readlines()]

    global WIDTH 
    global HEIGHT 

    WIDTH = len(data[0])
    HEIGHT = len(data)

    direction = 'u'
    starting_position = []

    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == '^':
                 starting_position = [i,j]

    part_1(data,starting_position,direction)

    print(WIDTH)
    print(HEIGHT)
    print(starting_position)

    return False

main()