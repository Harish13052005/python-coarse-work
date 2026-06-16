# recursion

'''
def func(num):
    if num == 0:
        return
    print(num, end=" ")
    func(num-1)

func(5)
'''

# for reversed order:
'''
def func(num):
    if num == 0:
        return
    func(num-1)
    print(num, end=" ")

func(5)
'''

# check the difference:
'''
def func(num):
    if num == 0:
        return
    print(num, end=" ")
    func(num-1)
    print(num, end=" ")

func(5)
'''

# sum of digits
'''
def sum_of_digits(num):
    if num == 0:
        return 0
    return num+sum_of_digits(num-1)
num = int(input())
print(sum_of_digits(num))
'''

# factorial
'''
def fact(num):
    if num == 1:
        return 1
    return num*fact(num-1)
num = int(input())
print(fact(num))
'''

#  Power of A to B
'''
def power(base, pow):
    if pow == 0:
        return 1
    return base * power(base, pow-1)
m,n = map(int, input().split())
print(power(m,n))
'''

# reverse of a string
'''
def reverse(s,ind):
    if ind == 0:
        return s[0]
    return s[ind]+reverse(s,ind-1)
s = input()
print(reverse(s,len(s)-1))
'''
