def total_distance(time_held: int, total_time: int) -> int:
    return (total_time - time_held) * time_held


def solution(file_path="input/puzzle.txt"):

    input_data = open(file_path, 'r').read().splitlines()
    input_data = [d.split(': ')[1].strip().split() for d in input_data]
    [time, goal] = input_data
    time = int(''.join(time))
    goal = int(''.join(goal))

    ways_to_win = 0
    for t in range(time):
        d = total_distance(t, time)
        if d > goal:
            ways_to_win += 1
            
    print(f"margin: {ways_to_win}")
    

if __name__ == "__main__":
    solution()
