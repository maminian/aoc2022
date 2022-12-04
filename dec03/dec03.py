
import csv

with open('input', 'r') as f:
    rucksacks = list( csv.reader(f) )

def analyze_ruck(r):
    thing = r[0]
    n = len(thing)
    c0 = thing[:n//2]
    c1 = thing[n//2:]
    return intersection(c0,c1)

def intersection(a,b):
    '''
    Inputs a and b are expected as strings!
    '''
    output = []
    for ai in a:
        if (ai in b) and (ai not in output):
            output.append(ai)
    return output

def triintersection(a,b,c):
    return intersection( ''.join(intersection(a,b)), c)

def let2num(letter, shift=-96):
    return ord(letter) + shift + letter.isupper()*(ord('z')-ord('A')+1)

# part 1.
# Find the item type that appears in both 
# compartments of each rucksack. 
# What is the sum of the priorities of 
# those item types?
junk = [analyze_ruck(r) for r in rucksacks]

print( sum([sum([let2num(jii) for jii in ji]) for ji in junk]) )

# part 2. Find the badge for each triple of elves.
s=0
for i in range(0,len(rucksacks), 3):
    group = rucksacks[i:i+3]
    badge = triintersection(*[ri[0] for ri in group])[0]
    s += let2num(badge)

print(s)
