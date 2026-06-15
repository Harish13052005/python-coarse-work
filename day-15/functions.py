'''
def function_name(arg):
    #stmts
    return
function_name(para)
'''

# Wish
'''
def wish(name):
    print(f'welcome to the python course {name}!')

wish('Harish')
wish('sahith')
wish('Rishi')
wish('vamshi')
'''

# iseven
'''
def iseven(num):
    if num%2==0:
        return f"{num} is even"
    else:
        return f"{num} is not even"

print(iseven(12))
print(iseven(13))
'''

# factorial
'''
def factorial(num):
    fact = 1
    for i in range(1, num+1):
        fact *= i

    return fact

num = int(input("enter a number:"))
print(f"fact of {num} is ", factorial(num))
'''

# prime  or not
'''
def isprime(num):
    for i in range(2,num//2):
        if num%i == 0:
            return f"{num} is not prime"
    return f"{num} is prime"

num = int(input("enter a number:"))
print(isprime(num))
'''

