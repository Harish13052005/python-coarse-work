Python 3.11.8 (tags/v3.11.8:db85d51, Feb  6 2024, 22:03:32) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#tuple
t = (1,2,3,4,5)
t
(1, 2, 3, 4, 5)
t = (10,20,30,40,50)
h = (70,80,90)
t+h
(10, 20, 30, 40, 50, 70, 80, 90)
t*4
(10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50)
t[1]
20
t[4]
50
t[-1]
50
t[-3]
30
t[:3]
(10, 20, 30)
t[3:]
(40, 50)
t[1:4]
(20, 30, 40)
t[2:]
(30, 40, 50)
t[::2]
(10, 30, 50)
t[::-1]
(50, 40, 30, 20, 10)
t[-1:-4:-1]
(50, 40, 30)
10 in t
True
30 in t
True
50 not in t
False
80 not in t
True
len(t)
5
sorted(t)
[10, 20, 30, 40, 50]
min(t)
10
max(t)
50
sum(t)
150
t.count(10)
1
t.index(10)
0
a = (1,2,4)
a
(1, 2, 4)
x,y,z = a
x
1
y
2
z
4
#packing and unpacking
t = (1,2,3,[4,5,6],7)
t
(1, 2, 3, [4, 5, 6], 7)
t[0]
1
t[2]
3
t[3]
[4, 5, 6]
t[5]
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    t[5]
IndexError: tuple index out of range
t[3].append(10)
t[3]
[4, 5, 6, 10]
t
(1, 2, 3, [4, 5, 6, 10], 7)
t[2] = 4
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    t[2] = 4
TypeError: 'tuple' object does not support item assignment
#set
s = {1,2,3,4}
s
{1, 2, 3, 4}
s = {1,2,3,12,3,4,5,qw,,2,3,4,3}
SyntaxError: invalid syntax
s = {1,2,3,12,3,4,5,qw,2,3,4,3}
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    s = {1,2,3,12,3,4,5,qw,2,3,4,3}
NameError: name 'qw' is not defined
s = {1,2,3,12,3,4,5,"qw",4,2,3,4,3}
s
{1, 2, 3, 4, 5, 'qw', 12}
s
{1, 2, 3, 4, 5, 'qw', 12}
s.add(13)
s
{1, 2, 3, 4, 5, 'qw', 12, 13}
s.add(23.34)
s
{1, 2, 3, 4, 5, 'qw', 12, 13, 23.34}
s = {1, 2, 3, 4, 5, 'qw', 12, 13, 23.34, [1,2,3,4]}
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    s = {1, 2, 3, 4, 5, 'qw', 12, 13, 23.34, [1,2,3,4]}
TypeError: unhashable type: 'list'
s = {1, 2, 3, 4, 5, 'qw', 12, 13, 23.34, (1,2,3,4)}
s
{1, 2, 3, 4, 5, 'qw', 12, 13, (1, 2, 3, 4), 23.34}
s
{1, 2, 3, 4, 5, 'qw', 12, 13, (1, 2, 3, 4), 23.34}
s = {1, 2, 3, 4, 5, 'qw', 12, 13, (1, 2, 3, 4), 23.34, {1,2,3}}
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    s = {1, 2, 3, 4, 5, 'qw', 12, 13, (1, 2, 3, 4), 23.34, {1,2,3}}
TypeError: unhashable type: 'set'
s = {1, 2, 3, 4, 5, 'qw', 12, 13, (1, 2, 3, 4), 23.34, {a:1, b:2, c:3})
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
s = {1, 2, 3, 4, 5, 'qw', 12, 13, (1, 2, 3, 4), 23.34, {a:1, b:2, c:3}}
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    s = {1, 2, 3, 4, 5, 'qw', 12, 13, (1, 2, 3, 4), 23.34, {a:1, b:2, c:3}}
NameError: name 'b' is not defined
s.add("hsg")
s
{1, 2, 3, 4, 5, 'qw', 12, 13, (1, 2, 3, 4), 'hsg', 23.34}
s.add([12])
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    s.add([12])
TypeError: unhashable type: 'list'
1 in s
True
2 in s
True
3 in s
True
12 in s
True
23 in s
False
False in s
False
s.append(True)
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    s.append(True)
AttributeError: 'set' object has no attribute 'append'
s.add(True)
s
{1, 2, 3, 4, 5, 'qw', 12, 13, (1, 2, 3, 4), 'hsg', 23.34}
s.add(False)
s
{False, 1, 2, 3, 4, 5, 'qw', 12, 13, (1, 2, 3, 4), 'hsg', 23.34}
True in s
True
False in s
True
#spcl operations
a = {1,2,3,4,5,7,9}
b = {3,6,8,9}
a | b
{1, 2, 3, 4, 5, 6, 7, 8, 9}
a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8, 9}
a & b
{9, 3}
a.intersection(b)
{9, 3}
a-b
{1, 2, 4, 5, 7}
a
{1, 2, 3, 4, 5, 7, 9}
a^b
{1, 2, 4, 5, 6, 7, 8}
#subset and superset
a
{1, 2, 3, 4, 5, 7, 9}
a <= [1}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
a <= {1}
False
a >= {1}
True
b = {2,4,6,8}
a = {1,2,3,4,5,6,7,8,9}
a >= b
True
b <= a
True
a >= {1,4,3,8,5}
True
a
{1, 2, 3, 4, 5, 6, 7, 8, 9}
a.add(17)
a
{1, 2, 3, 4, 5, 6, 7, 8, 9, 17}
a.update({11,12,13})
a
{1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 17}
a.pop()
1
a
{2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 17}
a.pop()
2
a
{3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 17}
a.remove(6)
a
{3, 4, 5, 7, 8, 9, 11, 12, 13, 17}
a.remove(6)
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    a.remove(6)
KeyError: 6
a.discard(3)
a
{4, 5, 7, 8, 9, 11, 12, 13, 17}
a.discard(3)
a
{4, 5, 7, 8, 9, 11, 12, 13, 17}
a.clear()
a
set()
a
set()
a = {1,2,3,4,5,6,}
a
{1, 2, 3, 4, 5, 6}
b = {2,4,6}
a.intersection(b)
{2, 4, 6}
a
{1, 2, 3, 4, 5, 6}
a.intersection_update(b)
a
{2, 4, 6}
b
{2, 4, 6}
>>> c = b
>>> c
{2, 4, 6}
>>> b
{2, 4, 6}
>>> b.add{8)
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
>>> b.add(8)
>>> b
{8, 2, 4, 6}
>>> c
{8, 2, 4, 6}
>>> b = copy(c)
Traceback (most recent call last):
  File "<pyshell#136>", line 1, in <module>
    b = copy(c)
NameError: name 'copy' is not defined
>>> b = c.copy()
>>> b
{8, 2, 4, 6}
>>> c
{8, 2, 4, 6}
>>> b.add(10)
>>> b
{2, 4, 6, 8, 10}
>>> c
{8, 2, 4, 6}
>>> len(c)
4
>>> min(c)
2
>>> max(c)
8
>>> sorted(c)
[2, 4, 6, 8]
>>> sum(c)
20
>>> sorted(c, reverse=True)
[8, 6, 4, 2]
