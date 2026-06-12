'''
s = 'python'
for i in range(len(s)):
    for j in range(i+1, len(s)):
        print(s[i],s[j],sep='', end=" ")
'''

#sum of nested lists
'''
l = [[1,2,3],[4,5,6],[7,8,9], [10,11,12], [13,14,15]]
s = 0
for i in l:
    for j in i:
        s+=j
print(s)
'''

#Account and pin
'''
d = {
    '1234':{'pin':'4567', 'balance':2345},
    '5677':{'pin':'8789', 'balance':5678},
    '5676':{'pin':'6565', 'balance':7679},
    '3436':{'pin':'3456', 'balance':3456},
    }

for i in d:
    print("Account number:",i)
    print("Pin Number:", d[i]['pin'])
'''

#Patterns
'''
for row in range(5):
    for col in range(5):
        print(col, end=" ")
    print()
'''

# stars
'''
n = int(input("enter the size:"))
for row in range(n):
    for col in range(n):
        print("*", end=" ")
    print()
'''

# pattern(0,1)
'''
n = int(input("enter the size:"))
for row in range(n):
    for col in range(n):
        print(col%2, end=" ")
    print()
'''

# pattern *
'''
n = int(input("enter the size:"))
for row in range(n):
    for col in range(row+1):
        print("*", end=" ")
    print()
'''

# pattern Left triangular
'''
n = int(input("enter the size"eeeeee))
for row in range(n):
    for col in range(n-row):
        print("*", end=" ")
    print()
'''

# pattern right
'''
n = int(input("enter the size:"))
for i in range(n+1):
    print(" "*(n-i), end=' ')
    print("*"*i)
'''
'''
n = int(input("enter size:"))
for row in range(n+1):
    for sp in range(n-row):
        print(" ", end=' ')
    for col in range(row):
        print("*", end=' ')
    print()
    '''
# pattern 7
'''
n = int(input("enter size:"))
for row in range(n):
    for sp in range(row):
        print(' ', end=' ')
    for col in range(n-row):
        print('*', end=' ')
    print()
'''

# pattern (0101)
'''
n = int(input("enter size:"))
for i in range(n):
    for j in range(n):
        print((i+j)%2, end=' ')
    print()
'''
# pattern 
n = int(input("enter the size:"))
c = 1
for i in range(n):
    for j in range(i+1):
        print(str(c).zfill(2),end=' ')
        c+=1
    print()
