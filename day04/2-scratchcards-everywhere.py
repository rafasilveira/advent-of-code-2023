def prepare_str(list: str):
    return list.replace('  ', ' ').strip().split(' ')

def prepare_line(line: str) -> tuple[int, set[int], set[int]]:
    [card_id, all_numbers] = line.split(': ')

    [winning_numbers, contestants] = all_numbers.split(' | ')
    winning_numbers = set([int(x) for x in prepare_str(winning_numbers)])
    contestants = set([int(x) for x in prepare_str(contestants)])

    card_id = int(card_id.split()[1])
    
    winners = []

    for number in contestants:
        if number in winning_numbers:
            winners.append(number)

    return (card_id, winning_numbers, contestants)

def solution(file_path="input/puzzle.txt"):
    cards_list = []
    cards_map = {}
    result = 0
    
    with open(file_path, "r") as input_file:
        for line in input_file:
            parsed_line = prepare_line(line)
            cards_list.append(parsed_line)


    print("begin mapping cards")
    for index, card in enumerate(cards_list):
        [card_id, winners, contestants] = card
        print(f" mapping card {card_id}")
    
        cards_map[card_id] = []
        wins = winners.intersection(contestants)

        for win_index in range(1, len(wins)+1):
            cards_map[card_id].append(cards_list[index + win_index])
    print("end mapping cards")

    print("begin counting cards")
    while len(cards_list) > 0:

        card = cards_list.pop(0)
        print(f" counting card {result}")
        cards_list.extend(cards_map[card[0]])
        result += 1
    
    print(f"Total cards: {result}")
    

if __name__ == "__main__":
    solution()
