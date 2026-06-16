# Local Scope
'''
def display():
    n=10
    print("Inside:", n)

display()
'''
'''
def display():
    n=10
    print("Inside:", n)

display()
print("Outside: ", n)
'''

# Global Scope
'''
n = 10
def display():
    print("Inside:", n)
display()
print("Outside:", n)
'''

'''
def display():
    global n
    n = 10
    print("Inside:", n)
display()
print("Outside:", n)
'''

'''
def display():
    global n
    n += 10
    print("Inside:", n)

n = 10
display()
print("Outside:", n)
'''

# commenting global
'''
def display():
    n += 10
    print("Inside:", n)

n = 10
print("Outside:", n)
display(n)
'''

# using nonlocal
'''
def outer():
    n=10
    def inner():
        nonlocal n
        n += 10
        print("inner function:", n)
    inner()

    print("Outer function:")
'''

# functions -> variables
'''
s = 'python'
print(len(s))               # whenever a function is used as as variable,
                        # then  it loses its properties and acts as a variiable
len = 5
print(len(s))
'''

# passing datatypes and calling
'''
int, float, complex, string, tuple, bool - no change in global
list, set, dict - changes the global values
'''
'''
def  update(n):
    n += 10
    print("inner:", n)

n = 10
update(n)
print("outer:", n)

'''
'''
def  update(n):
    n += 10
    print("inner:", n)

n = 10.4
update(n)
print("outer:", n)
'''
'''
def  update(n):
    n += 10
    print("inner:", n)

n = 10+3j
update(n)
print("outer:", n)
'''
'''
def  update(n):
    n += "Kumar"
    print("inner:", n)

n = "Harish"
update(n)
print("outer:", n)
'''
'''
def  update(n):
    n.append(5)
    print("inner:", n)

n = [1,2,3,4]
update(n)
print("outer:", n)
'''
'''
def  update(n):
    n += (5,6)
    print("inner:", n)

n = (1,2,3,4)
update(n)
print("outer:", n)
'''
'''
def  update(n):
    n.add(5)
    print("inner:", n)

n = {1,2,3,4}
update(n)
print("outer:", n)
'''
'''
def  update(n):
    n.update({5:5, 6:6})
    print("inner:", n)

n = {1:1, 2:2, 3:3}
update(n)
print("outer:", n)
'''
'''
def  update(n):
    n = False
    print("inner:", n)

n = True
update(n)
print("outer:", n)
'''
