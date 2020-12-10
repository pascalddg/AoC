import re

def load_data():
    with open("aoc20-04-data.txt", "r") as f:
        data = f.read().splitlines()  # read file and removes end of line character
    print("Loaded lines:", len(data))
    return data

def check_passport(passport:dict):
    try:
        for key, value in passport.items():
            if key=='byr':
                if not(1920<=int(value)<=2002):
                    return False
            elif key=='iyr':
                if not(2010<=int(value)<=2020):
                    return False
            elif key=='eyr':
                if not(2020<=int(value)<=2030):
                    return False
            elif key=='hgt':
                if value.endswith('cm'):
                    if  not( 150<=int(value[:-2])<=193):
                        return False
                else:
                    if  not( 59<=int(value[:-2])<=76):
                        return False
            elif key=='hcl':
                expr = re.compile('^#([0-9a-fA-F]{6})$')
                if not expr.match(value):
                    return False
            elif key=='ecl':
                colors = {'amb','blu','brn','gry','grn','hzl','oth'}
                if value not in colors:
                    return False
                pass
            elif key=='pid':
                expr = re.compile('^[0-9]{9}$')
                if not expr.match(value):
                    return False
    except ValueError:
        print(f'Error {key}:{value}')
        return False
    return True

data = load_data()
data.append('')

documents = []
passport = {}
dif=[]
counter = 0
for line in data:
    if len(line) > 0:
        elements = line.split(' ')
        for field in elements:
            key,value = field.split(':')
            passport[key] = value
    else:
        if len(passport)==8 or (len(passport)==7 and 'cid' not in passport):
            counter +=1
            documents.append(passport)
        else:
            dif.append(passport.get('byr'))
        passport = {}

counter2 = sum((check_passport(passport) for passport in documents))

print(f'Counter = {counter}')
print(f'Documents = {len(documents)}')
print(f'Counter2 = {counter2}')
print(dif)


