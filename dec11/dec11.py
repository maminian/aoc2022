import re
import csv

with open('input', 'r') as f:
    raw = list(csv.reader(f, delimiter=':'))
    monkeys = []
    monkey = []
    
    for row in raw:
        if len(row)==0:
            monkeys.append(monkey)
            monkey = []
        else:
            monkey.append(row)
    monkeys.append(monkey)

class Monkey:
    def __init__(self, lines, worry_factor=3):
        
        self.id = lines[0][0].split(' ')[1]
        
        self.items = [int(i) for i in lines[1][1].strip().split(',')]
        
        update = lines[2][1].split(' ')
        self.op = self.sum if update[4]=='+' else self.prod
#        self.factor = int( update[5] )
        self.factor = ( update[5] )
        self.divisibility = int( lines[3][1].split(' ')[3] )
        self.m0 = int(lines[4][1].split(' ')[4])
        self.m1 = int(lines[5][1].split(' ')[4])
#        print()

        self.inspections = 0
        self.wf = worry_factor
        
        return
    
    def __str__(self):
        return ' '.join([str(z) for z in ['Monkey ', self.id, ': ', 'items: ',self.items]])
    def __repr__(self):
        return self.__str__()
        
    def turn(self):
        if len(self.items)==0:
            return []
        throwables = []
        for i in range(len(self.items)-1,-1,-1):
            # monkey operation
            if self.factor == 'old':
                self.items[i] = self.op(self.items[i], self.items[i])
            else:
                self.items[i] = self.op(self.items[i], int(self.factor))
            # worry go down
            self.items[i] = int( self.items[i]/self.wf )
            # monkey inspect worry for throwing
            a = self.items.pop(i)
            self.inspections += 1
            
            if (a) % (self.divisibility) == 0:
                throwables.append( (self.m0, a) )
            else:
                throwables.append( (self.m1, a) )
        return throwables
    
    def prod(self,a,b):
        return a*b
    def sum(self,a,b):
        return a+b

class Barrel:
    def __init__(self, monkeys, worry_factor=3):
        self.monkeys = [Monkey(m, worry_factor=worry_factor) for m in monkeys]
        factors = [m.divisibility for m in self.monkeys]
        
        self.rounds = 0
        self.lcm = 1 # not actually the least common multiple
        for f in factors:
            self.lcm *= f
            
        return
        
    def round(self):
        for j,m in enumerate(self.monkeys):
            thrown = m.turn()
            for i,w in thrown:
                self.monkeys[i].items.append(w % self.lcm)
        self.rounds += 1
        return
        
    def __str__(self):
        return '\n'.join(['-'*30 + '\nRound %5i\n'%self.rounds] + [m.__str__() for m in self.monkeys] + ['-'*30 + '\n'])
    def __repr__(self):
        return self.__str__()
        
    def monkeybusiness(self, verbose=False):
        p = 1
        counts = [m.inspections for m in self.monkeys]
        if verbose:
            print(counts)
        counts.sort()
        return counts[-1]*counts[-2]

############

#mon = Monkey(monkeys[0])

# part 1
print('part 1')
b = Barrel(monkeys)

for _ in range(20):
    b.round()

print(b)
p = b.monkeybusiness(True)
print(p)
print('')

# part 2
print('part 2')
b = Barrel(monkeys, worry_factor=1)

for i in range(10000):
    b.round()
print(b)
p = b.monkeybusiness(True)
print(p)

