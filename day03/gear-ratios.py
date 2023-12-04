# based on https://github.com/tomquinn8/AdventOfCode/blob/main/2023/Day3.py

import re

def solution(file_path="input/puzzle.txt"):
    with open(file_path, "r") as file:
        lines = list(file)
        sum_part_numbers = 0
        parts = {}
        gears = {}
        

        for row in range(len(lines[0]) - 1):
            for col in range(len(lines)):
                if lines[row][col] not in '0123456789.':
                    parts[(row, col)] = lines[row][col]
                    if lines[row][col] == '*':
                        gears[(row,col)] = []

        for row_num, row in enumerate(lines):
            for c in re.finditer(r'\d+', row):
                possibilities = []
                for i in range(c.start() - 1, c.end() + 1):
                    possibilities.append((row_num - 1, i))
                    possibilities.append((row_num, i))
                    possibilities.append((row_num + 1, i))
                valid = False
                for p in possibilities:
                    if p in parts:
                        valid = True
                        if p in gears:
                            gears[p].append(int(c.group()))
                if valid:
                    sum_part_numbers += int(c.group())
        print(f"sum of part numbers: {sum_part_numbers}")
        sum_gear_ratios = 0
        for g in gears:
            if len(gears[g]) == 2:
                sum_gear_ratios += (gears[g][0] * gears[g][1])
        print(f"sum of gear ratios: {sum_gear_ratios}")
        


if __name__ == "__main__":
    solution()

