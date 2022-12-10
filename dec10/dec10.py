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
stack = []
while len(stack)>0 or instr_i<len(data):
#for _ in range(21):
    # start of cycle
#    print(stack)
    if count==0:
        if instr_i<len(data):
            instr = data[instr_i][0][:4]
            if instr=='noop':
#                stack.append([0,0])
                V=0
                count=1
            else:
                V = int(data[instr_i][0][5:])
#                stack.append([2, V])
                count=2

    i += 1
    count -= 1
#    print(i,count,X,i*X,V,ss)
    # middle of cycle
    if i in [20 + 40*k for k in range(6)]:
        ss += X*i
        print(i,X,i*X,ss)
#        print(stack)

    # end of cycle
    if count==0:
        X += V
        instr_i += 1

print(ss)
