def remove_zeros(game_round: dict[str, int]):
  return {key: value for key, value in game_round.items() if value != 0}


def parse_game(game: str):
  draws_per_color = {
    "red": 0,
    "green": 0,
    "blue": 0
  }

  for item in game.split(', '):
    [draws, color] = item.split(' ')
    draws_per_color[color] += int(draws)

  return remove_zeros(draws_per_color)

def get_minimum_set(game_rounds):
    minimum_set = {
    "red": 0,
    "green": 0,
    "blue": 0,
  }

    for round in game_rounds:
      
      if "red" in round and round["red"] > minimum_set["red"]:
        minimum_set["red"] = round["red"]

      if "green" in round and round["green"] > minimum_set["green"]:
        minimum_set["green"] = round["green"]

      if "blue" in round and round["blue"] > minimum_set["blue"]:
        minimum_set["blue"] = round["blue"]

    return remove_zeros(minimum_set)


def validate_game(game_dict: dict[str, int]):
  return game_dict["red"] <= 12 and game_dict["green"] <= 13 and game_dict["blue"] <= 14

def power(game_dict: dict[str, int]):
  return game_dict["red"] * game_dict["green"] * game_dict["blue"]


def solution(file_path = './input/puzzle.txt'):
  file = open(file_path, 'r')
  sum_of_powers = 0

  for line in file:
    [game_id, subsets] = line.strip().split(': ')
    game_id = game_id.replace('Game ', '')
    subsets = subsets.split('; ')
    rounds = [parse_game(round) for round in subsets]
    minimum_set = get_minimum_set(rounds)
    sum_of_powers += power(minimum_set)

  print (f"sum of powers: {sum_of_powers}")
  file.close()

if __name__ == '__main__':
  solution()