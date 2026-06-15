n = 11

#pattern A
'''
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or j==(n-1) or i==n//2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''

#pattern B
'''
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or j==(n-1) or i==n//2 or i==n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''

#pattern C
'''
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''

#pattern D
'''
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or j==n-1 or i==n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''

#pattern E
'''
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n//2 or i==n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''

#pattern F
'''
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n//2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''

#pattern G
'''
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or (i==n-1 and j<=n//2) or (j==n//2 and i>=n//2) or (i==n//2 and j>n//2) or (j==n-1 and i>n//2):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''

#pattern H
'''
for i in range(n):
    for j in range(n):
        if j==0 or j==(n-1) or i==n//2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''

#pattern I
'''
for i in range(n):
    for j in range(n):
        if i==0 or j==n//2 or i==n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''

#pattern J
'''
for i in range(n):
    for j in range(n):
        if i==0 or j==n//2 or (i==(n-1) and j<n//2) or (j==0 and i>n//2):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''


#pattern K
'''
for i in range(n):
    for j in range(n):
        if j == 0 or i + j == n//2 or i - j == n//2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''

#pattern L
'''
for i in range(n):
    for j in range(n):
        if j==0 or i==(n-1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''

# pattern M
'''
for i in range(n):
    for j in range(n):
        if j==0 or j==(n-1) or (i==j and j<=n//2) or (i + j == n-1 and i <= n//2):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''

#pattern N
'''
for i in range(n):
    for j in range(n):
        if j==0 or j==(n-1) or i==j:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''

#pattern O
'''
for i in range(n):
    for j in range(n):
        if (i==0 and 0<j<n-1) or (j==0 and 0<i<n-1) or (j==(n-1)and 0<i<n-1) or (i==n-1 and 0<j<n-1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''

#pattern P
'''
for i in range(n):
    for j in range(n):
        if j==0 or i==0 or i==n//2 or (j==n-1 and i<n//2):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''

#pattern Q
'''
for i in range(n):
    for j in range(n):
        if (i==0 and 0<j<n-1) or (j==0 and 0<i<n-1) or (j==(n-1)and 0<i<n-1) or (i==n-1 and 0<j<n-1) or (i==j and i >n//2):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''

#pattern R
'''
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n//2 or (j==n-1 and i<n//2) or (i==j and i>n//2):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''

#pattern S
'''
for i in range(n):
    for j in range(n):
        if (i==0 and j>0)  or (i==n-1 and j<n-1) or (i==n//2 and 0<j<n-1) or (j==0 and 0<i<n//2) or (j==n-1 and n//2<i<n-1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''

#pattern T
'''
for i in range(n):
    for j in range(n):
        if i==0 or j==n//2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''

#pattern U
'''
for i in range(n):
    for j in range(n):
        if (j==0 and i<n-1) or (i==n-1 and 0<j<n-1) or (j==n-1 and i<n-1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''

#pattern V
'''
for i in range(n):
    for j in range(n):
        if (j==0 and i<=n//2) or i-j==n//2 or (i+j==(n+n//2)-1) or (j==n-1 and i<=n//2):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''


#pattern W
'''
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or (i==j and i>=n//2) or (i+j==n-1 and i>n//2):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''

#pattern X
'''
for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''

#pattern Y
"""
for i in range(n):
    for j in range(n):
        if (i==j and i<=n//2)or (i+j==n-1 and i<n//2) or (j==n//2 and i>n//2) :
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
"""

#pattern Z

for i in range(n):
    for j in range(n):
        if  i==0 or i==n-1 or i+j==n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
