import time
import math
from itertools import product
from collections import deque

def load_data():
    with open("AoC2020/aoc20-20-data.txt", "r") as f:
        data = f.read().splitlines() 
    print("Loaded lines:", len(data))

    with open("AoC2020/aoc20-20-testdata.txt", "r") as f:
        testdata = f.read().splitlines() 
    print("Loaded lines:", len(testdata))
 
    return data, testdata

def edge2shape(edges):
    return tuple(int(line,2) for line in edges)


def flip_h(edges):
    return [edges[2],edges[1][::-1],edges[0],edges[3][::-1]]


def flip_v(edges):
    return [edges[0][::-1],edges[3],edges[2][::-1],edges[1]]


def rotate(edges):
    return [edges[3][::-1],edges[0],edges[1][::-1],edges[2]]


def get_shapes(p_tile):
    edges=[0,0,0,0]
    shapes = set()
    edges[0]=p_tile[1][0]
    edges[2]=p_tile[1][9]
    e1, e3 =[], []
    for line in p_tile[1]:
        e1.append(line[9])
        e3.append(line[0])
    edges[1]=''.join(e1)
    edges[3]=''.join(e3)
    edges = [s.replace('.','0').replace('#','1') for s in edges]
    
    for i in range(4):
        shapes.add(edge2shape(edges))
        shapes.add(edge2shape(flip_h(edges)))
        shapes.add(edge2shape(flip_v(edges)))
        shapes.add(edge2shape(flip_h(flip_v(edges))))
        edges = rotate(edges)
        
    return tuple(shapes)

# [id, [lines], [shapes]]
def parse_data(p_data):
    tiles = []
    tile=[0,[],[]]
    for line in data:
        if line.startswith("Tile"):
            tile[0]=int(line[5:-1])
        elif not line:
            tile[2]=get_shapes(tile)
            tiles.append(tile)
            tile=[0,[],[]]
        else:
            tile[1].append(line)
    if tile[0]:
        tile[2]=get_shapes(tile)
        tiles.append(tile)

    return tiles

def fit(mosaic, shape, px,py):
    if not 0<=px<len(mosaic) or not 0<=py<len(mosaic):
        return False

    if px>0 and mosaic[px-1][py]:
        if mosaic[px-1][py][1][1]!=shape[3]:
            return False
    if px<len(mosaic)-1 and mosaic[px+1][py]:
        if mosaic[px+1][py][1][3]!=shape[1]:
            return False
    if py>0 and mosaic[px][py-1]:
        if mosaic[px][py-1][1][0]!=shape[2]:
            return False
    if py<len(mosaic)-1 and mosaic[px][py+1]:
        if mosaic[px][py+1][1][2]!=shape[0]:
            return False

    return True

counter = 0
maxi = 0
t1 = time.perf_counter()
dirc = ((-1,0),(1,0),(0,1),(0,-1))
def arrange(mosaic, tiles, px, py, stack):
    global counter
    global maxi
    global t1
    counter +=1
    maxi = max(maxi,len(stack))
    if not counter % 10_000:
        t2 = time.perf_counter()
        print(counter//1000,' ', maxi, len(stack),' ',px,' ',py, f' TIME = {(t2-t1):.2f}')
        t1=t2

    if not 0<=px<len(mosaic) or not 0<=py<len(mosaic) or mosaic[px][py]:
        return False
    for tile in tiles:
        if tile not in stack:
            stack.append(tile)
            for shape in tile[2]:
                if fit(mosaic, shape, px,py):
                    mosaic[px][py] = (tile[0], shape)
                    if len(stack)==len(tiles):
                        return True
                    for d in dirc:
                        result = arrange(mosaic, tiles, px+d[0], py+d[1], stack)
                        if result:
                            return result
                    mosaic[px][py] = 0
            stack.pop()
    return False

data, test_data = load_data()
# uncomment the below line to use test data
#data = test_data

#part one

# [id, [lines], edges, edges_flipped]
tiles = parse_data(data)
edge_len = int(math.sqrt(len(tiles)))




mosaic = [[0 for _ in range(edge_len)] for _ in range(edge_len)]

t1 = time.perf_counter()
arrange(mosaic, tiles, 6, 6, [])

result1 = mosaic[0][0][0]\
        * mosaic[0][edge_len-1][0]\
        * mosaic[edge_len-1][0][0]\
        * mosaic[edge_len-1][edge_len-1][0]
print(f'result 1 = {result1}')

#part two 
t1 = time.perf_counter()

result2 = None

print(f'result 2 = {result2}')
t2 = time.perf_counter()
print(f'TIME = {(t2-t1):.2f}') 
