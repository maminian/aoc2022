import csv
import re

def parse_listy_str(s, verbose=0):
    if verbose:
        print('start:', s)
    assert s[0]=='[' and s[-1]==']'
    thing = []
    flag=False
    l=1
    r=0
    nest = 0
#    for i,c in enumerate(s[1:]):
    while l<len(s)-1 and r<len(s):
        r += 1
        if r>len(s)-1:
#            thing.append(int(s[l:r]))
            return thing
        c = s[r]
        if c=='[':
            nest += 1
            continue
        if c==']':
            if nest==1:
                nested = s[l:r+1]
                if verbose:
                    print('here we go', nested)
                thing.append( parse_listy_str(nested, verbose=verbose) )
                l = r+2
                r = l+1
                if l>=len(s)-1 or r>=len(s):
                    return thing
            nest -=1
            continue
        if nest > 0:
            continue
        if c==',' or c==']':
            if verbose:
                print('appending...',l,r, s[l:r], s, end=' -> ')
            thing.append(int(s[l:r]))
            print(thing)
            l = r+1

#    print('mo',l,r,s,thing, nest)
#    thing.append( int(s[l:r]) )
    return thing

#####
tests = [
'[1,2,3,4]',
'[1,[2,3],4]',
'[1,[[2,5],[4,5],2],4]',
'[[1,1,0],2,0,[5,6]]',
'[[[2],3,[5,6]],0,1]'
]

for i,test in enumerate(tests):
    try:
        huh = parse_listy_str(test, verbose=0)
        print('passed ', i)
        print(test)
        print(huh)
    except:
        print('failed ', i)
        print(test)
        huh = parse_listy_str(test,verbose=1)



with open('input_mini', 'r') as f:
    lines = f.readlines()
    
