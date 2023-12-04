def prepare_str(list: str):
    return list.replace('  ', ' ').strip().split(' ')

def solution(file_path="input/puzzle.txt"):
    with open(file_path, "r") as file:
        total_points = 0
        for line in file:
            [_, all_numbers] = line.split(': ')
            [winning_numbers, contestants] = all_numbers.split(' | ')
            winning_numbers = [int(x) for x in prepare_str(winning_numbers)]
            contestants = [int(x) for x in prepare_str(contestants)]
            
            winners = []

            for number in contestants:
                if number in winning_numbers:
                    winners.append(number)
            if (len(winners) > 0):
                total_points += pow(2, len(winners) - 1)


        print(f'total points: {total_points}')



if __name__ == "__main__":
    solution()
