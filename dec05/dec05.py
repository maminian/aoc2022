import csv
import copy

with open('input', 'r') as f:
    commands = []
    init = []
    switch = True
    
    csvr = csv.reader(f)
    for row in csvr:
        # phase 1.
        if switch:
            if len(row)==0:
                switch = False
            else:
                # oh no, not generalizable
                nstacks = len(row[0])//4+1
                init.append([row[0][1+4*i] for i in range(nstacks)])
        else:
        # phase 2.
            if len(row)==0:
                break
            commands.append(row[0])
    init = init[:-1]

def parse_command(cmd):
    s = cmd.split(' ')
    return [int(s[1]), int(s[3]), int(s[5])]

def execute_command(stacks,cmd, MODE=9000):
    if MODE==9000:
        for k in range(cmd[0]):
            a = stacks[cmd[1]-1].pop(-1)
            stacks[cmd[2]-1].append(a)
    elif MODE==9001:
        a = stacks[cmd[1]-1][-cmd[0]:]
        stacks[cmd[2]-1] = stacks[cmd[2]-1] + a
        stacks[cmd[1]-1] = stacks[cmd[1]-1][:-cmd[0]]
    return stacks

def pprint(stacks):
    for i,s in enumerate(stacks):
        print('%i --> '%(i+1), s)

#
stacks_orig = []
for i in range(nstacks):
    stack = []
    for j in range(len(init)-1, -1, -1):
        if init[j][i]!=' ':
            stack.append( init[j][i] )
    stacks_orig.append(stack)

#


# part 1: after rearrangement, 
# what crate is on the top of each stack?
def part1():
    stacks = copy.deepcopy(stacks_orig)
    for c in commands:
        stacks = execute_command(stacks, parse_command(c))

    print('Part 1: ', ''.join([s[-1] for s in stacks]) )

# part 2: after rearrangement using the 9001 instructions 
# (order of transferred stacks preserved),
# what crate is on the top of each stack?
def part2():
    stacks = copy.deepcopy(stacks_orig)
    for c in commands:
        stacks = execute_command(stacks, parse_command(c), MODE=9001)
    print('Part 2: ', ''.join([s[-1] for s in stacks]) )
#

part1()
part2()
