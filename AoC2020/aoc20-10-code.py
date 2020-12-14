from collections import deque
test_data="""28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""

test_data2 = """16
10
15
5
1
11
7
19
6
12
4"""

def load_data():
    with open("aoc20-10-data.txt", "r") as f:
        data = f.read().splitlines() 
    print("Loaded lines:", len(data))
    return data

def count_ways(table, x=0, cache={}):
    if x in cache:
        return cache[x]
    if x==len(table)-1:
        return 1
    counter = 0
    for i in range(1,4):
        if x+i<len(table) and table[x+i]-table[x]<=3:
            counter += count_ways(table, x+i, cache)
    cache[x] = counter
    return counter

data = load_data()
# uncomment the below line to work on the test data
#data = test_data.splitlines()

idata = [int(x) for x in data]
idata.append(max(idata)+3)
idata.append(0)
idata.sort()
diffs = [idata[x+1]-idata[x] for x in range(len(idata)-1)]
unos = diffs.count(1)
tres = diffs.count(3)

print(f'{unos=} {tres=}  result1 = {unos*tres}')

print(f'result2 = {count_ways(idata)}')

