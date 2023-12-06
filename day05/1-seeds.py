# https://www.youtube.com/watch?v=NmxHw_bHhGM

def solution(file_path="input/puzzle.txt"):
    seeds, *blocks = open(file_path, "r").read().split('\n\n')
    
    seeds = list(map(int, seeds.split(":")[1].split()))
    for block in blocks:
        ranges = []
        new = []
        for line in block.splitlines()[1:]:
            ranges.append(list(map(int, line.split())))

        for seed in seeds:

            for destination, source, length in ranges:
                if source <= seed < source + length:
                    new.append(seed - source + destination)
                    break
            else:
                new.append(seed)

        seeds = new
    print(f"closest: {min(new)}")

if __name__ == "__main__":
    solution()
