'''
day 7...

filesystem.
'''
import csv
import re
from collections import UserDict

with open('input', 'r') as f:
    csvr = ( csv.reader(f) )
    data = list(csvr)
    data = [r[0] for r in data]

def contents(d, loc):
    s = d[loc[0]]
    if len(loc)>1:
        for l in loc[1:]:
            s = s.get(l)
            if s is None: break
    return s
def insert(d, loc, key, value):
    s = d[loc[0]]
    if len(loc)>1:
        for l in loc[1:]:
            s = s[l]
    s[key] = value
    return

class File:
    def __init__(self, size=0):
        self.size = size
    def __repr__(self):
        return "(file, size=%i)"%self.size
class Dir(dict):
    def __init__(self, *args):
        dict.__init__(self, *args)
    def size(self, verbose=False):
        s = 0
        chonks = {}
        for k,v in self.items():
            if isinstance(v, Dir):
                chonk = v.size(verbose=verbose)
                if verbose:
                    print(k, chonk)
                    cheater.append([k,chonk])
                s += chonk
            elif isinstance(v, File):
                s += v.size
        return s


filesystem = Dir()
location = []
mode = 'navigate'

for r in data:
#    print(r)
#    print(location)
#    print(mode)
    
    if re.match('\$ .*', r):
        mode = 'navigate'
    
    m = re.match('\$ cd \/', r)
    if m:
        # navigate home.
        location = ['/']
        if '/' not in filesystem.keys():
            filesystem['/'] = Dir({})
        continue
    
    m = re.match('\$ ls', r)
    if m:
        mode = 'list'
        continue
    
    m = re.match('\$ cd ([a-zA-Z0-9]{1,})', r)
    if m:
        # directory change; folder m.groups(0) exists.
        cd = m.groups(0)[0]
        thing = contents(filesystem, location)
        if cd not in thing:
            insert(filesystem, location, cd, Dir({}))
        location.append( cd )
        continue
    
    m = re.match('\$ cd \.\.', r)
    if m:
        # go one directory back from current position.
        location.pop(-1)
        continue
    
    if mode=='list':
        m = re.match('([0-9]{1,}) ([a-zA-Z0-9\.]{1,})', r)
        if m:
            g = m.groups(0)
            insert(filesystem, location, g[1], File(int(g[0])))
        continue

#

# part 1...

cheater = [] # global variable
que = filesystem.size(verbose=True)

s = 0
for c in cheater:
    if c[1]<100000:
        s += c[1]

print(s)

# part 2:
# find the smallest directory that can be deleted 
# such that 30000000 of 70000000 is available.
#
import numpy as np
sizes = np.array([c[1] for c in cheater])
o = np.argsort(sizes)

target = que - (70000000 - 30000000) # want just slightly larger than this
for i,oi in enumerate(o):
    if sizes[oi] >= target:
        print(oi)
        print(cheater[oi])
        break


