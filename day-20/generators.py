# iterating through generaors
'''
def display():
    for i in range(1,11):
        yield i

n = display()
for i in range(10):
    print(next(n))
'''

# factors using generstors
'''
def factors(n):
    for i in range(1,n+1):
        if n%i==0:
            yield i
n=int(input())
x = factors(n)
try:
    while True:
        print(next(x))
except StopIteration:
    print("end of the program")

'''

# next method
'''
def factors(n):
    return [i for i in range(1,n+1) if n%i==0]

def generators(res):
    for i in res:
        yield i
        
n = int(input())
res = factors(n)
facts = generators(res)
for i in range(len(res)):
    print(next(facts))
'''

# prime numbers

def Primes():
    res = []
    for num in range(2,101):
        for i in range(2, num//2):
            if num%i==0:
                break
        else:
            res.append(num)
    return res

def generators(res):
    for i in res:
        yield i

res = Primes()
g = generators(res)
for i in range(len(res)):
    print(next(g))
