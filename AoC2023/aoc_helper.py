def load_data(day:int):
	with open(f'AoC2023/aoc23-{day:02d}.txt','r') as f:
		data = f.readlines()
		print("Loaded lines:", len(data))
	return data

