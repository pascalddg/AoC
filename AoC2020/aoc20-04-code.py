import re

def load_data():
    with open("aoc20-04-data.txt", "r") as f:
        data = f.read() 
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
# 1. remove whitespaces at the end of file
# 2. replace empty line with record separator
# 3. replace remaining endline characters with space - field separator
# 4. create list of records
records = data.strip().replace('\n\n','|').replace('\n',' ').split('|')

documents = []

# part one
for line in records:
    passport = {keyval[:3]:keyval[4:] for keyval in line.split(' ') if keyval[:3]!='cid'}
    if len(passport)==7:
        documents.append(passport)

#part two
counter2 = sum((check_passport(passport) for passport in documents))

print(f'counter1 = {len(documents)}')
print(f'Counter2 = {counter2}')



