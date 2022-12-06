import csv
import copy

with open('input', 'r') as f:
    csvr = csv.reader(f)
    data = list(csvr)[0][0]
#

def str_unique(string):
    '''
    returns a string with unique **letters* in the input.
    acaabaca -> acb
    '''
    out = ''
    for s in string:
        if s not in out:
            out += s
    return out

def detect_marker(string,T=4):
    n = len(string)
    for i in range(T,n):
        if len( str_unique(data[i-T:i]) ) == T:
            print(i, data[i-T:i])
            break
    return i

# part 1
print( 'part 1: ', detect_marker(data, 4) )
print( 'part 2: ', detect_marker(data, 14) )

