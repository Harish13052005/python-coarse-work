# Lambda Function : var = lambda args: expression
'''
add = lambda a,b: a+b
mul = lambda c,d: c*d

print(add(3,4))
print(add(2,6))
print(add(6,7))
print(add(3,4))
print(add(6,7))
print(add(2,4))
'''

#welcome
'''
wish = lambda name: f"welcome to python course {name}"

print(wish('Harish'))
print(wish('rishi'))
print(wish('vamshi'))
'''

# GST
'''
gst = lambda price, tax: price*(tax/100)

price = int(input())
tax = float(input())
print(gst(price, tax))
'''

# greatest
'''
greatest = lambda a,b: a if a>b else b

print(greatest(18,19))
print(greatest(112,134))
print(greatest(1823,1239))
'''

# iseven
'''
iseven = lambda a: f"{a} is even" if a%2==0 else f"{a} is odd"

print(iseven(4))
print(iseven(32))
print(iseven(41))
'''

# charge
'''
bill = lambda charge: charge if charge>99 else charge+30

print(bill(120))
print(bill(33))
print(bill(250))
'''

# login and buy
'''
login = True
instock = True

status = lambda login, instock: ("you can buy product" if instock else "product is out of stock") if login else " Login to buy a product"

print(status(login, instock))

'''

#
'''
l = [1,2,3,4,5,6,7]
res = list(map(lambda i: i**3,l))
print(res)

names = ['harish', 'rishi', 'vamshi']
t = list(map(lambda i: i.title(), names))
print(t)
'''

# filter
'''
l = [1,2,3,4,5,6,7,8,9]
res = list(filter(lambda i: i>5, l))
print(res)

l = [1,2,3,4,5,6,7,8,9]
res = list(filter(lambda i: i%2==0, l))
print(res)

l = [1,2,3,4,5,6,7,8,9]
res = list(filter(lambda i: i%3==0, l))
print(res)
'''

# Reduce
'''
from functools import reduce
l = [1,2,3,4,5,6,7,8,9]

s = reduce(lambda sum,i: sum+i, l)
p = reduce(lambda pro,i: pro*i, l)

print(s,p)
'''

'''
from functools import reduce
l = [1,2,3,4,5,6,7,8,9]

s = reduce(lambda sum,i: sum+i, l)
p = reduce(lambda pro,i: pro*i, l)
m = reduce(lambda max,i: max if max>i else i,l)
mi = reduce(lambda max,i: max if max<i else i,l)

print(s,p,m,mi)
'''

# dict func
'''
d = {'subbu':50, 'nagendra':40, 'naresh':60, 'dinesh':80, 'sahith':70}

print(dict(sorted(d.items())))
print(dict(sorted(d.items(), key=lambda i: i[1])))
print(dict(sorted(d.items(), reverse=True)))
print(dict(sorted(d.items(), key=lambda i:i[1], reverse=True)))
'''
