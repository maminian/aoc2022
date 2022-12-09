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

def snakey(moves, KNOTS=2, track=True, history=False):
    '''
    simulates knot (snake) of length n 
    where the head moves according to the 
    moves provided (puzzle input) and 
    middle sections follow according to 
    rules described (if max norm > 1 then 
    move in a signed direction towards previous knot)
    '''
    import numpy as np
    import copy
    
    pos = np.zeros((KNOTS,2), dtype=int)
    if track:
        visited = {tuple(pos[-1])}
    if history: 
#        poss = np.zeros((len(moves)+1, KNOTS,2), dtype=int)
        poss = []
    for i,move in enumerate(data):
        c,l = move[0].split(' ')
        for i in range(int(l)):
            pos[0] += m[c]
            if history:
                poss.append(pos.copy())
            for k in range(1,pos.shape[0]):
                if d(pos[k-1], pos[k])>1:
                    pos[k] += v(pos[k], pos[k-1])
                    if history:
                        poss.append(pos.copy())
            if track:
                # keep track of unique places visited
                visited.add(tuple(pos[-1]))
#        if history:
#            poss[i+1] = pos
    if track:
        print('tail visited this many sites: ', len(visited))
    if history:
        return np.array(poss)
    else:
        return None
#

# part 1
snakey(data)
# part 2
snakey(data, KNOTS=10)

###########

# thisiswherethefunbegins.mp4
from matplotlib import pyplot
from matplotlib import ticker
import cmocean

import os

pyplot.style.use('dark_background')

if not os.path.exists('frames/'):
    os.mkdir('frames')

T = 360
KNOTS = 10
cream = np.array([1,1,0.85,1]) 

poss = snakey(data, KNOTS=KNOTS, history=True, track=False)

xl,xr = [np.floor(poss[:T,:,0].min()/5)*5, np.ceil(poss[:T,:,0].max()/5)*5]
yl,yr = [np.floor(poss[:T,:,1].min()/5)*5, np.ceil(poss[:T,:,1].max()/5)*5]

dx = xr-xl
dy = yr-yl
ss = max(dx,dy)

#edgecolors = pyplot.cm.rainbow(np.linspace(0,1,KNOTS))
sectioncolors = cmocean.cm.deep_r(np.linspace(0,1,KNOTS))
edgecolors = 0.4*cream + 0.6*sectioncolors

fig,ax = pyplot.subplots(constrained_layout=True, figsize=(dx/ss*7, 1.04*dy/ss*7))

ax.set_xlim([xl,xr])
ax.set_ylim([yl,yr])
ax.set_aspect('equal')

ax.set_xticklabels([])
ax.set_yticklabels([])
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))

ax.grid(which='major', lw=1.5, zorder=-1000)
ax.grid(which='minor', lw=0.25, zorder=-1000)


for i in range(T):
    if i>0:
        collection.remove()
        connection[0].remove()
    # for zorder reasons, need to scatter in reverse order.
    collection = ax.scatter(poss[i][::-1,0], poss[i][::-1,1], 
        marker='o', 
        s=200, 
        facecolor=sectioncolors[::-1],
        edgecolor=edgecolors[::-1], lw=2,
        alpha=1,
        zorder=1000
    )
    
    connection = ax.plot(poss[i][:,0], poss[i][:,1], lw=3, c=cream, zorder=-100)
    ax.yaxis.set_inverted(True)
    fig.savefig( os.path.join('frames', 'frame_%04d.png'%i))

