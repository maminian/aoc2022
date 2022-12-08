import csv
import numpy as np

with open('input', 'r') as f:
    huh = csv.reader(f)
    data = list(huh)
    data = np.array([[int(di) for di in d[0]] for d in data], dtype=int)


def scanx(arr, reverse=False):
    out = np.zeros(arr.shape, dtype=bool)

    if reverse:
        arr = arr[:,::-1]
    for i in range(out.shape[1]):
        out[:,i] = (i == np.argmax(arr[:,:i+1], axis=1))
    if reverse:
        out = out[:,::-1]
    return out
def scany(arr, reverse=False):
    out = np.zeros(arr.shape, dtype=bool)

    if reverse:
        arr = arr[::-1]
    for i in range(out.shape[0]):
        out[i,:] = (i == np.argmax(arr[:i+1,:], axis=0))
    if reverse:
        out = out[::-1,:]
    return out
#

def sweep(arr):
    left = scanx(data)
    right = scanx(data,True)
    top = scany(data)
    bottom = scany(data,True)
    return left + right + top + bottom
#

def eval_view(arr,i,j):
    # west
    views = np.zeros(4, dtype=int)
    for p in range(i-1,-1,-1):
        views[0] += 1
        if arr[p,j] >= arr[i,j]:
#            print(i,j,p,'l')
            break
    # east
    for p in range(i+1,arr.shape[0],1):
        views[1] += 1
        if arr[p,j] >= arr[i,j]:
#            print(i,j,p,'r')
            break
    # north
    for q in range(j-1,-1,-1):
        views[2] += 1
        if arr[i,q] >= arr[i,j]:
#            print(i,j,q,'n')
            break
    # south
    for q in range(j+1,arr.shape[1],1):
        views[3] += 1
        if arr[i,q] >= arr[i,j]:
#            print(i,j,q,'s')
            break
    return views

# part 1
vis = sweep(data)
print("visible trees: ",vis.sum())


# part 2: maximum viewing distance?
all_scores = np.zeros(data.shape, dtype=int)
for i in range(1,data.shape[0]-1):
    for j in range(1,data.shape[1]-1):
        views = eval_view(data,i,j)
#        print(i,j, views)
        all_scores[i,j] = views.prod()

best = np.argmax(all_scores)
best = np.unravel_index(best, all_scores.shape)
print('best spot: ', best, '; best score: ', all_scores[best])

