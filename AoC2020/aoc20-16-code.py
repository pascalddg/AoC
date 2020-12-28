import time
import math

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
    with open("AoC2020/aoc20-16-data.txt", "r") as f:
        data = f.read().splitlines() 
    print("Loaded lines:", len(data))
    return data


data = load_data()
# uncomment the below line to work on the test data
#data = test_data.splitlines()

rules = []
my_ticket = []
nearby_tickets = []

data_iter = iter(data)
for line in data_iter:
    if not len(line):
        break
    name, ranges = line.split(': ')
    rtx1, rtx2 = ranges.split(' or ')
    ra = tuple(map(int, rtx1.split('-')))
    rb = tuple(map(int, rtx2.split('-')))
    rules.append((name, ra, rb))

next(data_iter)
line = next(data_iter)
my_ticket = [int(x) for x in line.split(',')]

next(data_iter)
next(data_iter)
for line in data_iter:
    numbers = [int(x) for x in line.split(',')]
    nearby_tickets.append(numbers)

invalids = []
valid_tickets = []
for ticket in nearby_tickets:
    is_ticket_valid = True
    for number in ticket:
        valid_number = False
        for name, ra, rb in rules:
            if ra[0]<=number<=ra[1] or rb[0]<=number<=rb[1]:
                valid_number = True
                break
        if not valid_number:
            invalids.append(number)
            is_ticket_valid = False
    if is_ticket_valid:
        valid_tickets.append(ticket)

print(f'nearby_tickets = {len(nearby_tickets)}')
print(f'valid_tickets = {len(valid_tickets)}')

result = sum(invalids)
print(f'result 1 = {result}')

#part 2 TODO
t1 = time.perf_counter()

fields  = []
for i in range(len(my_ticket)):
    fields.append((i, [name for name, _, _ in rules]))

for name, ra, rb in rules:
    for n_idx in range(len(my_ticket)):
        for t_idx in range(len(valid_tickets)):
            number = valid_tickets[t_idx][n_idx]
            if not (ra[0]<=number<=ra[1] or rb[0]<=number<=rb[1]):
                fields[n_idx][1].remove(name)
                break
fields.sort(key = lambda x:len(x[1]))

for i, field in enumerate(fields):
    for field_2 in fields[i+1:]:
        if len(field_2[1])<=1:
            print('\nERROR\n')
        elif field[1][0] in field_2[1]:
            field_2[1].remove(field[1][0])

departures = []
for idx, name in fields:
    if name[0].startswith('departure'):
        departures.append(my_ticket[idx])
        print (idx,' ', name[0], ' ', my_ticket[idx])
print(departures)

result2 = math.prod(departures)
print(f'result 2 = {result2}')
t2 = time.perf_counter()
print(f'time = {(t2-t1):.2f}') 