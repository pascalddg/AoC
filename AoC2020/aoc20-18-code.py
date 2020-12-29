import time
import math

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
# data = test_data.splitlines()


def calculator(tokens_iter):
    result = None
    operator = None
    for token in tokens_iter:
        if token=='(':
            value = calculator(tokens_iter)
        elif token==')':
            break
        elif token in '*+':
            operator = token
        else:
            value = int(token)
    
        if not result:
            result = value
            value = None
        elif value:
            if operator == '+':
                result = result + value
            elif operator == '*':
                result = result * value
            value = None
    return result


def calculator2(tokens_iter):
    stack = []
    operator = None
    
    for token in tokens_iter:
        if token=='(':
            value = calculator2(tokens_iter)
        elif token==')':
            break
        elif token in '*+':
            operator = token
        else:
            value = int(token)
        if not stack:
            stack.append(value)
            value = None
        elif value:
            if operator == '+':
                stack[-1] += value
            elif operator == '*':
                stack.append(operator)
                stack.append(value)
            value = None
    
    while len(stack)>1:
        value = stack.pop()
        operator = stack.pop()
        if operator=='*':
            stack[-1] *= value
    
    return stack.pop()


#part one
results = []
results2 = []
for line in data:
    tokens = line.replace('(','( ').replace(')',' )').split(' ')
    results.append(calculator(iter(tokens)))
    results2.append(calculator2(iter(tokens)))

result1 = sum(results)
print(f'result 1 = {result1}')

#part two 
result2 = sum(results2)

print(f'result 2 = {result2}')
