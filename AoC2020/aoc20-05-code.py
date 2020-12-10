import math


def load_data():
    with open("aoc20-05-data.txt", "r") as f:
        data = f.read().splitlines()  # read file and removes end of line character
    print("Loaded lines:", len(data))
    return data

data = load_data()

counter = 0
print(f'{counter=}')

maxseat = 0
seats = set()
for boarding_pass in data:
    #instead checking rows and columns separately lets search by seat number
    low, high = 0, 128*8-1
    mid = low + (high-low)//2
    for letter in boarding_pass:
        if letter=='B' or letter=='R':
            low=mid+1
        else:
            high=mid
        mid = low + (high-low)//2

    maxseat = max(maxseat,mid)
    seats.add(mid)

print(f'{maxseat=}')

for i in range(1,128*8-1):
    if i not in seats and i-1 in seats and i+1 in seats:
        print(f'myseat = {i}')
