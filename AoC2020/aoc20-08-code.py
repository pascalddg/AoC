test_data="""nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
"""

def load_data():
    with open("aoc20-08-data.txt", "r") as f:
        data = f.read().splitlines() 
    print("Loaded lines:", len(data))
    return data

def cpu(prog):
    acc = 0
    pc = 0
    clock = 0        #this is just for fun
    tracer = set()

    halt = False
    while not halt:
        clock+=1

        instr = prog[pc][0]
        oldpc = pc
        oldacc = acc

        if instr == 'acc':
            acc += int(prog[pc][1])
            pc += 1
        elif instr == 'jmp':
            pc += int(prog[pc][1])
            #infinite loop detector
            if pc==oldpc:
                halt = True
                print('Err: Infinite loop.')
        elif instr == 'nop':
            pc += 1
        else:
            print(f'ERR, unknown instruction: {instr}')
            halt = True
        #loop detector
        if oldpc not in tracer:
            tracer.add(oldpc)    
        else:
            halt = True

        #end of program detector
        if pc == len(prog):
            halt = True

#    print(f'HALT: PC = {pc}, ACC = {acc}, oldPC = {oldpc}, oldACC = {oldacc}, INSTR = {instr}, CLOCK = {clock}')
    return acc, oldacc, pc

data = load_data()
# uncomment the below line to work on the test data
#data = test_data.splitlines()

program = [line.split(' ') for line in data]
acc, oldacc, pc = cpu(program)
print(f'{oldacc=}')

for line in program:
    if line[0] == 'nop':
        line[0] = 'jmp'
        acc, oldacc, pc = cpu(program)
        line[0] = 'nop'
    elif line[0] == 'jmp':
        line[0] = 'nop'
        acc, oldacc, pc = cpu(program)
        line[0] = 'jmp'
    if pc == len(program):
        print(f"\nSUCCESS: {acc}\n")
        break

