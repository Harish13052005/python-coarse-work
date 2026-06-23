# sys module
'''

import sys

print(sys.argv)
print()
print(sys.path)
print()
print(sys.version)
print()

print("before exit")
sys.exit()
print("after exit")
'''

# platform module
'''
import platform

print(platform.system(), platform.release(), platform.processor())

'''

# math module
'''
import math

print(math.pi)
print(math.e)

print(math.sqrt(25))
print(math.pow(2,3))

print(math.ceil(12.3))
print(math.ceil(12.000001))
print(math.ceil(12.999999))
print(math.ceil(12.8))

print(math.floor(12.3))
print(math.floor(12.000001))
print(math.floor(12.999999))
print(math.floor(12.8))
'''
'''
import math

print(math.fabs(-12))
print(math.factorial(5))
print(math.gcd(8,28))

print(math.log(10,10))
print(math.sin(10))
print(math.cos(10))
print(math.tan(10))

print(math.degrees(20))
print(math.radians(20))
'''

# Random module
'''
import random
random.seed(3)

print(random.random())
print(random.randint(1,6))
print(random.uniform(1,6))
print()

l = ['python', 'Java', 'c', 'c++', 'html']
print(random.choice(l))
print(random.choices(l, k=3))

s='rps'
print(random.choices(s))

print(l)
random.shuffle(l)
print(l)
'''

# Collections
'''
import collections

s = 'python programming'
print(collections.Counter(s))
'''

''' regular method

s = 'python programming'

d = {}
for i in s:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print(d)
'''

'''
# default dict

import collections

s = 'python programming'
d = collections.defaultdict(int)

for i in s:
    d[i] += 1

print(d)
'''

# deque
'''
import collections

l = collections.deque([])

# M1

l.append(10)
l.append(20)
l.append(30)
l.append(40)
l.popleft()
l.popleft()
l.popleft()

l.append(50)
l.append(60)

l.popleft()

# M2

l.append(10)
l.append(20)
l.append(30)
l.append(40)
l.pop()
l.pop()
l.pop()

l.append(50)
l.append(60)

l.pop()

# M3

l.appendleft(10)
l.appendleft(20)
l.appendleft(30)
l.appendleft(40)
l.pop()
l.pop()
l.pop()

l.appendleft(50)
l.appendleft(60)

l.pop()

print(l)
'''

# itertools module
'''
from itertools import combinations, permutations

com = combinations('abcd', 2)
print([''.join(i) for i in com])
per = permutations('abcd', 2)
print([''.join(i) for i in per])
'''

