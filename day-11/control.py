# control ststements: str, list, tuple, set, dict, range()
''' for var in seq:
        print(var)
'''

#str
'''
s = "python programming"
for ch in s :
    print(ch)
'''

# List
'''
l = [1,2,3,4,5,6]
for i in l:
    print(i)
'''

# Tuple
'''
T = ("abc", 123, "kits", 456)
for i in T:
    print(i)
'''

# Set
'''
S = {"a", 2, "b", 4}
for i in S:
    print(i)
'''

# Dictionary
'''
D = {"a":1, "b":2, "c":[3,4,5]}
for i in D:
  # print(i)
    print(i, D[i])
'''

# Range
'''
for i in range(1,11):
    print(i)
print("ok next")
for i in range(2,51,2):
    print(i)
print("ok next")
for i in range(5,101,5):
    print(i)
print("ok next")
for i in range(20,0,-1):
    print(i)
print("ok next")
for i in range(30,0,-3):
    print(i)
print("ok next")
for i in range(6):
    print(i)
'''
'''
s = 'looping statement'

for i in range(len(s)):
    print(i)
    print(i, s[i])
print("ok next")

l = [7,2,4,3,5,6,7]
for i in range(len(l)):
    print(i)
    print(i, l[i])
print("ok next")

t = (2,4,4,6,7,8,3)
for i in range(len(t)):
    print(i)
    print(i,t[i])
'''
# using enumerate
'''
print("using enumerate")
s = 'looping'
for i in enumerate(s):
    print(i)
    print(i[0], i[1])
print("ok next")

l = [2,4,5,78,5,2,4,5]
for i in enumerate(l):
    print(i)
    print(i[0], i[1])
print("ok next")

t = (2,4,5,78,5,2,4,5)
for i in enumerate(t):
    print(i)
    print(i[0], i[1])
print("ok next")

k = {2,4,5,78,5,2,4,5}
for i in enumerate(k):
    print(i)
    print(i[0], i[1])
'''

# pass, break and continue
'''
print("pass")
print("for an empty block of code \n")
for i in range(10):
    pass
print("break")
for i in range(10):
    if i==5:
        break
    print(i)
print("continue")
for i in range(10):
    if i==5:
        continue
    print(i)
'''

# Class room Task
'''
s = 'looping ststement'
for i in s:
    if i in "aeiouAEIOU":
        print(i)
'''
# for printing even numers
'''
l = [23,45,23,56,78,34,6,78,2,56]
for i in l:
    if i%2==0:
        print(i)
'''

# using dictionary
'''
d = {'laptops':4, 'mobiles':3, 'chargers':0, 'mouse':6, 'tab':2}
for i in d:
    if d[i]:
        print(i)
'''

# item X index
'''
t = (1,2,4,5,6,8,8)
for i in range(len(t)):
    print(i*t[i])
'''

#converting elements of the set into upper case

names = {'subbu','naresh','dinesh','rishi'}
for i in names:
    print(i.upper())
