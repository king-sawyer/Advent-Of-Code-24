"""
Puzzle - 3
Description:
Part 1:
   - Add the result of multiplying X and Y for every complete instance of the string mult(X,Y) in the data, with X and Y being an integer up to three digits, and return it.

Things that I learned about python:
- split() returns a list where every item starts at the next seperator found. It does not include the seperator in the list.
"""
def part_1(data: str) -> int:

    total = 0
    locations = data.split('mul(')
    numbers = []

    for location in locations:
        location = location.split(')')
        location = location[0].split(',')
        if len(location) == 2 and location[0].isnumeric() and location[1].isnumeric():
                numbers.append([int(location[0]), int(location[1])])
    
    for pair in numbers:
         total += (pair[0] * pair[1])

    return total

def part_2(data: str) -> int:

    return_string = ""
    conditionals = data.split('do')
    
    for conditional in conditionals:
        if len(conditional) > 3:
            if conditional[0] == "n" and conditional[1] == "'" and conditional[2] == "t":
                continue
            else:
                return_string += conditional

    return part_1(return_string)

def main():
    data = open("data.txt", "r").read()
    print(f"Part 1: {part_1(data)}")
    print(f"Part 2: {part_2(data)}")

main()