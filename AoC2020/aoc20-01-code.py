def load_data():
	with open("aoc20-01-data.txt","r") as f:
	 	data = f.readlines()
	 	print("Loaded lines:", len(data))
	return data

data = load_data()

numbers = set()
for el in data:
    numbers.add(int(el))

for el in numbers:
    diff = 2020 - int(el)
    if diff in numbers:
        print (f'x:{el}, y:{diff}, mul = {el*diff}')

for el in numbers:
    for em in numbers:
        diff = 2020 - el - em
        if diff in numbers:
            print (f'x:{el}, y:{diff}, z:{em}, mul = {el*em*diff}')
