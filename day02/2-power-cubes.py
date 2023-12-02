def remove_zeros(dict: dict[str, int]):
    return {key: value for key, value in dict.items() if value != 0}


def parse_game(game: str):
    draws_per_color = {"red": 0, "green": 0, "blue": 0}

    for item in game.split(", "):
        [draws, color] = item.split(" ")
        draws_per_color[color] += int(draws)

    return remove_zeros(draws_per_color)


def get_minimum_set(game_rounds):
    colors = ["red", "green", "blue"]
    minimum_set = {
        color: max(round_.get(color, 0) for round_ in game_rounds) for color in colors
    }

    return remove_zeros(minimum_set)


def power(game_dict: dict[str, int]):
    return (
        game_dict.get("red", 1) * game_dict.get("green", 1) * game_dict.get("blue", 1)
    )


def solution(file_path='./input/puzzle.txt'):
    sum_of_powers = 0

    with open(file_path, 'r') as file:
        for line in file:
            game_id, subsets = map(str.strip, line.split(': '))
            game_id = game_id.replace('Game ', '')
            rounds = [parse_game(round) for round in subsets.split('; ')]
            minimum_set = get_minimum_set(rounds)
            sum_of_powers += power(minimum_set)

    print(f"Sum of powers: {sum_of_powers}")

if __name__ == "__main__":
    solution()
