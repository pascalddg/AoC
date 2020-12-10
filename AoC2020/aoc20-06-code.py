import math


def load_data():
    with open("aoc20-06-data.txt", "r") as f:
        data = f.read() 
    print("Loaded lines:", len(data))
    return data

data = load_data()

records = data.strip().replace('\n\n','|').replace('\n',' ').split('|')
base = set("abcdefghijklmnopqrstuvwxyz")
# base is used here to revmove spaces from the other sets
uniques = [len(base.intersection(set(group))) for group in records]
print(f'uniques = {sum(uniques)}')

commons=[]
# base is used here as starting set for the intersection
for group in records:
    commons.append(len(base.intersection(*[set(s) for s in group.split(' ')])))

print(f'commons = {sum(commons)}')

