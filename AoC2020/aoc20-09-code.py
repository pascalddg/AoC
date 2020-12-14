from collections import deque
test_data="""35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""

def load_data():
    with open("aoc20-09-data.txt", "r") as f:
        data = f.read().splitlines() 
    print("Loaded lines:", len(data))
    return data


data = load_data()
preamble = 25
# uncomment the below lines to work on the test data
#data = test_data.splitlines()
#preamble = 5

def is_sum(queue,val):
    for x, e1 in enumerate(queue):
        for y, e2 in enumerate(queue):
            if val == e1 + e2 and x!=y:
                return True
    return False

queue = deque()
idata = [int(x) for x in data]

for val in idata[:preamble]:
    queue.append(val)

for val in idata[preamble:]:
    if is_sum(queue,val):
        queue.append(val)
        queue.popleft()
    else:
        break

print(f'result = {val}')

x, y = 0, 1
total = idata[x]+idata[y]
while total!=val and y<len(idata):
    if total>val:
        total -= idata[x]
        x+=1
    else:
        y+=1
        total += idata[y]

if val==total:
    mini = min(idata[x:y+1])
    maxi = max(idata[x:y+1])
    print(f'mini={mini}, maxi={maxi}, result = {mini+maxi}')
else:
    print(f'ERR: x={x}, y={y}')
