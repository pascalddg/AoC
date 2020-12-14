from collections import deque
test_data="""L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""


def load_data():
    with open("aoc20-11-data.txt", "r") as f:
        data = f.read().splitlines() 
    print("Loaded lines:", len(data))
    return data

def count_neighbours(table, y, x):
    width = len(table[0])
    height = len(table)
    neighbours = 0
    for j in range(max(0,y-1),min(height,y+2)):
        neighbours += table[j][max(0,x-1):min(width,x+2)].count('#')
    if table[y][x] == '#':
        neighbours -= 1
    return neighbours

def update_seat(table, y, x):
    if table[y][x] == '.':
        return '.'
    neighbours = count_neighbours(table, y, x)
    if neighbours == 0:
        return '#'
    if neighbours >=4:
        return 'L'
    return table[y][x]


def look_dir(table, y, x, dy, dx):
    width = len(table[0])
    height = len(table)
    nx = x+dx
    ny = y+dy
    while 0<=nx<width and 0<=ny<height: 
        if table[ny][nx]=="#":
            return 1
        if table[ny][nx]=="L":
            return 0
        nx += dx
        ny += dy
    return 0

dirc_all = (
        (-1, 1), (0, 1), (1, 1),
        (-1, 0),         (1, 0),
        (-1,-1), (0,-1), (1,-1)
        )

def count_neighbours2(table, y, x):
    neighbours = 0
    for dirc in dirc_all:
        neighbours += look_dir(table,y,x,dirc[0],dirc[1])
        # if neighbours==5:
        #     break
    return neighbours


def update_seat2(table, y, x):
    if table[y][x] == '.':
        return '.'
    neighbours = count_neighbours2(table, y, x)
    if neighbours == 0:
        return '#'
    if neighbours >=5:
        return 'L'
    return table[y][x]


data = load_data()
# uncomment the below line to work on the test data
#data = test_data.splitlines()

first_table = [[c for c in line] for line in data]

table = first_table
occupied = sum((line.count("#") for line in table))
previous = -1
while previous!=occupied:
    print(f'{occupied=}')
    previous = occupied
    table = [[update_seat(table, y, x) for x, _ in enumerate(line)] for y,line in enumerate(table)]
    occupied = sum((line.count("#") for line in table))

result = occupied
print(f'result = {result}')

table = first_table
occupied = sum((line.count("#") for line in table))
previous = -1
while previous!=occupied:
    print(f'{occupied=}')
    previous = occupied
    table = [[update_seat2(table, y, x) for x, _ in enumerate(line)] for y,line in enumerate(table)]
    occupied = sum((line.count("#") for line in table))

result2 = occupied
print(f'result2 = {result2}')
