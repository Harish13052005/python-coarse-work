Python 3.11.8 (tags/v3.11.8:db85d51, Feb  6 2024, 22:03:32) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#dictionary
d = {}
d = dict()
type(d)
<class 'dict'>
d = {'k1':'v1', 'k2':'v2'}
d
{'k1': 'v1', 'k2': 'v2'}
d[1] = 'int'
d
{'k1': 'v1', 'k2': 'v2', 1: 'int'}
d[12.3] = 'float'
d
{'k1': 'v1', 'k2': 'v2', 1: 'int', 12.3: 'float'}
d['asdf'] = '2j+3'
d
{'k1': 'v1', 'k2': 'v2', 1: 'int', 12.3: 'float', 'asdf': '2j+3'}
d[3j+2]='abcd'
d
{'k1': 'v1', 'k2': 'v2', 1: 'int', 12.3: 'float', 'asdf': '2j+3', (2+3j): 'abcd'}
d[[1,2,3]] = [2,3,4]
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    d[[1,2,3]] = [2,3,4]
TypeError: unhashable type: 'list'
d[(1,2,3)] = (2,3,4)
d
{'k1': 'v1', 'k2': 'v2', 1: 'int', 12.3: 'float', 'asdf': '2j+3', (2+3j): 'abcd', (1, 2, 3): (2, 3, 4)}
d[{1,2,3}) = {5,6,7}
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
d[{1,2,3}] = {5,6,7}
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    d[{1,2,3}] = {5,6,7}
TypeError: unhashable type: 'set'
d[4] = {5,6,7}
d
{'k1': 'v1', 'k2': 'v2', 1: 'int', 12.3: 'float', 'asdf': '2j+3', (2+3j): 'abcd', (1, 2, 3): (2, 3, 4), 4: {5, 6, 7}}
d[1] = 1
d
{'k1': 'v1', 'k2': 'v2', 1: 1, 12.3: 'float', 'asdf': '2j+3', (2+3j): 'abcd', (1, 2, 3): (2, 3, 4), 4: {5, 6, 7}}
d[2.1] = 2.12
d
{'k1': 'v1', 'k2': 'v2', 1: 1, 12.3: 'float', 'asdf': '2j+3', (2+3j): 'abcd', (1, 2, 3): (2, 3, 4), 4: {5, 6, 7}, 2.1: 2.12}
d[3] = 2+3j
d
{'k1': 'v1', 'k2': 'v2', 1: 1, 12.3: 'float', 'asdf': '2j+3', (2+3j): 'abcd', (1, 2, 3): (2, 3, 4), 4: {5, 6, 7}, 2.1: 2.12, 3: (2+3j)}
d[4] = [1,2,3]
d
{'k1': 'v1', 'k2': 'v2', 1: 1, 12.3: 'float', 'asdf': '2j+3', (2+3j): 'abcd', (1, 2, 3): (2, 3, 4), 4: [1, 2, 3], 2.1: 2.12, 3: (2+3j)}
d[5] = {1:1, 2:2, 3:3}
d
{'k1': 'v1', 'k2': 'v2', 1: 1, 12.3: 'float', 'asdf': '2j+3', (2+3j): 'abcd', (1, 2, 3): (2, 3, 4), 4: [1, 2, 3], 2.1: 2.12, 3: (2+3j), 5: {1: 1, 2: 2, 3: 3}}
type(d)
<class 'dict'>
d[6] = False
d
{'k1': 'v1', 'k2': 'v2', 1: 1, 12.3: 'float', 'asdf': '2j+3', (2+3j): 'abcd', (1, 2, 3): (2, 3, 4), 4: [1, 2, 3], 2.1: 2.12, 3: (2+3j), 5: {1: 1, 2: 2, 3: 3}, 6: False}
## in dictionary keys must be immutable and unique, values can be anything
d[1] = 123
d
{'k1': 'v1', 'k2': 'v2', 1: 123, 12.3: 'float', 'asdf': '2j+3', (2+3j): 'abcd', (1, 2, 3): (2, 3, 4), 4: [1, 2, 3], 2.1: 2.12, 3: (2+3j), 5: {1: 1, 2: 2, 3: 3}, 6: False}
d[2]
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    d[2]
KeyError: 2
d[1]
123
d[3]
(2+3j)
d[4]
[1, 2, 3]
d[5]
{1: 1, 2: 2, 3: 3}
d[6]
False
e = {'harish':98, 'rishi':21, 'vamshi':82, 'sahith':63}
e
{'harish': 98, 'rishi': 21, 'vamshi': 82, 'sahith': 63}
e[sahith]
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    e[sahith]
NameError: name 'sahith' is not defined
e['sahith']
63
e['harish']
98
e['rishi']
21
e['nagendra']
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    e['nagendra']
KeyError: 'nagendra'
e.get['sahith']
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    e.get['sahith']
TypeError: 'builtin_function_or_method' object is not subscriptable
e.get('sahith')
63
e.get('harish')
98
e.get('nagendra')
e
{'harish': 98, 'rishi': 21, 'vamshi': 82, 'sahith': 63}
e.get('harish', 'sahith', 'nagendra')
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    e.get('harish', 'sahith', 'nagendra')
TypeError: get expected at most 2 arguments, got 3
e.get('harish', 'nagendra')
98
d.get('harish', 'user not found')
'user not found'
e.get('harish', 'user not found')
98
'harish' in e
True
'sahith' in e
True
'akhil' in e
False
'nag' not in e
True
d.keys()
dict_keys(['k1', 'k2', 1, 12.3, 'asdf', (2+3j), (1, 2, 3), 4, 2.1, 3, 5, 6])
e.keys()
dict_keys(['harish', 'rishi', 'vamshi', 'sahith'])
d.values()
dict_values(['v1', 'v2', 123, 'float', '2j+3', 'abcd', (2, 3, 4), [1, 2, 3], 2.12, (2+3j), {1: 1, 2: 2, 3: 3}, False])
e.values()
dict_values([98, 21, 82, 63])
d.items()
dict_items([('k1', 'v1'), ('k2', 'v2'), (1, 123), (12.3, 'float'), ('asdf', '2j+3'), ((2+3j), 'abcd'), ((1, 2, 3), (2, 3, 4)), (4, [1, 2, 3]), (2.1, 2.12), (3, (2+3j)), (5, {1: 1, 2: 2, 3: 3}), (6, False)])
e.items()
dict_items([('harish', 98), ('rishi', 21), ('vamshi', 82), ('sahith', 63)])
sorted(d)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    sorted(d)
TypeError: '<' not supported between instances of 'int' and 'str'
sorted(e)
['harish', 'rishi', 'sahith', 'vamshi']
max(d)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    max(d)
TypeError: '>' not supported between instances of 'int' and 'str'
max(e)
'vamshi'
min(e)
'harish'
len(d)
12
len(e)
4
d['harish'] = 99
d
{'k1': 'v1', 'k2': 'v2', 1: 123, 12.3: 'float', 'asdf': '2j+3', (2+3j): 'abcd', (1, 2, 3): (2, 3, 4), 4: [1, 2, 3], 2.1: 2.12, 3: (2+3j), 5: {1: 1, 2: 2, 3: 3}, 6: False, 'harish': 99}
d['subbu'] = 85
d
{'k1': 'v1', 'k2': 'v2', 1: 123, 12.3: 'float', 'asdf': '2j+3', (2+3j): 'abcd', (1, 2, 3): (2, 3, 4), 4: [1, 2, 3], 2.1: 2.12, 3: (2+3j), 5: {1: 1, 2: 2, 3: 3}, 6: False, 'harish': 99, 'subbu': 85}
e['harish'] = 99
e
{'harish': 99, 'rishi': 21, 'vamshi': 82, 'sahith': 63}
e['subbu'] = 85
e
{'harish': 99, 'rishi': 21, 'vamshi': 82, 'sahith': 63, 'subbu': 85}
e.update({'naren':88, 'praneeth':65, 'praveen':77})
e
{'harish': 99, 'rishi': 21, 'vamshi': 82, 'sahith': 63, 'subbu': 85, 'naren': 88, 'praneeth': 65, 'praveen': 77}
e.pop()
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    e.pop()
TypeError: pop expected at least 1 argument, got 0
e.popitem()
('praveen', 77)
e.popitem()
('praneeth', 65)
e.pop('sahith')
63
e
{'harish': 99, 'rishi': 21, 'vamshi': 82, 'subbu': 85, 'naren': 88}
del d['vamsi']
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    del d['vamsi']
KeyError: 'vamsi'
del e['vamsi']
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    del e['vamsi']
KeyError: 'vamsi'
del e['vamshi']
e
{'harish': 99, 'rishi': 21, 'subbu': 85, 'naren': 88}
e.clear()
e
{}
d.setdefault('rishi',0)
0
d.setdefault('harish', 0)
99

#Conditional statements
s = "python statement"

print("found" if "python" in s)
SyntaxError: expected 'else' after 'if' expression
>>> 
============================================= RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-9/Conditions.py =============================================
found
True
>>> 
============================================= RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-9/Conditions.py =============================================
enter the username and password:abc 12345
Invalid Login
>>> 
============================================= RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-9/Conditions.py =============================================
enter the username and password:abc 1234
Login Successful
>>> 
============================================= RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-9/Conditions.py =============================================
enter the username and password:abc 1234
Invalid Login
>>> 
============================================= RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-9/Conditions.py =============================================
12345
+ve
>>> 
============================================= RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-9/Conditions.py =============================================
-123456
-ve
>>> 
============================================= RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-9/Conditions.py =============================================
00000
zero
>>> 
============================================= RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-9/Conditions.py =============================================
enter the product:TV
TV is unavailable
>>> 
============================================= RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-9/Conditions.py =============================================
enter the product:laptops
 laptops out of stock
>>> 
============================================= RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-9/Conditions.py =============================================
enter the product:mouse
 You can buy mouse
