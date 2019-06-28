#!/anaconda3/bin/python

import random
import time

def create_dna(n, alphabet= 'acgt'):
    return ''.join([random.choice(alphabet) for i in range(n)])

dna = create_dna(1000000)

def count1(dna, base):
    i = 0
    for c in dna:
        if c == base:
            i += 1 
    return i

def count2(dna, base):
    i = 0 
    for j in range(len(dna)):
        if dna[j] == base:
            i += 1 
    return i 

def count3(dna, base):
    match = [c == base for c in dna]
    return sum(match)

def count4(dna, base):
    return dna.count(base)

def count5(dna, base):
    return len([i for i in range(len(dna)) if dna[i] == base])

def count6(dna,base):
    return sum(c == base for c in dna)

print(time.process_time())
print(count1(dna,'c'))
print(time.process_time())
print(count2(dna,'c'))
print(time.process_time())
print(count3(dna,'c'))
print(time.process_time())
print(count4(dna,'c'))
print(time.process_time())
print(count5(dna,'c'))
print(time.process_time())
print(count6(dna,'c'))
print(time.process_time())
