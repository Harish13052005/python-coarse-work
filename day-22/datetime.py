
from datetime import date, time, datetime, timedelta

'''
# date

t = date.today()

print(t)
print("year:", t.year)
print("month:", t.month)
print("day:", t.day)

print("weekday from 0:", t.weekday())
print("weekday from 1:", t.isoweekday())
'''

'''
t = date(2026,6,23)
# these are invalid, raises errors
    u = date(20220,6,23)
    v = date(2026,2,31)
    w = date(2026,13,23)
print(t)
print(u)
print(v)
print(w)
'''
'''
# time

t = time(23,59,0)
print(t)
'''

# datetime

n = datetime.now()

'''
print(n)
print("Year:", n.year)
print("month:", n.month)
print("day:", n.day)
print("hour:", n.hour)
print("minute:", n.minute)
print("second:", n.second)
'''
'''
print(n.strftime('%d/%m/%y'))
print(n.strftime('%d/%m/%y %H:%M:%S'))
print(n.strftime('%d/%m/%y %I:%M:%S'))
print(n.strftime('%d/%m/%y %I:%M:%S %p'))
print(n.strftime('%d/%b/%y %I:%M:%S %p'))
print(n.strftime('%d/%B/%y %I:%M:%S %p'))
print(n.strftime('%a, %d %B, %Y I:%M:%S %p'))
print(n.strftime('%A, %d %B, %Y I:%M:%S %p'))
'''

# Time delta

'''
n = datetime.now()

n15 = n + timedelta(minutes=15)
n2 = n + timedelta(hours=2)
n7 = n + timedelta(days=7)
n60 = n + timedelta(days=60)

print(n15, n2, n7, n60, sep="\n")
'''
