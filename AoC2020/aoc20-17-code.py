import time
import math

test_data = """.#.
..#
###"""


def load_data():
    with open("AoC2020/aoc20-17-data.txt", "r") as f:
        data = f.read().splitlines() 
    print("Loaded lines:", len(data))
    return data


data = load_data()
# uncomment the below line to work on the test data
#data = test_data.splitlines()

def count_neighbors(pocket_d,px,py,pz):
    counter = 0
    for x in range(px-1,px+2):
        for y in range(py-1,py+2):
            for z in range(pz-1,pz+2):
                if (x,y,z) in pocket_d and (x,y,z)!=(px,py,pz):
                    counter +=1
    return counter


def count_neighbors4d(p_pocket,px,py,pz,pw):
    counter = 0
    for x in range(px-1,px+2):
        for y in range(py-1,py+2):
            for z in range(pz-1,pz+2):
                for w in range(pw-1,pw+2):
                    if (x,y,z,w) in p_pocket and (x,y,z,w)!=(px,py,pz,pw):
                        counter +=1
    return counter


def calculate_minimaxi(pmini,pmaxi,x,y,z,w=None):
    rmini = [0] * len(pmini)
    rmaxi = [0] * len(pmaxi)
    rmini[0] = min(pmini[0],x)
    rmaxi[0] = max(pmaxi[0],x)
    rmini[1] = min(pmini[1],y)
    rmaxi[1] = max(pmaxi[1],y)
    rmini[2] = min(pmini[2],z)
    rmaxi[2] = max(pmaxi[2],z)
    if len(pmini)>3:
        rmini[3] = min(pmini[3],w)
        rmaxi[3] = max(pmaxi[3],w)
    return rmini, rmaxi

pocket = set()
mini = [0,0,0]
maxi = [0,0,0]
for x, line in enumerate(data):
    for y, c in enumerate(line):
        if c=='#':
            pocket.add((x,y,0))
            mini, maxi = calculate_minimaxi(mini,maxi,x,y,0)

for cycle in range(6):
    next_pocket = set()
    for x in range(mini[0]-1,maxi[0]+2):
        for y in range(mini[1]-1,maxi[1]+2):
            for z in range(mini[2]-1,maxi[2]+2):
                neighbors = count_neighbors(pocket,x,y,z)
                if neighbors == 3 or (neighbors==2 and (x,y,z) in pocket):
                    next_pocket.add((x,y,z))
                    mini, maxi = calculate_minimaxi(mini,maxi,x,y,z)

    pocket = next_pocket
    print(f'{cycle}: {len(pocket)}')


result = len(pocket)
print(f'result 1 = {result}')

#part two
t1 = time.perf_counter()
pocket = set()
mini = [0,0,0,0]
maxi = [0,0,0,0]
for x, line in enumerate(data):
    for y, c in enumerate(line):
        if c=='#':
            pocket.add((x,y,0,0))
            mini, maxi = calculate_minimaxi(mini,maxi,x,y,0,0)

for cycle in range(6):
    next_pocket = set()
    for x in range(mini[0]-1,maxi[0]+2):
        for y in range(mini[1]-1,maxi[1]+2):
            for z in range(mini[2]-1,maxi[2]+2):
                for w in range(mini[3]-1,maxi[3]+2):
                    neighbors = count_neighbors4d(pocket,x,y,z,w)
                    if neighbors == 3 or (neighbors==2 and (x,y,z,w) in pocket):
                        next_pocket.add((x,y,z,w))
                        mini, maxi = calculate_minimaxi(mini,maxi,x,y,z,w)

    pocket = next_pocket
    print(f'{cycle}: {len(pocket)}')


result2 = len(pocket)

print(f'result 2 = {result2}')
t2 = time.perf_counter()
print(f'time = {(t2-t1):.2f}') 