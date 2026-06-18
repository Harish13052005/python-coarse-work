# pattern 1
'''
def display(s, ind):
    if ind == len(s):
        return
    print(s[:ind+1])
    display(s, ind+1)
display("python", 0)
'''

#pattern 2
'''
def display(s,ind,l):
    if ind == len(s)-l+1:
        return
    print(s[ind:ind+l])
    display(s, ind+1,l)
display("python programming", 0, 10)
'''

# sum using recursion
'''
def display(l, ind):
    if ind == len(l):
        return 0
    return l[ind]+display(l, ind+1)
l = [1,2,3,5,76,5,4]
print(display(l,0))
'''

# counting Vowels
'''
def display(s, i):
    if i==len(s):
        return 0
    if s[i] in 'aeiouAEIOU':
        return 1+display(s, i+1)
    else:
        return display(s, i+1)

s = "python programming"
print(display(s, 0))
'''

# 
