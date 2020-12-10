def load_data():
	with open("aoc20-02-data.txt","r") as f:
	 	data = f.readlines()
	 	print("Loaded lines:", len(data))
	return data

data = load_data()

segment = []
counter = 0
counter2 = 0
for line in data:
    segment = line.strip().split(' ')
    mini, maxi = map(int, segment[0].split('-'))
    letter = segment[1][0]
    password = segment[2]
    x = password.count(letter) 
    if x>=mini and x<=maxi:
        counter +=1 

    tmp = password[mini-1] + password[maxi-1]
    if tmp.count(letter)==1:
        counter2 +=1

print(f'counter = {counter}')
print(f'counter2 = {counter2}')
