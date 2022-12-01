'''

elves sacks with items with calories
one number per line
separation by blank line

''' 
import csv

with open('input', 'r') as f:
    csvr = csv.reader(f)
    data = list(csvr)

containers = []
bag = []
for d in data:
    if len(d)==0:
        containers.append(bag)
        bag = []
    else:
        bag.append( int(d[0]) )
containers.append(bag)

# part 1: maximum calories in a bag?
maxcal = 0
for bag in containers:
    maxcal = max(maxcal, sum(bag))

print(maxcal)

# part 2: largest three calorie holders and the sum of their bags' calories?
# order, and who has what, doesn't matter!
K = 3
candidates = [sum(containers[i]) for i in range(K)]
candidates.sort(reverse=True)

for i in range(K,len(containers)):
    s = sum(containers[i])
    for j in range(len(candidates)):
        if s > candidates[j]:
            candidates[j+1:] = candidates[j:-1]
            candidates[j] = s
            break

print(sum(candidates))


