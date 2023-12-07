# https://www.youtube.com/watch?v=NmxHw_bHhGM

def solution(file_path="input/puzzle.txt"):
    inputs, *blocks = open(file_path, "r").read().split('\n\n')
    inputs = list(map(int, inputs.split(":")[1].split()))
    seeds = []

    for i in range(0, len(inputs), 2):
        seeds.append((inputs[i], inputs[i] + inputs[i + 1]))    
    
    for block in blocks:
        ranges = []
        for line in block.splitlines()[1:]:
            ranges.append(list(map(int, line.split())))

        new_ranges = []

        while len(seeds) > 0:
            seed_range_start, seed_range_end = seeds.pop()
            for range_dest, range_src, range_length in ranges:
                overlap_start = max(seed_range_start, range_src)
                overlap_end = min(seed_range_end, range_src + range_length)
                if overlap_start < overlap_end:
                    new_ranges.append((overlap_start - range_src + range_dest, overlap_end - range_src + range_dest))
                    if overlap_start > seed_range_start:
                        seeds.append((seed_range_start, overlap_start))
                    if seed_range_end > overlap_end:
                        seeds.append((overlap_end, seed_range_end))
                    break
            else:
                new_ranges.append((seed_range_start, seed_range_end))
        seeds = new_ranges
    

    print(f"closest: {min(seeds)[0]}")

if __name__ == "__main__":
    solution()
