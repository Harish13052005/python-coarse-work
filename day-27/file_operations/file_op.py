# opening a file 
'''
file = open('sample.txt', 'r')

print(file.read())
file.seek(0)
print(file.readline())
file.seek(0)
print(file.readlines())

file.close()
'''

# Handling file not found Error
'''
try:
    file = open('sample.txt', 'r')
except FileNotFoundError:
    print("No file named with that")
else:
    print(file.read())
    file.seek(8)
    print(file.readline())
    file.seek(0)
    print(file.readlines())

    file.close()
'''

# Better method
'''
with open('sample.txt', 'r') as file:
    print(file.read())
    file.seek(8)
    print(file.readline())
    file.seek(0)
    print(file.readlines())
'''

# Appending elements
'''
with open('sample.txt', 'a') as file:
    file.write('\npraneeth\nshiva\nsrikanth')

with open('samples.txt', 'a') as file:  # creates a new file samples.txt
    file.write('\npraneeth\nshiva\nsrikanth')
'''

# Writing the elements
'''
with open('sample.txt', 'w') as file:   # overwrites the existing data
    file.write('\npraneeth\nshiva\nsrikanth')

with open('samples.txt', 'w') as file:  # creates a new file samples.txt
    file.write('\npraneeth\nshiva\nsrikanth')
'''

# Read and write with r+
'''
with open('sample.txt', 'r+') as file:
    file.write("\n harish \n rishi \n sahith")
    file.seek(0)
    print(file.read())
    file.write("\n praneeth \n subbu \n nag")
    file.seek(0)
    print(file.read())
'''

# write and read with w+

'''
with open('sample.txt', 'w+') as file:
    file.write("\n praneeth \n subbu \n nag")
    file.seek(0)
    print(file.read())
'''

# append and read with a+
'''
with open('sample.txt', 'a+') as file:
    file.write("\n praneeth \n subbu \n nag")
    file.seek(0)
    print(file.read())
'''

# os module
'''
import os

# os.mkdir('sample')
os.rmdir('sample')
'''

# Regular Expression
'''
# match

import re

pattern1 = '[A-Z]'
pattern2 = '[abcde]'
text = 'abc'

res1 = re.match(pattern1, text)
res2 = re.match(pattern2, text)

print(res1.group() if res1 else "No Match Found")
print(res2.group() if res2 else "No Match Found")
'''

'''
# search

import re

pattern1 = '[A-Z]'
pattern2 = '[abcde]'
text = 'abc'

res1 = re.search(pattern1, text)
res2 = re.search(pattern2, text)

print(res1.group() if res1 else "No Match Found")
print(res2.group() if res2 else "No Match Found")
'''

'''
# findall

import re

pattern1 = '[A-Z]'
pattern2 = '[abcde]'
pattern3 = '[123456789]'
text = 'Python Programming @123_456'

res1 = re.findall(pattern1, text)
res2 = re.findall(pattern2, text)
res3 = re.findall(pattern3, text)

print(res1)
print(res2)
print(res3)
'''

'''
# finditer

import re

pattern1 = '[A-Z]'
pattern2 = '[abcde]'
pattern3 = '[123456789]'
text = 'Python Programming @123_456'

res1 = re.finditer(pattern1, text)
res2 = re.finditer(pattern2, text)
res3 = re.finditer(pattern3, text)

for i in res1:
    print(i.group(), i.start())
for i in res2:
    print(i.group(), i.start())
for i in res3:
    print(i.group(), i.start())
'''

'''
# Full match

import re

pattern = '[a-z]{9}'
text = 'akcpefgji'

res = re.fullmatch(pattern,text)

print(res.group() if res else "No Match Found")
'''

'''
# split

import re

pattern = r'[,a+yn]'
text = 'java, python, c++'

res = re.split(pattern, text)

print(res)
'''

# sub

import re

pattern = r'[0-9]{2}'
text = 'python: 34 mysql: 78 java: 55 html: 54'

res = re.sub(pattern, '**', text)

print(res)
