import aoc_helper as ah
data = ah.load_data(1)
test_data = \
'''two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen'''.splitlines()

result1 = 0
for line in data:
    a, b, c = 0, 0, 0  
    for a in line:
        if a.isdigit():
            break
    for b in line[::-1]:
        if b.isdigit():
            break
    c = int(a+b)
    result1 += c
print(f'{result1 = }')

words = ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
def what_digit(token):
    if token[0].isdigit():
        return int(token[0])
    for i, w in enumerate(words,start=1):
        if token.startswith(w):
            return i
    return -1 

result2 = 0    
#data= test_data
for line in data:
    
    for x in range(len(line)):
        if (a:=what_digit(line[x:]))>0 :
            break
    for x in range(len(line)-1, -1, -1):
        if (b:=what_digit(line[x:]))>0 :
            break
    c = int(a*10+b)
    result2 += c
print(f'{result2 = }')
