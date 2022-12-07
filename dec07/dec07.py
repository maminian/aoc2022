'''
day 7...

filesystem.
'''
import csv
import re
from collections import UserDict

with open('input_mini', 'r') as f:
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
    def size(self, verbose=False, capture=False):
        s = 0
        chonks = {'self': 0}
        for k,v in self.items():
            if isinstance(v, Dir):
                chonk = v.size(verbose=verbose)
                if verbose:
                    print(k, chonk)
                if capture:
                    chonks[k] = chonk
                s += chonk
            elif isinstance(v, File):
                s += v.size
        if capture:
            return chonks
        else:
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

print(filesystem['/'].size(verbose=True, capture=True))
