import csv

with open('input', 'r') as f:
    data = []
    for row in csv.reader(f):
        data.append( row[0].split(' ') )

# could probably build a scoring 
# matrix too... whatever
scoring = {
    'A' : {'X' : 1 + 3,
           'Y' : 2 + 6,
           'Z' : 3 + 0},
    'B' : {'X' : 1 + 0,
           'Y' : 2 + 3,
           'Z' : 3 + 6},
    'C' : {'X' : 1 + 6,
           'Y' : 2 + 0,
           'Z' : 3 + 3}
    }

strategy = {
    'A' : {'X' : 'Z', 
           'Y' : 'X',
           'Z' : 'Y'},
    'B' : {'X' : 'X', 
           'Y' : 'Y',
           'Z' : 'Z'},
    'C' : {'X' : 'Y', 
           'Y' : 'Z',
           'Z' : 'X'}
    }

# What would your total score be if 
# everything goes exactly according 
# to your strategy guide?
s1 = 0
for rps in data:
    s1 += scoring[rps[0]][rps[1]]
print(s1)

# What would your total score be 
# if X,Y,Z indicate how you're meant 
# to end the round?
s2 = 0
for rps in data:
    r = strategy[rps[0]][rps[1]]
    s2 += scoring[rps[0]][r]
print(s2)
