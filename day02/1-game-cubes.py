

def parse_game(game: str):
  draws_per_color = {
    "red": 0,
    "green": 0,
    "blue": 0
  }

  for item in game.split(', '):
    [draws, color] = item.split(' ')
    draws_per_color[color] += int(draws)

  return draws_per_color

def validate_game(game_dict: dict[str, int]):
  return game_dict["red"] <= 12 and game_dict["green"] <= 13 and game_dict["blue"] <= 14
  

def solution(file_path = './input/puzzle.txt'):

  file = open(file_path, 'r')

  valid_games = 0

  for line in file:
    [game_id, subsets] = line.strip().split(': ')

    game_id = game_id.replace('Game ', '')
    subsets = subsets.split('; ')
    game_is_valid = True
    for game in subsets:
      game_dict = parse_game(game)
      round_is_valid = validate_game(game_dict)
      game_is_valid = game_is_valid and round_is_valid

    if (game_is_valid):
      valid_games += int(game_id)


      

  print (f"valid_games: {valid_games}")

  file.close()


if __name__ == '__main__':
  solution()