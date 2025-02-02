"""
Puzzle - 5
Description:
Part 1:
   - Verify a rule by iterating thorugh each number in a rule and checking to see if the numbers that came before were not associated with a rule that required it came after the current number.
   - Once you have all safe rules, add up the integers in the middle index of the rule and return the total.

Things that I learned about python:
- // -> floor division. Allows you to divide and round down
"""
def part_1(x_y_values, rules) -> int:

    correct_rows = []
    return_value = 0

    for rule in rules:
        for i in range(len(rule)):
            result = check_row(rule[i], rule[:i], x_y_values)
            if not result: break
        if result:
            correct_rows.append(rule)

    for row in correct_rows:
        return_value += row[len(row) // 2]
        

    return return_value

def check_row(num, row, x_y_values) -> bool:
    for i in range(len(row)):
        if num in x_y_values:
            if row[i] in x_y_values[num]:
                return False

    return True

def main() -> int:
    with open("data.txt", "r") as file:
        data = file.read().strip()

    sections = data.split("\n\n")
    
    x_y_values = {}
    for line in sections[0].splitlines():
        x,y = map(int, line.split("|"))
        if x not in x_y_values:
            x_y_values[x] = []
        x_y_values[x].append(y)

    rules = [list(map(int, line.split(","))) for line in sections[1].splitlines()]

    print(f"Part 1: {part_1(x_y_values, rules)}")

    return 0

main()