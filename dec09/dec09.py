import csv
import numpy as np

with open('input', 'r') as f:
    data = list(csv.reader(f))
    
#

m = {
    'R': np.array([1,0]),
    'U': np.array([0,1]),
    'D': np.array([0,-1]),
    'L': np.array([-1,0])
}

def d(x,y):
    return np.linalg.norm(x-y, np.inf)
def v(x,y):
    '''FROM x TO y'''
    return np.sign(y-x)

hp, tp = np.zeros((2,2), dtype=int)
visited = {tuple(tp)}
for move in data:
    c,l = move[0].split(' ')
    for i in range(int(l)):
        hp += m[c]
        if d(hp,tp)>1:
            tp += v(tp,hp)
            visited.add(tuple(tp)) # keep track of where we've visited

print('tail visited this many sites: ', len(visited))
