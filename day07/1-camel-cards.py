from collections import Counter
from functools import cmp_to_key

Card = tuple[int, str]

type_strength = {
    "five_of_kind": 6,
    "four_of_kind": 5,
    "full_house": 4,
    "three_of_kind": 3,
    "two_pair": 2,
    "one_pair": 1,
    "high_card": 0
}


strength = {
    "A": 13,
    "K": 12,
    "Q": 11,
    "J": 10,
    "T": 9,
    "9": 8,
    "8": 7,
    "7": 6,
    "6": 5,
    "5": 4,
    "4": 3,
    "3": 2,
    "2": 1,
}


def is_five_of_kind(hand: str) -> bool:
    return 5 in Counter(hand).values()


def is_four_of_kind(hand: str) -> bool:
    return 4 in Counter(hand).values()


def is_full_house(hand: str) -> bool:
    cards_counter = Counter(hand).values()
    return 3 in cards_counter and 2 in cards_counter


def is_three_of_kind(hand: str) -> bool:
    return 3 in Counter(hand).values()


def is_two_pair(hand: str) -> bool:
    cards_counter = Counter(hand).values()
    return 2 in Counter(cards_counter).values()


def is_one_pair(hand: str) -> bool:
    cards_counter = Counter(hand).values()
    return 2 in cards_counter and 3 in Counter(cards_counter).values()


def first_is_stronger(first: str, second: str) -> bool:
    for i in range(len(first)):
        if first[i] != second[i]:
            return strength[first[i]] > strength[second[i]]

        return first_is_stronger(first[i + 1 :], second[i + 1 :])


def get_type(hand: str) -> str:
    if is_five_of_kind(hand):
        return "five_of_kind"
    if is_four_of_kind(hand):
        return "four_of_kind"
    if is_full_house(hand):
        return "full_house"
    if is_three_of_kind(hand):
        return "three_of_kind"
    if is_two_pair(hand):
        return "two_pair"
    if is_one_pair(hand):
        return "one_pair"
    return "high_card"


def compare_hands(first: Card, second: Card) -> bool:
    h1 = first[0]
    h2 = second[0]
    h1_type = get_type(h1)
    h2_type = get_type(h2)

    if h1_type == h2_type:
        return 1 if first_is_stronger(h1, h2) else -1
    return 1 if type_strength[h1_type] > type_strength[h2_type] else -1


def solution(file_path="input/puzzle.txt"):
    hands: list[Card] = []
    with open(file_path, "r") as file:
        for line in file:
            [hand, bid] = line.strip().split()
            hands.append((hand, int(bid)))

    sorted_hands = sorted(hands, key=cmp_to_key(compare_hands))
    total_winnings = 0
    for rank, hand in enumerate(sorted_hands, 1):
        total_winnings += rank * hand[1]

    print(f"total winnings: {total_winnings}")


if __name__ == "__main__":
    solution()
