import time

test_data = """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12"""


def load_data():
    with open("aoc20-16-data.txt", "r") as f:
        data = f.read().splitlines() 
    print("Loaded lines:", len(data))
    return data


data = load_data()
# uncomment the below line to work on the test data
#data = test_data.splitlines()

ranges = []
ticket = []
nearby_tickets = []

data_iter = iter(data)
for line in data_iter:
    if not len(line):
        break
    for range in line[line.find(':')+2:].split(' or '):
        beg,end = range.split('-')
        ranges.append((int(beg), int(end)))

next(data_iter)
line = next(data_iter)
ticket = [int(x) for x in line.split(',')]

next(data_iter)
next(data_iter)
for line in data_iter:
    numbers = [int(x) for x in line.split(',')]
    nearby_tickets.append(numbers)

print(f'{ranges=}')
print(f'{ticket=}')
print(f'{nearby_tickets=}')
invalids = []
for ticket in nearby_tickets:
    for number in ticket:
        valid = False
        for r in ranges:
            if r[0]<=number<=r[1]:
                valid = True
                break
        if not valid:
            invalids.append(number)

print(f'{invalids=}')

result = sum(invalids)
print(f'result 1 = {result}')

#part 2 TODO
t1 = time.perf_counter()


result2 =None
print(f'result 2 = {result2}')
t2 = time.perf_counter()
print(f'time = {(t2-t1):.2f}')
