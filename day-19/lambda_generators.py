# lambda with dict updation
'''
d = {'sugar':40, 'salt':20, 'cooking oil':80, 'chili':60}

res = dict(map(lambda i: (i[0], i[1]+i[1]*0.18), d.items()))
res1 = dict(map(lambda i: (i[0], i[1]-i[1]*0.5), d.items()))

print(res)
print(res1)
'''

# lambda with filter
'''
d = {'sugar':40, 'salt':20, 'cooking oil':80, 'chili':60}

res = dict(filter(lambda i: i[1]>50, d.items()))
res1 = dict(filter(lambda i: i[1]<50, d.items()))

print(res)
print(res1)
'''

# List comprehension
'''
res1=[]

#regular method
for i in range(1,11):
    res1.append(i)
# comprehension method
res2=[i for i in range(1,10)]

print(res1)
print(res2)
'''

'''
res3 = []
for in in range(3, 31, 3):
    res3.append(i)
print(res3)
'''
# comprehension for 3 multiple
'''
res4 = [i for i in range(3, 31, 3)]
print(res4)

'''
'''
res5 = []
for i in range(2, 51, 2):
    res5.append(i)
print(res5)
'''
# even numbers
'''
res6 = [i for i in range(2, 51, 2)]
print(res6)
'''

# simple if list comprehension
'''
s = 'python programming'
l=[]
for i in  s:
    if i in 'aeiouAEIOU':
        l.append(i)
print(l)

# comprehensed

l1 = [i for i in s if i in 'aeiouAEIOU']
print(l1)
        
'''

# if else
'''
a = [1,2,3,4,57,8,535,56,78,89,7]
l1=[]
for i in a:
    if i%2==0:
        l1.append(i)
    else:
        l1.append(0)
print(l1)
'''
# comprehensed
'''
l2 = [i if i%2==0 else 0 for i in a]

print(l2)
'''
# taking input into iist
'''
n = int(input())
l1 = [int(input()) for i in range(n)]
print(l1)
'''

# nested loops
'''
l = []
for i in range(3):
    for j in range(1,4):
        l.append(j)
print(l)

# comprehensed

l1 = [j for i in range(3) for j in range(1,4)]
print(l1)
'''

#NL-2
'''
l = []
for i in range(3):
    temp = []
    for j in range(1,4):
        temp.append(j)
    l.append(temp)
print(l)
'''
# comprehensed
'''
l1 = [[j for j in range(1,4)] for i in range(3)]
print(l1)
'''

# set comprehension
'''
s = set()
for i in range(1,11):
    s.add(i)
print(s)
'''
# comprehensed
'''
s1 =  {i for i in range(1,11)}
print(s1)
'''

# dictionary comprehension
'''
d1 = {}
for i in range(1,11):
    d1[i] = i*i
print(d1)
'''
# comprehensed
'''
d2 = { i : i*i for i in range(1,11)}
print(d2)
'''

# dict with names and marks
'''
d={}
n = int(input())
for i in range(n):
    name = input("enter the name")
    marks = int(input("enter the marks"))
    d[name]=marks
print(d)
'''
# comprehensed
'''
n = int(input())
res = {input("enter the name:"): int(input("enter marks:")) for i in range(n)}
print(res)
'''

# GENERATORS

def display():
    l = ['1..50', '51..100', '101..150', '151..200']
    yield l[0]
    yield l[1]
    yield l[2]
    yield l[3]

scroll = display()

print(next(scroll))
print(next(scroll))
print(next(scroll))
print(next(scroll))

    
