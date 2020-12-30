import time
import re
from functools import reduce
test_data = """0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb"""


def load_data():
    with open("AoC2020/aoc20-19-data.txt", "r") as f:
        data = f.read().splitlines() 
    print("Loaded lines:", len(data))
    return data

def build_regexp(rules, idx):
    rule = rules[idx]
    text = ''

    if rule[0] in "ab":
        return rule[0]
    for x in rule:
        if x == '|':
            text += '|'    
        else:
            text += build_regexp(rules, x)
    
    if '|' in rule:
        text = '('+text+')'
    return text    

def build_regexp2(rules, idx):
    rule = rules[idx]
    text = ''

    if rule[0] in "ab":
        return rule[0]
    for x in rule:
        if x == '|':
            text += '|'    
        else:
            text += build_regexp2(rules, x)
    
    if '|' in rule:
        text = '('+text+')'
    if idx in ('8'):
        text = '('+text+')+'
    return text    

data = load_data()
# uncomment the below line to use test data
#data = test_data.splitlines()

# using iterator to read the file in one pass
rules = {}
data_iter = iter(data)
for line in data_iter:
    if not len(line):
        break
    key, value = line.split(': ')
    rules[key] = value.replace('"','').split(' ')

messages = [line for line in data_iter]

#part one
regexp = build_regexp(rules,'0')
# print(regexp)
expr = re.compile('^'+regexp+'$')

counter = 0
# for line in messages:
#     print(int(expr.match(line)!=None))
#     if expr.match(line):
#         counter +=1
counter = reduce(lambda a,line: a+int(expr.match(line)!=None),messages,0)

result1 = counter
print(f'result 1 = {result1}')

#part two 
# rules['8'] = ['42','|','42','8']
# rules['11'] = ['42','31','|','42','11','31']
# rules['8'] = ['42','|','42','42','|','42','42','42']
rules['11'] = ['42','31','|','42','42','31','31','|','42','42','42','31','31','31','|','42','42','42','42','31','31','31','31']

regexp = build_regexp2(rules,'0')
# print(regexp)
expr = re.compile('^'+regexp+'$')

counter = 0
for line in messages:
    if expr.match(line):
        counter +=1

result2 = counter
print(f'result 2 = {result2}')
