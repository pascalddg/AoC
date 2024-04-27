import aoc_helper as ah
from functools import reduce
raw_data = ah.load_data(2)

test_data = \
'''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'''.splitlines()

goal = {'red':12,'green':13,'blue':14}

def parse_data(raw_data):
    result = {}
    for line in raw_data:
        game, draws = line.split(':')
        game_no = int(game.replace('Game ',''))
        result[game_no]=[]
        for draw in draws.split(';'):
            group = {}
            for num_color in draw.strip().split(','):
                num, color = num_color.strip().split(' ')    
                group[color.strip()] = int(num.strip())
            result[game_no].append(group)
    return result

#raw_data=test_data
data = parse_data(raw_data)

good_games=[]

for game, draws in data.items():
    for draw in draws:
        for color in draw.keys():
            if draw[color]>goal[color]:
                game = None
    if game:
        good_games.append(game)

print(f'{good_games = }')
print(f'{sum(good_games) = }')

powers = []
for game, draws in data.items():
    mins={}
    for draw in draws:
        for color in draw.keys():
            mins[color] = max(draw[color], mins.get(color, 0))
    powers.append(reduce((lambda x, y: x * y), mins.values()))

print(f'{powers = }')
print(f'{sum(powers) = }')
