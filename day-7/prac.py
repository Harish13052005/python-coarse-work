Python 3.11.8 (tags/v3.11.8:db85d51, Feb  6 2024, 22:03:32) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s = ' hello world'
s
' hello world'
s = '  hello   world   '
s
'  hello   world   '
s.strip
<built-in method strip of str object at 0x000001D9FC39F4B0>
s.strip
<built-in method strip of str object at 0x000001D9FC39F4B0>
s.strip()
'hello   world'
s.lstrip
<built-in method lstrip of str object at 0x000001D9FC39F4B0>
s.lstrip()
'hello   world   '
s.rstrip()
'  hello   world'
s = 'string.py
SyntaxError: unterminated string literal (detected at line 1)
s = 'string.py'
s
'string.py'
s.startswith('str')
True
s.startswith('gfh')
False
s.endswith(''py')
           
SyntaxError: unterminated string literal (detected at line 1)
s.endswith('py')
           
True
s.endswith('exe')
           
False
'ygtfv'.isalpha()
           
True
'123456'.isalpha()
           
False
'asdfgh12345'.isalnum()
           
True
'asdfghrtyuk'.isalnum()
           
True
'12345678'isalnum()
           
SyntaxError: invalid syntax
'123456789'.isalnum()
           
True
'asdfgh1234567@#$%'.isalnum()
           
False
'wertyuilkh'.islower()
           
True
'asdfgh1234567'.islower()
           
True
'asdfghj123456789@#$%^&*'.islower
           
<built-in method islower of str object at 0x000001D9FC0DD890>
'asdfgh12345678@#$%^&*9'.islower()
           
True
' '.isspace()
           
True
'    yfgvhb'.isspace()
           
False
'Py Program Lan'.istitle()
           
True
'Pyghjk program Lsfgf'.istitle()
           
False
'py_python'.isidentifier()
           
True
'py@gh'.isidentifier()
           
False
# List operations
           
l[]
           
SyntaxError: invalid syntax
l=[]
           
m = list()
           
type(l)
           
<class 'list'>
xswxawwws
           
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    xswxawwws
NameError: name 'xswxawwws' is not defined
l = [1,2,3,4]
           
m=[7,5,4,3]
           
l+m
           
[1, 2, 3, 4, 7, 5, 4, 3]
l*4
           
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
l = [10,20,30,40,50]
           
l[4]
           
50
l[0]
           
10
l[-1]
           
50
l[-3]
           
30
l[1:4]
           
[20, 30, 40]
l[::-1]
           
[50, 40, 30, 20, 10]
l[-1:-4:-1]
           
[50, 40, 30]
l[-3::-1]
           
[30, 20, 10]
l
           
[10, 20, 30, 40, 50]
20 in l
           
True
30 in l
           
True
40 not in l
           
False
80 in l
           
False
id(l)
           
2035791405248
l[1]
           
20
l[1]=70
           
l
           
[10, 70, 30, 40, 50]
id(l)
           
2035791405248
l[4]=100
           
l
           
[10, 70, 30, 40, 100]
l.append(120)
           
l
           
[10, 70, 30, 40, 100, 120]
l.insert(1,60)
           
l
           
[10, 60, 70, 30, 40, 100, 120]
l.insert(4,50)
           
l
           
[10, 60, 70, 30, 50, 40, 100, 120]
l.extend([80,90,110])
           
l
           
[10, 60, 70, 30, 50, 40, 100, 120, 80, 90, 110]
l.pop()
           
110
l
           
[10, 60, 70, 30, 50, 40, 100, 120, 80, 90]
l.pop()
           
90
l
           
[10, 60, 70, 30, 50, 40, 100, 120, 80]
l.pop(3)
           
30
l
           
[10, 60, 70, 50, 40, 100, 120, 80]
l.pop(1)
           
60
l
           
[10, 70, 50, 40, 100, 120, 80]
l.remove(100)
           
l
           
[10, 70, 50, 40, 120, 80]
l.remove(100)
           
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    l.remove(100)
ValueError: list.remove(x): x not in list
del l[1]
           
l
           
[10, 50, 40, 120, 80]
del l[2]
           
l
           
[10, 50, 120, 80]
l.clear()
           
l
           
[]
id(l)
           
2035791405248
l = [10, 60, 70, 30, 50, 40, 100, 120, 80]
           
l
           
[10, 60, 70, 30, 50, 40, 100, 120, 80]
sorted(l)
           
[10, 30, 40, 50, 60, 70, 80, 100, 120]
l.sort()
           
l
           
[10, 30, 40, 50, 60, 70, 80, 100, 120]
min(l)
           
10
max(l)
           
120
sorted(l,reverse=True)
           
[120, 100, 80, 70, 60, 50, 40, 30, 10]
l.index(120)
           
8
l.index(50)
           
3
l.index(99)
           
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    l.index(99)
ValueError: 99 is not in list
l.count(30)
           
1
l.count(20)
           
0
m = l
           
m
           
[10, 30, 40, 50, 60, 70, 80, 100, 120]
m.append(700)
           
m
           
[10, 30, 40, 50, 60, 70, 80, 100, 120, 700]
l
           
[10, 30, 40, 50, 60, 70, 80, 100, 120, 700]
n = l.copy()
           
n
           
[10, 30, 40, 50, 60, 70, 80, 100, 120, 700]
n.append(800)
           
n
           
[10, 30, 40, 50, 60, 70, 80, 100, 120, 700, 800]
l
           
[10, 30, 40, 50, 60, 70, 80, 100, 120, 700]
>>> len(l)
...            
10
>>> sum(l)
...            
1260
>>> 
>>> # 0 0.0 '' [] () {} set() False
...            
>>> any([1,2,3,4,5,5,0,0,0,0,0])
...            
True
>>> all([1,2,3,4,5,5,0,0,0,0,0])
...            
False
>>> any([123456])
...            
True
>>> any(0 0.0 '' [] () {} set() False)
...            
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> any([0,0.0,'',[],(),{},set(),False])
...            
False
>>> any([1,0,0.0,'',[],(),{},set(),False])
...            
True
>>> all([0,0.0,'',[],(),{},set(),False])
...            
False
>>> all(1,2,3)
...            
Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    all(1,2,3)
TypeError: all() takes exactly one argument (3 given)
>>> KeyboardInterrupt
>>> all([1,2,3])
...            
True
