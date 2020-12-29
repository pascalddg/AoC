import time


test_data = """2 * 3 + (4 * 5)
5 + (8 * 3 + 9 + 3 * 4 * 3)
5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"""


def load_data():
    with open("AoC2020/aoc20-18-data.txt", "r") as f:
        data = f.read().splitlines() 
    print("Loaded lines:", len(data))
    return data


data = load_data()
# uncomment the below line to use test data
data = test_data.splitlines()

#part one

result1 = None
print(f'result 1 = {result1}')

#part two 
t1 = time.perf_counter()

result2 = None

print(f'result 2 = {result2}')
t2 = time.perf_counter()
print(f'TIME = {(t2-t1):.2f}') 
