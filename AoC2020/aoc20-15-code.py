import time

data = (5,2,8,16,18,0,1)
#data = (0,3,6)

def mem_game(starting_numbers, max_turn):
    mem = {n:i+1 for i, n in enumerate(starting_numbers)}
    start_turn = len(mem)+1
    last = 0
    for turn in range(start_turn, max_turn):
        if last in mem:
            dist = turn - mem[last]
            mem[last]=turn
            last = dist
        else:
            mem[last]=turn
            last = 0
    return last

result1 = mem_game(data,2020)
print(f'result1 = {result1}')

#part 2
t1 = time.perf_counter()

result2 = mem_game(data,30_000_000)
print(f'result2 = {result2}')

t2 = time.perf_counter()
print(f'time = {(t2-t1):.2f}')
