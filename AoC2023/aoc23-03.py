import re
import aoc_helper as ah
from functools import reduce
from collections import defaultdict
import math
raw_data = ah.load_data(3)

test_data = \
'''467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..'''.splitlines()


# test_data = \
# '''\
# .....#
# -234.#
# .....#
# '''.splitlines()



data = raw_data

def extend_data(data):
    edata = []
    for line in data:
        edata.append(line+'.')
    edata.append('.'*len(edata[0]))
    return edata

def check_surrounding(edata, yp, x_zero, xp):
    
    for i in range(x_zero-1,xp+1):
        c = edata[yp-1][i]
        if  c !='.' and not c.isdigit():
            return True
        c = edata[yp+1][i]
        if  c !='.' and not c.isdigit():
            return True

    c = edata[yp][x_zero-1]
    if c!='.' and not c.isdigit():
        return True

    c = edata[yp][xp]
    if c!='.' and not c.isdigit():
        return True
            
    return False


def star_1(data:list):
    edata = extend_data(data)
    numbers = []
    for y, line in enumerate(edata):
        digit = None
        for x, c in enumerate(line):
            if digit:
                if not c.isdigit():
                    if check_surrounding(edata, y, x_zero, x):
                        num = int(line[x_zero:x])
                        numbers.append(num)
                    digit = False
            else:
                digit=c.isdigit()
                x_zero = x

#    print(numbers)
#    print(f'{len(numbers) = }')
    return sum(numbers)



def star_2(data:list):
    edata = extend_data(data)
    cogs = tuple( (y,x) for y in range(len(edata)) for x in range(len(edata[0])) if edata[y][x] == '*')

    nums = defaultdict(list)
    for y, line in enumerate(edata):
        for obj in re.finditer(r'\d+', line):
            for j in (y-1, y, y+1):
                for i in range(obj.start()-1, obj.end()+1):
                    if (j, i) in cogs:
                        z = nums[(j, i)]
                        z.append(int(obj.group()))
#                        nums.get((j,i),[]).append(int(obj.group()))

    result = sum( math.prod(idx) for idx in nums.values() if len(idx)==2)
    return result



result_1t = star_1(test_data)
print(f'\n{result_1t = }')
result_1 = star_1(data)
print(f'\n{result_1 = }')
result_2t = star_2(test_data)
print(f'\n{result_2t = }')
result_2 = star_2(raw_data)
print(f'\n{result_2 = }')
