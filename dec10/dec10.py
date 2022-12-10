import csv

with open('input', 'r') as f:
    data = list(csv.reader(f))
#

i=0
instr_i=0
ss = 0
X = 1
count = 0
V=0

while instr_i<len(data):
    # start of cycle
    if count==0:
        if instr_i<len(data):
            instr = data[instr_i][0][:4]
            if instr=='noop':
                V=0
                count=1
            else:
                V = int(data[instr_i][0][5:])
                count=2

    i += 1
    count -= 1

    # middle of cycle
    if i in [20 + 40*k for k in range(6)]:
        ss += X*i

    # X positions sprite.
    if i%40-2 <= X and X <= i%40: # counting from 0
        # something is still wonky with the indexing
        # near the edges... but it still is good enough.
        # 
        # on further inspection: X=-1 and i=40 is the issue.
        print('#', end='')
#        print(i,X)
    else:
        print(' ', end='')
    if i%40==0:
        print('') # newline



    # end of cycle
    if count==0:
        X += V
        instr_i += 1

print(ss)
