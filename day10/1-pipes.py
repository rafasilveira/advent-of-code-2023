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

        if (
            row < len(grid) - 1
            and char in "S|7F"
            and grid[row + 1][col] in "|JL"
            and cell_down not in loop
        ):
            loop.add(cell_down)
            queue.append(cell_down)

        if (
            col > 0
            and char in "S-J7"
            and grid[row][col - 1] in "-LF"
            and cell_left not in loop
        ):
            loop.add(cell_left)
            queue.append(cell_left)

        if (
            col < len(grid[row]) - 1
            and char in "S-LF"
            and grid[row][col + 1] in "-J7"
            and cell_right not in loop
        ):
            loop.add(cell_right)
            queue.append(cell_right)

    print(f"distance: {len(loop) // 2}")


if __name__ == "__main__":
    solution()
