import time
import math
from itertools import product
from collections import deque, defaultdict

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

# [id, [lines], [shapes],[matching tiles]]
def parse_data(p_data):
    tiles = []
    tile=[0,[],[],[]]
    for line in data:
        if line.startswith("Tile"):
            tile[0]=int(line[5:-1])
        elif not line:
            tile[2]=get_shapes(tile)
            tiles.append(tile)
            tile=[0,[],[],[]]
        else:
            tile[1].append(line)
    if tile[0]:
        tile[2]=get_shapes(tile)
        tiles.append(tile)

    return tiles


def fit(mosaic, shape, px,py, len_mos):
    if not 0<=px<len_mos or not 0<=py<len_mos:
        return False

    if px>0 and mosaic[px-1][py]:
        if mosaic[px-1][py][1][1]!=shape[3]:
            return False
    if px<len_mos-1 and mosaic[px+1][py]:
        if mosaic[px+1][py][1][3]!=shape[1]:
            return False
    if py>0 and mosaic[px][py-1]:
        if mosaic[px][py-1][1][0]!=shape[2]:
            return False
    if py<len_mos-1 and mosaic[px][py+1]:
        if mosaic[px][py+1][1][2]!=shape[0]:
            return False

    return True

#dirc = ((-1,0),(1,0),(0,1),(0,-1))


def dfs(mosaic, graf, tile, px, py, stack, depth):

#    print(depth)
    
    if not 0<=px<len(mosaic) or not 0<=py<len(mosaic) or mosaic[px][py]:
        return False
    len_mos = len(mosaic)

    if tile not in stack:
        stack.append(tile)
        for shape in tile[2]:
            if fit(mosaic, shape, px, py, len_mos):
                mosaic[px][py] = (tile[0], shape)
                if len(stack)==len(tiles):
                    return True

                result = False
                if px>0 and not mosaic[px-1][py]:
                    edge_value = shape[3]
                    matching_tiles = graf.get(edge_value)
                    for i, item in enumerate(matching_tiles.values()):
                        if item != tile:
                            depth.append(1)
                            result = dfs(mosaic, graf, item, px-1, py, stack, depth)
                            depth.pop()
                    if result:
                        return result
                    continue

                if px<len(mosaic)-1 and not mosaic[px+1][py] and not result:
                    edge_value = shape[1]
                    matching_tiles = graf.get(edge_value)
                    for i, item in enumerate(matching_tiles.values()):
                        if item != tile:
                            depth.append(2)
                            result = dfs(mosaic, graf, item, px+1, py, stack, depth)
                            depth.pop()
                    if result:
                        return result
                    continue

                if py>0 and not mosaic[px][py-1] and not result:
                    edge_value = shape[2]                        
                    matching_tiles = graf.get(edge_value)
                    for i, item in enumerate(matching_tiles.values()):
                        if item != tile:
                            depth.append(3)
                            result = dfs(mosaic, graf, item, px, py-1, stack, depth)
                            depth.pop()
                    if result:
                        return result
                    continue

                if py<len(mosaic)-1 and not mosaic[px][py+1] and not result:
                    edge_value = shape[0]                        
                    matching_tiles = graf.get(edge_value)
                    for i, item in enumerate(matching_tiles.values()):
                        if item != tile:
                            depth.append(4)
                            result = dfs(mosaic, graf, item, px, py+1, stack, depth)
                            depth.pop()
                    if result:
                        return result
                    continue

        stack.pop()
    mosaic[px][py] = 0
    return False


data, test_data = load_data()
# uncomment the below line to use test data
#data = test_data

#part one

# [id, [lines], [shapes],[matching tiles]]
tiles = parse_data(data)
edge_len = int(math.sqrt(len(tiles)))

graf = defaultdict(dict)
for tile in tiles:
    for shape in tile[2]:
        for ival in shape:
            graf[ival][tile[0]]=tile

mosaic = [[0 for _ in range(edge_len)] for _ in range(edge_len)]

found = False
for i,tile in enumerate(tiles):
    found = dfs(mosaic, graf, tile,0,0,[], [i])
    if found:
        break
if found:
    result1 = mosaic[0][0][0]\
            * mosaic[0][edge_len-1][0]\
            * mosaic[edge_len-1][0][0]\
            * mosaic[edge_len-1][edge_len-1][0]
else:
    result1 = 'Not found.'
print(f'result 1 = {result1}')
if result1==13224049461431:
    print(' -=OK=- ')
else:
    print(' --err-- ')
#part two 
t1 = time.perf_counter()

result2 = None

#print(f'result 2 = {result2}')
t2 = time.perf_counter()
#print(f'TIME = {(t2-t1):.2f}') 
