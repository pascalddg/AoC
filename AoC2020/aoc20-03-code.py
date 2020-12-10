import math


def load_data():
    with open("aoc20-03-data.txt", "r") as f:
        data = f.read().splitlines()  # read file and removes end of line character
    print("Loaded lines:", len(data))
    return data
def count_trees(forest, step_x, step_y):
    pattern_size = len(forest[0])
    counter = 0
    x = 0
    for y in range(step_y, len(forest), step_y):
        x = (x + step_x) % pattern_size
        if forest[y][x] == '#':
            counter += 1
    return counter


data = load_data()

# first task
counter = count_trees(data, 3, 1)
print(f'{counter=}')

# second task
slopes = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
results = [count_trees(data, slope[0], slope[1]) for slope in slopes]
product = math.prod(results)
print(f'{results=}')
print(f'{product=}') 


