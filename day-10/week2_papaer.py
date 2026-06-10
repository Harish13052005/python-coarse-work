#week2 paper:

# Q1
'''
salary = int(input())
bonus = 0
if salary >= 70000:
    bonus = salary*0.2
elif salary >= 50000:
    bonus = salary*0.15
elif salary >= 30000:
    bonus = salary*0.1
else:
    bonus = salary*0.05

print(bonus)
'''

#Q2
'''
tup = tuple(input().split())
pro = input()
pri = int(input())
s = set(map(int, input().split()))

print(tup)
d={}
d[pro] = pri
print(d)
print(s)
'''

#Q3
'''
n = list(map(int, input().split()))
print(len(n))
print(sorted(n))
print(max(n))
print(min(n))
'''

#Q4
'''
age = int(input())
if age >= 18:
    print("eligible to vote")
else:
    print("not eligible")
'''

#Q5
marks = int(input())
if marks >= 35:
    print("pass")
else:
    print("fail")


