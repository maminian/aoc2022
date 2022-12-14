import csv
import numpy as np
import itertools

import ugh

SHFT = 97

with open('input', 'r') as f:
    data = list(csv.reader(f))
    flags = [False,False]
    E = np.array([[ord(di)-SHFT if di==di.lower() else 0 for di in d[0]] for d in data])
    for i,row in enumerate(data):
        for j,letter in enumerate(row[0]):
            if letter=='E':
                FINISH = [i,j]
                E[FINISH[0], FINISH[1]] = 25
                flags[1] = True
            if letter=='S':
                START = [i,j]
                flags[0] = True
            if all(flags):
                break
        if all(flags):
            break
#

E2 = np.inf*np.ones( (E.shape[0]+2,E.shape[1]+2) )
E2[1:-1,1:-1] = E

START[0] = START[0] + 1
START[1] = START[1] + 1
FINISH[0] = FINISH[0] + 1
FINISH[1] = FINISH[1] + 1

#E2[5:-5,4:20] = np.inf

Ex = np.diff(E2, axis=0)
Ey = np.diff(E2, axis=1)


G = []
for i,j in itertools.product(range(1,E2.shape[0]-1), range(1,E2.shape[1]-1)):
    ind = i + j*E2.shape[0]
    if Ex[i,j] < 2:
        G.append([ind, ind+1])
    if Ex[i-1,j] < 2:
        G.append([ind, ind-1])
    if Ey[i,j] < 2:
        G.append([ind, ind+E2.shape[0]])
    if Ey[i,j-1] < 2:
        G.append([ind, ind-E2.shape[0]])
#
G = np.array(G)
N = E2.size
##

distances,path = ugh.dijkstra(G, N, ugh.ij2ind(*START,E2.shape[0]), ugh.ij2ind(*FINISH,E2.shape[0]))
#distances,path = ugh.dijkstra(G, 433, ugh.ij2ind(*FINISH,E2.shape[0]))

# supposed to be this..
FINISH_ind = ugh.ij2ind(*FINISH, E2.shape[0])
print('part 1...? ', distances[FINISH_ind])

############
if True:
    # the fun stuff
    from matplotlib import pyplot,ticker
    
    fig,ax = pyplot.subplots(1,2, sharex=True, sharey=True, constrained_layout=True, figsize=(7,6))

    ax[0].matshow(E2.T, cmap=pyplot.cm.terrain)
    ax[0].scatter(*START, marker='o', s=40, edgecolor='k', facecolor='w', label='elf')
    ax[0].scatter(*FINISH, marker='*', s=80, edgecolor='k', facecolor=[0,0,0,0], label='peak')
    ax[0].legend(loc='upper right')
#    ax[1].matshow(Ex.T < 2, cmap=pyplot.cm.Reds_r)
#    ax[2].matshow(Ey.T < 2, cmap=pyplot.cm.Blues_r)

    pairs = ugh.ind2ij(path, E2.shape[0])
#    ax[0].plot(pairs[:,0], pairs[:,1], c='r')
    obj = ax[1].matshow(np.reshape(distances, E2.shape[::-1]), cmap=pyplot.cm.gist_ncar)
#    fig.colorbar(obj)
    
    ax[1].scatter(*START, marker='o', s=40, edgecolor='k', facecolor='w', label='elf')
    ax[1].scatter(*FINISH, marker='*', s=80, edgecolor='k', facecolor=[0,0,0,0], label='peak')
    ax[1].legend(loc='upper right')
#    for k,g in enumerate(G):
#
#        pair = ugh.ind2ij(g, E2.shape[0])
#        ax[0].plot(pair[:,0], pair[:,1], c='r')

    ax[0].xaxis.set_major_locator(ticker.MultipleLocator(10))
    ax[0].yaxis.set_major_locator(ticker.MultipleLocator(10))
    ax[1].xaxis.set_major_locator(ticker.MultipleLocator(10))
    ax[1].yaxis.set_major_locator(ticker.MultipleLocator(10))
    
    ax[0].grid(c=[.5,0.5,0.5], lw=0.5)
    ax[1].grid(c=[.5,0.5,0.5], lw=0.5)
    
    fig.savefig('elf_mindist.png', bbox_inches='tight')
    fig.show()

