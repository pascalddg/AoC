from collections import defaultdict
import time
import itertools

test_data1 = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0"""

test_data = """mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1"""


def load_data():
    with open("aoc20-14-data.txt", "r") as f:
        data = f.read().splitlines() 
    print("Loaded lines:", len(data))
    return data


data = load_data()
# uncomment the below line to work on the test data
# data = test_data.splitlines()

mask_or = 0
mask_and = 0
mem = defaultdict(int)
for line in data:
    instr, param = line.split(' = ')
    if instr == 'mask':
        mask_or = int(param.replace('X','0'), base=2)
        mask_and = int(param.replace('X','1'), base=2)
    else:
        addr = int(instr[4:-1])
        value = int(param) | mask_or
        mem[addr] = value & mask_and

result = sum(mem.values())
print(f'result1 = {result}')

#part 2
t1 = time.perf_counter()

mem = defaultdict(int)
for line in data:
    instr, param = line.split(' = ')
    if instr == 'mask':
        mask_unchange = int(param.replace('1','X').replace('0','1').replace('X','0'), base=2)
        mask_override = int(param.replace('X','0'), base=2)
        # using lists instrad iterators for tracability
        floating_bits = [2**i for i, c in enumerate(reversed(param)) if c=='X']
        superpositions = [*itertools.product([0,1],repeat = len(floating_bits))]
        addreses = []
        for bits in superpositions:
            addr = 0
            for enabled, bit in zip(bits,floating_bits):
                if enabled:                
                    addr = addr | bit
            addreses.append(addr)
    else:
        addr = int(instr[4:-1])
        value = int(param)
        addr = addr & mask_unchange
        addr = addr | mask_override
        for option in addreses:
            addr_tmp = addr + option
            mem[addr_tmp] = value 

result2 = sum(mem.values())
print(f'result2 = {result2}')
t2 = time.perf_counter()
print(f'time = {(t2-t1):.2f}')
