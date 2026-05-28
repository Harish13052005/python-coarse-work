Python 3.11.8 (tags/v3.11.8:db85d51, Feb  6 2024, 22:03:32) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# int to:
a = 10
float(a)
10.0
complex(a)
(10+0j)
str(a)
'10'
list(a)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
dict(a)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
bool(a)
True
# int -> flaot, complex, string, bool

# float to: int, complex, str, bool
b = 12.3
int(b)
12
complex(b)
(12.3+0j)
str(b)
'12.3'
list(b)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    list(b)
TypeError: 'float' object is not iterable
tuple(b)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    tuple(b)
TypeError: 'float' object is not iterable
set(b)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    set(b)
TypeError: 'float' object is not iterable
dict(b)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    dict(b)
TypeError: 'float' object is not iterable
bool(b)
True

# complex to : str, bool
c = 2+3j
int(c)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    int(c)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
float(c)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    float(c)
TypeError: float() argument must be a string or a real number, not 'complex'
str(c)
'(2+3j)'
list(c)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    list(c)
TypeError: 'complex' object is not iterable
tuple(c)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    tuple(c)
TypeError: 'complex' object is not iterable
set(c)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    set(c)
TypeError: 'complex' object is not iterable
dict(c)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    dict(c)
TypeError: 'complex' object is not iterable
bool(c)
True

# string to:
d = "123456"
e = "harish"
f = "1234.5678"
int(d)
123456
int(f)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    int(f)
ValueError: invalid literal for int() with base 10: '1234.5678'
int(g)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    int(g)
NameError: name 'g' is not defined
int(e)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    int(e)
ValueError: invalid literal for int() with base 10: 'harish'
float(d)
123456.0
float(e)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    float(e)
ValueError: could not convert string to float: 'harish'
float(f)
1234.5678
complex(d)
(123456+0j)
complex(e)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    complex(e)
ValueError: complex() arg is a malformed string
complex(f)
(1234.5678+0j)
list(d)
['1', '2', '3', '4', '5', '6']
list(e)
['h', 'a', 'r', 'i', 's', 'h']
list(f)
['1', '2', '3', '4', '.', '5', '6', '7', '8']
tuple(d)
('1', '2', '3', '4', '5', '6')
tuple(e)
('h', 'a', 'r', 'i', 's', 'h')
tuple(f)
('1', '2', '3', '4', '.', '5', '6', '7', '8')
set(d)
{'3', '5', '4', '2', '6', '1'}
set(e)
{'h', 'a', 's', 'i', 'r'}
set(f)
{'3', '.', '8', '5', '4', '2', '6', '7', '1'}
dict(d)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    dict(d)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
dict(e)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    dict(e)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
dict(f)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    dict(f)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
bool(d)
True
bool(e)
True
boo(f)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    boo(f)
NameError: name 'boo' is not defined. Did you mean: 'bool'?

# list to : str, tuple, set, bool
g = [1,2,3,4,5]
int(g)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    int(g)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
float(g)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    float(g)
TypeError: float() argument must be a string or a real number, not 'list'
complex(g)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    complex(g)
TypeError: complex() first argument must be a string or a number, not 'list'
str(g)
'[1, 2, 3, 4, 5]'
tuple(g)
(1, 2, 3, 4, 5)
set(g)
{1, 2, 3, 4, 5}
dict(g)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    dict(g)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
bool(g)
True

#tuple to: str, list, set, bool
h = (1,2,3,4,5)
int(h)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    int(h)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
float(h)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    float(h)
TypeError: float() argument must be a string or a real number, not 'tuple'
complex(h)
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    complex(h)
TypeError: complex() first argument must be a string or a number, not 'tuple'
str(h)
'(1, 2, 3, 4, 5)'
list(h)
[1, 2, 3, 4, 5]
tuple(h)
(1, 2, 3, 4, 5)
set(h)
{1, 2, 3, 4, 5}
dict(h)
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    dict(h)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
bool(h)
True

# set to: str, list, tuple, bool
i = {1,2,3,4,5}
int(i)
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    int(i)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'set'
float(i)
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    float(i)
TypeError: float() argument must be a string or a real number, not 'set'
complex(i)
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    complex(i)
TypeError: complex() first argument must be a string or a number, not 'set'
str(i)
'{1, 2, 3, 4, 5}'
list(i)
[1, 2, 3, 4, 5]
tuple()
()
tuple(i)
(1, 2, 3, 4, 5)
dict(i)
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    dict(i)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
bool(i)
True

# dict to: str,list,tuple,set,bool
j = {'a':1, 'b':2, 'c':3}
int(j)
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    int(j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'dict'
float(j)
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    float(j)
TypeError: float() argument must be a string or a real number, not 'dict'
complex(j)
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    complex(j)
TypeError: complex() first argument must be a string or a number, not 'dict'
str(j)
"{'a': 1, 'b': 2, 'c': 3}"
list(j)
['a', 'b', 'c']
tuple(j)
('a', 'b', 'c')
set(j)
{'c', 'b', 'a'}
dict(j)
{'a': 1, 'b': 2, 'c': 3}
bool(j)
True

# bool to: int, float, str, complex
k = True
L = False
int(k)
1
int(l)
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    int(l)
NameError: name 'l' is not defined. Did you mean: 'L'?
int(L)
0
float(k)
1.0
float(L)
0.0
complex(k)
(1+0j)
complex(L)
0j
str(k)
'True'
str(L)
'False'
list(k)
Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    list(k)
TypeError: 'bool' object is not iterable
>>> list(L)
Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    list(L)
TypeError: 'bool' object is not iterable
>>> tuple(k)
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    tuple(k)
TypeError: 'bool' object is not iterable
>>> tuple(L)
Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    tuple(L)
TypeError: 'bool' object is not iterable
>>> set(k)
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    set(k)
TypeError: 'bool' object is not iterable
>>> set(L)
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    set(L)
TypeError: 'bool' object is not iterable
>>> dict(k)
Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    dict(k)
TypeError: 'bool' object is not iterable
>>> dict(L)
Traceback (most recent call last):
  File "<pyshell#130>", line 1, in <module>
    dict(L)
TypeError: 'bool' object is not iterable
