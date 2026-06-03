Python 3.11.8 (tags/v3.11.8:db85d51, Feb  6 2024, 22:03:32) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

================================================= RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-6/q1.py =================================================
harish
12
81
89
91
student name:harish
roll no:12
Total marks:261
Average marks:87.0

================================================= RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-6/q2.py =================================================
python
total characters: 6
first character: p
last character: n
uppercase: PYTHON
reversed string: nohtyp

================================================= RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-6/q3.py =================================================
12 34 56
sum: 102
average: 64.66666666666667
product: 22848
s = 'python programming'
len(s)
18
sorted(s)
[' ', 'a', 'g', 'g', 'h', 'i', 'm', 'm', 'n', 'n', 'o', 'o', 'p', 'p', 'r', 'r', 't', 'y']
min(s)
' '
max(s)
'y'
ord('a')
97
ord('p')
112
ord('H')
72
ord('h')
104
ord('%')
37
chr(12)
'\x0c'
chr(35)
'#'
chr(65)
'A'
chr(45)
'-'
s.upper()
'PYTHON PROGRAMMING'
s.lower()
'python programming'
s.capitalize()
'Python programming'
s.title()
'Python Programming'
s.swapcase()
'PYTHON PROGRAMMING'
"sTraasjhx".casefold() # for converting the accent characters into lower
'straasjhx'
# Alignmnet operations
s.center(28,'*')
'*****python programming*****'
s.ljust(28,'_')
'python programming__________'
rjust('_')
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    rjust('_')
NameError: name 'rjust' is not defined
s.rjust('_')
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    s.rjust('_')
TypeError: 'str' object cannot be interpreted as an integer
s.rjust(28,'_')
'__________python programming'
'123'.zfill(5)
'00123'
'123'.zfill(10)
'0000000123'
s.zfill(21)
'000python programming'
s.zfill(2)
'python programming'
s
'python programming'
#finding

s.find('o')
4
s.find('g')
10
s.rfind('o')
9
s.find('z')
-1
s.count('Y')
0
s.count9'y')
SyntaxError: unmatched ')'
s.count('y')
1
s.count('o')
2
#replace
s.replace('python','java')
'java programming'
s.maketrans('python','123456')
{112: 49, 121: 50, 116: 51, 104: 52, 111: 53, 110: 54}
s.translate(s.maketrans('python','123456')
)
'123456 1r5grammi6g'
#splitting & joining
s='java,python,javascript,c,c++'
s.split(',')
['java', 'python', 'javascript', 'c', 'c++']
s.split(',',2)
['java', 'python', 'javascript,c,c++']
s.rsplit(',',2)
['java,python,javascript', 'c', 'c++']
g = 'sdfgh'
>>> g='''wdcgv
... wdchkn
... wdch'''
>>> g
'wdcgv\nwdchkn\nwdch'
>>> l = 'java', 'python', 'javascript', 'c', 'c++']
SyntaxError: unmatched ']'
>>> ''.join(1)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    ''.join(1)
TypeError: can only join an iterable
>>> ''.join(l)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    ''.join(l)
NameError: name 'l' is not defined
>>> l = ['java', 'python', 'javascript', 'c', 'c++']
>>> ''.join(l)
'javapythonjavascriptcc++'
>>> '-'.join(l)
'java-python-javascript-c-c++'
>>> '@'.join(l)
'java@python@javascript@c@c++'
>>> ' '.join(l)
'java python javascript c c++'
>>> ','.join(l)
'java,python,javascript,c,c++'
>>> #partition
>>> s.partition(',')
('java', ',', 'python,javascript,c,c++')
>>> s.rpartition(',')
('java,python,javascript,c', ',', 'c++')
>>> #encoding and decoding ( to convert the data to byte cide and vise versa)
>>> t = "hello ❤"
>>> t.encode()
b'hello \xe2\x9d\xa4'
>>> b'hello \xe2\x9d\xa4'.decode
<built-in method decode of bytes object at 0x0000012D06248AB0>
>>> b'hello \xe2\x9d\xa4'.decode()
'hello ❤'
