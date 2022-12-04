import csv

with open('input', 'r') as f:
    data = []
    for row in csv.reader(f):
        data.append( [[int(r) for r in col.split('-')] for col in row] )

def is_interval_subset(i1,i2):
    return (i2[0] <= i1[0]) and (i1[1] <= i2[1])

def intersection(list1,list2):
    output = []
    for i in list1:
        if i in list2:
            output.append(i)
    return output

def has_nonempty_intersection(i1,i2):
    l1 = list(range(i1[0], i1[1]+1))
    l2 = list(range(i2[0], i2[1]+1))
    huh = intersection(l1,l2)
    return len(intersection(l1,l2)) > 0

# part 1...
# In how many assignment pairs 
# does one range fully contain the other?
count1 = 0
for row in data:
    count1 += (is_interval_subset(row[0],row[1]) or is_interval_subset(row[1],row[0]))

print(count1)

# part 2...
# In how many assignment pairs do the ranges overlap?
count2 = 0
for row in data:
    count2 += has_nonempty_intersection(row[0], row[1])

print(count2)
