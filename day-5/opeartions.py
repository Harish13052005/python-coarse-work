Python 3.11.8 (tags/v3.11.8:db85d51, Feb  6 2024, 22:03:32) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
name = input()
Hari
name
'Hari'
name = input("enter your name:")
enter your name:Hari
name
'Hari'
age = input("enter your age:")
enter your age:21
age
'21'
age = int(input("enter your age:"))
enter your age:21
age
21
type(age)
<class 'int'>
gpa = float(input("enter the cgpa:"))
enter the cgpa:7.46
type(gpa)
<class 'float'>
'Harish, rishi, vamsi, subbu, nagendra, sahith'
'Harish, rishi, vamsi, subbu, nagendra, sahith'
'Harish, rishi, vamsi, subbu, nagendra, sahith'.split('')
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    'Harish, rishi, vamsi, subbu, nagendra, sahith'.split('')
ValueError: empty separator
'Harish, rishi, vamsi, subbu, nagendra, sahith'.split(' ')
['Harish,', 'rishi,', 'vamsi,', 'subbu,', 'nagendra,', 'sahith']
'Harish-rishi-vamsi-subbu-nagendra-sahith'.split('-')
['Harish', 'rishi', 'vamsi', 'subbu', 'nagendra', 'sahith']
names = input("enter names:").split()
enter names:subbu nag hari sahith rishi vamshi
names
['subbu', 'nag', 'hari', 'sahith', 'rishi', 'vamshi']
products = input("enter prod:").split()
enter prod:laptop mouse charger keyboard
products
['laptop', 'mouse', 'charger', 'keyboard']
topics = tuple(input("enter topics:").split())
enter topics:token statement variable comment
topics
('token', 'statement', 'variable', 'comment')
op = set(input("enter operators:").split())
enter operators:in not in is not and or not
op
{'in', 'or', 'is', 'not', 'and'}
a = map(int,input().split())
12 34 64 23 1
a
<map object at 0x0000021C009F3B50>
b = list(map(int,input("enter marks:").split()))
enter marks:1 3 5 85 345
list(map(int,input("enter marks:").split()))
enter marks:1 3 5 67 345
[1, 3, 5, 67, 345]
b
[1, 3, 5, 85, 345]
prices = tuple(map(int, input("enter prices:").split()))
enter prices:123 345 67 23
prices
(123, 345, 67, 23)
rating = set(map(int, input("enter rating:").split()))
enter rating:12.3 23.5 34.6 6.7
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    rating = set(map(int, input("enter rating:").split()))
ValueError: invalid literal for int() with base 10: '12.3'
rating = set(map(float, input("enter rating:").split()))
enter rating:12.3 23.5 34.6 6.7
rating
{34.6, 12.3, 6.7, 23.5}
per = list(map(float, input("enter the percentage:").split()))
enter the percentage:5.3 23.5 45.7 12.7
per
[5.3, 23.5, 45.7, 12.7]
prices = tuple(map(float, input("enter the prices:").split()))
enter the prices:123 345 456 678
prices
(123.0, 345.0, 456.0, 678.0)
prices = set(map(float, input("enter the prices:")))
enter the prices:332 345 567 345
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    prices = set(map(float, input("enter the prices:")))
ValueError: could not convert string to float: ' '
prices = set(map(float, input("enter the prices:").split()))
enter the prices:234 345 678 89
>>> prices
{89.0, 345.0, 234.0, 678.0}
>>> prices = set(map(float, input("enter the prices:").split()))
... 
enter the prices:234 345 567 8oo
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    prices = set(map(float, input("enter the prices:").split()))
ValueError: could not convert string to float: '8oo'
>>> username, password = input().split()
hari h@123
>>> username
'hari'
>>> password
'h@123'
>>> a,b,c,d = list(map(int, input("enter 4 values:").split()))
enter 4 values:2 4 6 8
>>> a
2
>>> b
4
>>> c
6
>>> d
8
>>> price,discount = list(map(float, input("enter the price and discount:").split()))
enter the price and discount:345678 89.2
>>> price
345678.0
>>> discount
89.2
>>> a = eval(input())
356
>>> a
356
>>> a = eval(input())
... 
123.456
>>> a
123.456
>>> a = eval(input())

'harish'
a
'harish'
a = eval(input())
[1 2 3 4 5]
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    a = eval(input())
  File "<string>", line 1
    [1 2 3 4 5]
     ^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
a = eval(input())
[1,2,3,4,5]
a
[1, 2, 3, 4, 5]
a = eval(input())
(1,2,3,4,5)
a
(1, 2, 3, 4, 5)
a = eval(input())
{1,2,3,4,5)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    a = eval(input())
  File "<string>", line 1
    {1,2,3,4,5)
              ^
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
a = eval(input())
{1,2,3,4,5}
a
{1, 2, 3, 4, 5}
a = eval(input())
{a:1,b:2,c:3}
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    a = eval(input())
  File "<string>", line 1, in <module>
TypeError: unhashable type: 'set'
a = eval(input())
{ a:1, b:2, c:3}
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    a = eval(input())
  File "<string>", line 1, in <module>
TypeError: unhashable type: 'set'
a = eval(input())
{1:2,3:4,5:6}
a
{1: 2, 3: 4, 5: 6}
a = eval(input())
{ d:1, b:2, c:3}
a
{8: 1, 4: 2, 6: 3}
a = eval(input())
True
type(a)
<class 'bool'>
a = 'harish'
b = 'kumar'
a+b
'harishkumar'
#repetition
a*10
'harishharishharishharishharishharishharishharishharishharish'
'*'*5
'*****'
#indexing
names = 'harish kumar sahith rohith'
names[0]
'h'
names[-1]
'h'
names[:5]
'haris'
names[2:7]
'rish '
names[-9::-1]
'tihas ramuk hsirah'
#slicing ^
names[5:]
'h kumar sahith rohith'
#membership
s = [ a b c d e f]
SyntaxError: invalid syntax. Perhaps you forgot a comma?
s = [a,b,c,d,e,f]
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    s = [a,b,c,d,e,f]
NameError: name 'e' is not defined
s = "hello world"
"a" in s
False
e in s
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    e in s
NameError: name 'e' is not defined
"e" in s
True
t = [1,2,3,4]
2 in t
True
5 in t
False
3 not in t
False
