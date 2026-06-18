Python 3.11.8 (tags/v3.11.8:db85d51, Feb  6 2024, 22:03:32) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

==== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-18/lambda.py ===
7
8
13
7
13
6
# lambda functions


==== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-18/lambda.py ===
welcome to python course Harish
welcome to python course rishi
welcome to python course vamshi

==== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-18/lambda.py ===
180.0
3240.0
3960.0

==== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-18/lambda.py ===

==== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-18/lambda.py ===
Traceback (most recent call last):
  File "C:/Users/HARISH/Desktop/python-coarse-work/day-18/lambda.py", line 26, in <module>
    print(gst(price, tax))
NameError: name 'price' is not defined. Did you mean: 'print'?

==== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-18/lambda.py ===
23456
12.2
286163.2

==== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-18/lambda.py ===
12345
12.5
15431.25

==== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-18/lambda.py ===
12345
0.1
1234.5

# greatest

==== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-18/lambda.py ===
19
134
1823

==== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-18/lambda.py ===
4 is even
32 is even
41 is odd

==== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-18/lambda.py ===
120
63
250

==== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-18/lambda.py ===
12345
10.5
12962.25

==== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-18/lambda.py ===
12345
10.5
1296.225

# login and buy

==== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-18/lambda.py ===
you can buy product

==== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-18/lambda.py ===
product is out of stock

==== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-18/lambda.py ===
 Login to buy a product

==== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-18/lambda.py ===
[1, 8, 27, 64, 125, 216, 343]

==== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-18/lambda.py ===
[1, 8, 27, 64, 125, 216, 343]
['Harish', 'Rishi', 'Vamshi']

==== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-18/lambda.py ===
[1, 8, 27, 64, 125, 216, 343]
['Harish', 'Rishi', 'Vamshi']
[2, 4, 6, 8]

==== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-18/lambda.py ===
[2, 4, 6, 8]

==== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-18/lambda.py ===
[6, 7, 8, 9]
[2, 4, 6, 8]

==== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-18/lambda.py ===
[6, 7, 8, 9]
[2, 4, 6, 8]
[3, 6, 9]
# filter

# Reduce


==== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-18/lambda.py ===
Traceback (most recent call last):
  File "C:/Users/HARISH/Desktop/python-coarse-work/day-18/lambda.py", line 102, in <module>
    p = reduce(lambda pro, i: pro*l)
TypeError: reduce expected at least 2 arguments, got 1

==== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-18/lambda.py ===
Traceback (most recent call last):
  File "C:/Users/HARISH/Desktop/python-coarse-work/day-18/lambda.py", line 102, in <module>
    p = reduce(lambda pro, i: pro*l, l)
  File "C:/Users/HARISH/Desktop/python-coarse-work/day-18/lambda.py", line 102, in <lambda>
    p = reduce(lambda pro, i: pro*l, l)
TypeError: can't multiply sequence by non-int of type 'list'
>>> 
==== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-18/lambda.py ===
45 362880
>>> 
==== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-18/lambda.py ===
Traceback (most recent call last):
  File "C:/Users/HARISH/Desktop/python-coarse-work/day-18/lambda.py", line 113, in <module>
    mi = reduce(lambda ma,i: max if max<i else i,l)
  File "C:/Users/HARISH/Desktop/python-coarse-work/day-18/lambda.py", line 113, in <lambda>
    mi = reduce(lambda ma,i: max if max<i else i,l)
TypeError: '<' not supported between instances of 'builtin_function_or_method' and 'int'
>>> 
==== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-18/lambda.py ===
Traceback (most recent call last):
  File "C:/Users/HARISH/Desktop/python-coarse-work/day-18/lambda.py", line 113, in <module>
    mi = reduce(lambda ma,i: max if max<i else i,l)
  File "C:/Users/HARISH/Desktop/python-coarse-work/day-18/lambda.py", line 113, in <lambda>
    mi = reduce(lambda ma,i: max if max<i else i,l)
TypeError: '<' not supported between instances of 'builtin_function_or_method' and 'int'
>>> 
==== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-18/lambda.py ===
45 362880 9 1
>>> 
>>> # dict one
>>> 
==== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-18/lambda.py ===
{'dinesh': 80, 'nagendra': 40, 'naresh': 60, 'sahith': 70, 'subbu': 50}
{'nagendra': 40, 'subbu': 50, 'naresh': 60, 'sahith': 70, 'dinesh': 80}
{'subbu': 50, 'sahith': 70, 'naresh': 60, 'nagendra': 40, 'dinesh': 80}
{'dinesh': 80, 'sahith': 70, 'naresh': 60, 'subbu': 50, 'nagendra': 40}
