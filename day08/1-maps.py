def solution(file_path="input/puzzle.txt"):
    directions = ""
    lines = []
    with open(file_path, "r") as file:
        directions, _, *lines = file.read().splitlines()

    network = {}
    for line in lines:
        [node, connections] = line.split(" = ")
        connections = connections.replace("(", '').replace(")", '')
        network[node] = connections.split(', ')

    current = "AAA"
    current_step = 0
    steps_count = 0
    while current != "ZZZ":
        step = 1 if directions[current_step] == "R" else 0
        print(f"{steps_count}: going {directions[current_step]} from {current} to {network[current][step]}")
        current = network[current][step]
        steps_count += 1
        current_step = (current_step + 1) if current_step < len(directions) - 1 else 0

    print(f"Steps count: {steps_count}")

if __name__ == "__main__":
    solution()
