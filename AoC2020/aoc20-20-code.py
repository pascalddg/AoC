import time
import math
import numpy as np
from itertools import product
from collections import deque, defaultdict, namedtuple

#TODO #4 make 2nd part of the task

def load_data():
    with open("AoC2020/aoc20-20-data.txt", "r") as f:
        data = f.read()
    print("Loaded lines:", len(data.splitlines()))

    with open("AoC2020/aoc20-20-testdata.txt", "r") as f:
        testdata = f.read()
    print("Loaded lines:", len(testdata.splitlines()))
 
    return data, testdata


Shape = namedtuple('Shape',['N','E','S','W','arr'])

def make_shape(arr):
    # borders = [arr[:,0], arr[0,:], arr[:,9], arr[9,:]]
    borders = [arr[0,:], arr[:,9], arr[9,:], arr[:,0]]
    num_borders = []
    for b in borders:
        num = int(''.join(map(str,b)),2)
        num_borders.append(num)
    sh = Shape(*num_borders,np.copy(arr))
    return sh


def get_shapes(array):
  
    shapes = []
    arr = array
    for _ in range(2):
        for _ in range(4):
            shapes.append(make_shape(arr))
            arr = np.rot90(arr)
        arr = np.fliplr(arr)
        
    return tuple(shapes)


Tile = namedtuple('Tile',['id','array','shapes','edges'])

def parse_data(p_data):
    tiles = []     
    segments = data.split('\n\n')

    for segment in segments:
        header, pattern = segment.split(':\n')
        tile_id=int(header[5:])
        bin_list=list(pattern.replace('\n','').replace('#','1').replace('.','0'))
        arr = np.array(bin_list,dtype=np.int8).reshape(10,10)
        shapes=get_shapes(arr)
        edges = None
        tiles.append(Tile(tile_id, arr,shapes, edges))

    return tiles


def fit(mosaic, shape, px,py):
    if not 0<=px<len(mosaic) or not 0<=py<len(mosaic):
        return False

    if px>0 and mosaic[px-1][py]:
        if mosaic[px-1][py][1].E != shape.W:
            return False
    if px<len(mosaic)-1 and mosaic[px+1][py]:
        if mosaic[px+1][py][1].W != shape.E:
            return False
    if py>0 and mosaic[px][py-1]:
        if mosaic[px][py-1][1].N != shape.S:
            return False
    if py<len(mosaic)-1 and mosaic[px][py+1]:
        if mosaic[px][py+1][1].S != shape.N:
            return False

    return True


def dfs_helper(mosaic, graf, px, py, pstack, tile, edge_value):
    result = False
    matching_tiles = graf.get(edge_value)
    for item in matching_tiles.values():
        if item != tile:
            result = dfs(mosaic, graf, item, px, py, pstack)
    return result


def dfs(mosaic, graf, tile, px, py, pstack):

    if not 0<=px<len(mosaic) or not 0<=py<len(mosaic) or mosaic[px][py]:
        return False

    if tile not in pstack:
        pstack.append(tile)
        for shape in tile.shapes:
            if fit(mosaic, shape, px, py):
                mosaic[px][py] = (tile.id, shape)
                if len(pstack)==len(tiles):
                    return True

                result = False
                if px>0 and not mosaic[px-1][py]:
                    edge_value = shape.W
                    result = dfs_helper(mosaic, graf, px-1, py, pstack, tile, shape.W)
                elif px<len(mosaic)-1 and not mosaic[px+1][py]:
                    result = dfs_helper(mosaic, graf, px+1, py, pstack, tile, shape.E)
                elif py<len(mosaic)-1 and not mosaic[px][py+1]:
                    result = dfs_helper(mosaic, graf, px, py+1, pstack, tile, shape.N)
                # elif py>0 and not mosaic[px][py-1]:
                #     result = dfs_helper(mosaic, graf, px, py-1, pstack, tile, shape.S)

                if result:
                    return result

        pstack.pop()
    mosaic[px][py] = 0
    return False


data, test_data = load_data()
# uncomment the below line to use test data
# data = test_data

#part one

# [id, [lines], [shapes],[matching tiles]]
tiles = parse_data(data)
edge_len = int(math.sqrt(len(tiles)))

graf = defaultdict(dict)
for tile in tiles:
    for shape in tile.shapes:
        for ival in shape:
            #todo: iterates over different types. fixit
            if isinstance(ival,int):
                graf[ival][tile.id]=tile

mosaic = [[0 for _ in range(edge_len)] for _ in range(edge_len)]

found = False
for i,tile in enumerate(tiles):
    found = dfs(mosaic, graf, tile,0,0,[])
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
