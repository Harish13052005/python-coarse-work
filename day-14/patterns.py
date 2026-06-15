#pattern 1
'''
n = int(input("enter size:"))
if n%2==0:
    m = n//2
else:
    m = (n//2)+1
for i in range(n):
    if i<=m:
        for j in range(i+1):
            print("*", end=" ")
    else:
        for j in range(n-i):
            print('*', end=' ')
    print()
    
'''

'''
n = int(input())
m = n//2
for i in range(n):
    if i<=m:
        print('* '*(i+1), end=" ")
    else:
        print('* '*(n-i), end=" ")
    print()
'''

#pattern2
'''
n = int(input("enter the size:"))
m = n//2

for i in range(n):
    if i<=m:
        print('  '*(m-i), end=' ')
        print("* "*(i+1), end=" ")
    else:
        print('  '*(i-m), end=' ')
        print('* '*(n-i),end=' ')
    print()
'''
'''
n = int(input("enter the size:"))
m = n//2

for i in range(n):
    if i<=m:
        print(" "*(m-i) + "* "*(i+1), end=" ")
    else:
        print(" "*(i-m) + '* '*(n-i),end=' ')
    print()
'''

#pattern 3
'''
n = int(input("Enter size: "))

for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''

#pattern 4
'''
n = int(input("enter size:"))

for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1 or i==(n//2) or j==(n//2):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''

#pattern 5

'''
n = int(input("enter size:"))

for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n-1 or i==j or (i+j)==n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''

#pattern 6
