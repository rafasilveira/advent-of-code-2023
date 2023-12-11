# https://www.youtube.com/watch?v=r3i3XE9H4uw
# https://github.com/hyper-neutrino/advent-of-code/blob/main/2023/day10p1.py

from collections import deque


def solution(file_path="input/puzzle.txt"):
    grid = []
    with open(file_path, "r") as file:
        grid = file.read().strip().splitlines()

    starting_row = ""
    starting_col = ""

    for r, row in enumerate(grid):
        for c, char in enumerate(row):
            if char == "S":
                starting_row = r
                starting_col = c
                break
        # else-continue-break is a way to propagate a inner break outside
        else:
            continue
        break

    # breadth-first flood
    # start at some point
    # try every single position
    # if valid, add to queue; invalid, ignore
    # go to next in queue, try every single pos
    # if loop or invalid, ignore; valid, add to queue

    loop = {(starting_row, starting_col)}
    queue = deque([(starting_row, starting_col)])
    maybe_s = {"|", "-", "J", "L", "7", "F"}

    while queue:
        row, col = queue.popleft()

        char = grid[row][col]

        cell_up = (row - 1, col)
        cell_down = (row + 1, col)
        cell_left = (row, col - 1)
        cell_right = (row, col + 1)

        if (
            row > 0
            and char in "S|JL"
            and grid[row - 1][col] in "|7F"
            and cell_up not in loop
        ):
            loop.add(cell_up)
            queue.append(cell_up)
            if char == 'S': maybe_s &= {'|', "J", 'L'}

        if (
            row < len(grid) - 1
            and char in "S|7F"
            and grid[row + 1][col] in "|JL"
            and cell_down not in loop
        ):
            loop.add(cell_down)
            queue.append(cell_down)
            if char == 'S': maybe_s &= {'|', "7", 'F'}
        if (
            col > 0
            and char in "S-J7"
            and grid[row][col - 1] in "-LF"
            and cell_left not in loop
        ):
            loop.add(cell_left)
            queue.append(cell_left)
            if char == 'S': maybe_s &= {"-", "J", "7"}


        if (
            col < len(grid[row]) - 1
            and char in "S-LF"
            and grid[row][col + 1] in "-J7"
            and cell_right not in loop
        ):
            loop.add(cell_right)
            queue.append(cell_right)
            if char == 'S': maybe_s &= {"-", "L", "F"}

    (S,) = maybe_s
    grid = [row.replace("S", S) for row in grid]
    grid = ["".join(ch if (r, c) in loop else "." for c, ch in enumerate(row)) for r, row in enumerate(grid)]

    outside = set()
    for r, row in enumerate(grid):
        within = False
        up = None
        for c, ch in enumerate(row):
            if ch == "|":
                assert up is None
                within = not within
            elif ch == "-":
                assert up is not None
            elif ch in "LF":
                assert up is None
                up = ch == "L"
            elif ch in "7J":
                assert up is not None
                if ch != ("J" if up else "7"):
                    within = not within
                up = None
            elif ch == ".":
                pass
            else:
                raise RuntimeError(f"unexpected character (horizontal): {ch}")
            if not within:
                outside.add((r, c))
                
    print(len(grid) * len(grid[0]) - len(outside | loop))


if __name__ == "__main__":
    solution()
