import numpy as np

def dijkstra(G,N,n0,nf):
    '''
    G: list of edges, assuming nodes numbered 0 to N-1, as an K-by-2 array.
    N: number of nodes
    n0: index of start
    nf: index of finish
    
    output: 
    P: list of nodes corresponding to shortest path sequence from n0 to nf.
    Entry 0 is n0; entry K is nf.
    '''
    
    # build dict; keys are nodes, values are lists of neighbors.
#    n = np.max(G)+1
    duh = {i:[] for i in range(N)}
    for e in G:
        if e[1] not in duh[e[0]]:
            duh[e[0]].append(e[1])
        if e[0] not in duh[e[1]]:
            duh[e[1]].append(e[0])
    D = np.inf*np.ones(N)
    
    import pdb
#    pdb.set_trace()
    
    D[n0] = 0
    curr = int(n0)
    path = []
    unvisited = [i for i in range(N)]
    for i in range(N):
        curr = unvisited[ np.nanargmin(D[unvisited]) ]
        unvisited.remove(curr)

        nbrs = duh[curr]
        for nbr in nbrs:
            if nbr in unvisited:
                if D[curr]+1 < D[nbr]:
                    D[nbr] = D[curr] + 1
                    path.append([nbr,curr])
                    if nbr==nf:
                        print('whoopee')
                        break
#        path.append(curr)

#        print(len(visited), len(np.unique(visited)),len(subset))

    return D,path

def ij2ind(i,j,m):
    return i + j*m
    
def ind2ij(ind, m):
    '''m: rows'''
    if hasattr(ind,'__iter__'):
        return np.array([ind2ij(indi, m) for indi in ind])
    i,j = ind%m, int(ind//m)
    return i,j
