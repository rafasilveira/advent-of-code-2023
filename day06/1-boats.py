def total_distance(time_held: int, total_time: int) -> int:
    return (total_time - time_held) * time_held


def solution(file_path="input/puzzle.txt"):

    races = []
    input_data = open(file_path, 'r').read().splitlines()
    input_data = [d.split(': ')[1].strip().split() for d in input_data]
    [times, distances] = input_data
    times = [int(t) for t in times]
    distances = [int(d) for d in distances]

    for i in range(len(times)):
        races.append((times[i], distances[i]))
        
    margin_of_error = []
    for race in races:
        (time, goal) = race
        ways_to_win = 0
        for t in range(time):
            d = total_distance(t, time)
            if d > goal:
                ways_to_win += 1
        margin_of_error.append(ways_to_win)
    mult = 1
    for me in margin_of_error:
        mult *= me
            
    print(f"margin: {margin_of_error}")
    print(f"multiplication: {mult}")
    

    

if __name__ == "__main__":
    solution()
