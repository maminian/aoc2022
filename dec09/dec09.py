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

KNOTS = 10
pos = np.zeros((KNOTS,2), dtype=int)
visited = {tuple(pos[-1])}
for move in data:
    c,l = move[0].split(' ')
    for i in range(int(l)):
        pos[0] += m[c]
        for k in range(1,pos.shape[0]):
            if d(pos[k-1], pos[k])>1:
                pos[k] += v(pos[k], pos[k-1])
        visited.add(tuple(pos[-1])) # keep track of where we've visited

print('tail visited this many sites: ', len(visited))

