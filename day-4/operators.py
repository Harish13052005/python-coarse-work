Python 3.11.8 (tags/v3.11.8:db85d51, Feb  6 2024, 22:03:32) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = 20
b = 10

a+b
30
a-b
10
a*b
200
a/b
2.0
a//b
2
a%b
0

#Comparison
a<b
False
a<=b
False
a>b
True
a>=b
True
a==b
False
a!=b
True

# Assignment
a+=10
a-=5
a*=2
a-=5
a
45
aa/=5
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    aa/=5
NameError: name 'aa' is not defined. Did you mean: 'a'?
a/=5
a
9.0
a*=5
a
45.0
a//=5
a
9.0
a**=5
a
59049.0

#Logical
a%10 and b%10 and a>b
0
a%10==0 and b%10==0 and a>b
False
a%10==0 or b%10==0 and a>b
True
a%10==0
False
a
59049.0
a=20

b=10
a%10==0
True
not a%10==0
False

#Membership
str = "abcdefg"
'a' in str
True
'h' not in str
True
'k' in str
False
l = ["sbc", 123, "hari", 3,2,1]
3 in l
True
32 in l
False
321 in l
False
123 in l
True
12 not in l
True
"hari" in l
True
t = (12,23,34,"hari",1,3,5)
12 in t
True
hari in t
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    hari in t
NameError: name 'hari' is not defined
"hari in t
SyntaxError: unterminated string literal (detected at line 1)
"hari" in t
True
2 not in t
True
s={1,2,3,"h","a","r"}
"s" in s
False
2 in s
True
'r' not in s
False
d={'a':1, 'b':2, 'c':3, 4:4}
"a" in d
True
'b' not in d
False
4 in d
True
2 in d
False

#Identity
i = [1,2,3,4,5]
j = [1,2,3,4,5]
>>> i
[1, 2, 3, 4, 5]
>>> j
[1, 2, 3, 4, 5]
>>> k=j
>>> i==j
True
>>> j==k
True
>>> i==k
True
>>> i is j
False
>>> j is k
True
>>> i is k
False
>>> i is not k
True
>>> j is not k
False
>>> 
>>> #Bitwise
>>> a=20
>>> b=10
>>> a&b
0
>>> a|b
30
>>> a^b
30
>>> a,,b
SyntaxError: invalid syntax
>>> a<<
SyntaxError: invalid syntax
>>> a<<b
20480
>>> a>>b
0
