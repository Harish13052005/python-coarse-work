'''
status = None
assert status != None, "you need to update the status"
print(status)
'''

#2
'''
name = 'abc'
batch = 55
age = None
assert (name!=None and batch!=None and age!=None), "You need to update the data"
print(name, batch, age)
'''

# while loop

i = 1
'''
while i<11:
    print(i)
    i+=1 
'''
'''
print("\n")
while i<21:
    print(i)
    i+=2
'''
'''
i = 10
while i > 0:
    print(i)
    i-=1
'''
#list
'''
l = [1,3,2,4,56,67,2]
i = 0
while i<len(l):
    print(l[i])
    i+=1
'''

#string
'''
l = "python programming"
i = 0
while i<len(l):
    print(l[i])
    i+=1
'''

#tuple
'''
l = (1,3,23,345,567678,7)
i = 0
while i<len(l):
    print(l[i])
    i+=1
'''

# remove zeros
'''
l = [1,2,3,0,4,0,6,9,0,3,5,7,9,0,4,6,8,0]
while 0 in l:
    l.remove(0)
print(l)
'''

# candycrush moves
moves = 30
while moves>1:
    status = input("[W]in or [C]ontinue:").upper()
    if status == 'W':
        print("you won the game")
        break

    moves -= 1
    print(f"{moves} moves are left")
else:
    print("Game Over")
    
