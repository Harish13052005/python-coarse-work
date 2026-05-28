Python 3.11.8 (tags/v3.11.8:db85d51, Feb  6 2024, 22:03:32) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# Numeric
a = 1
type(a)
<class 'int'>
b = 2.0
type(b)
<class 'float'>
c = 2+3j
type(c)
<class 'complex'>
# sequential
d = "string"
type(d)
<class 'str'>
e = [1,2,4,6,8,3]
f = list()
f.append(3)
f.append(6)
type(e)
<class 'list'>
type(f)
<class 'list'>
print(e)
[1, 2, 4, 6, 8, 3]
print(f)
[3, 6]
g = (1,2,4,6,3)
h = ()

type(g)
<class 'tuple'>
type(h)
<class 'tuple'>
print(g)
(1, 2, 4, 6, 3)
>>> print(h)
()
>>> #Mapping
>>> i = {1,2,3,4,2,3}
>>> j = set()
>>> type(i)
<class 'set'>
>>> type(j)
<class 'set'>
>>> k = set(2,3,4)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    k = set(2,3,4)
TypeError: set expected at most 1 argument, got 3
>>> k = set(3)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    k = set(3)
TypeError: 'int' object is not iterable
>>> k = {'name':'hari', 'age': 20}
>>> type(k)
<class 'dict'>
>>> print(k)
{'name': 'hari', 'age': 20}
>>> # Boolean
>>> l = True
>>> m = False
>>> l
True
>>> m
False
>>> type(l)
<class 'bool'>
>>> type(m)
<class 'bool'>
>>> #None
>>> n = None
>>> n
>>> type(n)
<class 'NoneType'>
