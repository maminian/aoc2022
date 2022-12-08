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

vis = sweep(data)
#print(data)
#print(vis)
print("visible trees: ",vis.sum())
