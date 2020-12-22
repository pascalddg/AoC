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

rules = []
ticket = []
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
ticket = [int(x) for x in line.split(',')]

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


result2 =None
print(f'result 2 = {result2}')
t2 = time.perf_counter()
print(f'time = {(t2-t1):.2f}')
