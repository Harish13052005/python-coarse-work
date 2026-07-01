import re

'''
# a.b
pattern = r'h.t\b'
text = 'hot hit hate hitter hoot heart h@t h#t h$t'

res = re.findall(pattern, text)
print(res)
'''

'''
# ^a -- starts with a
pattern = r'^h'
text = 'hot hit hate hitter hoot heart h@t h#t h$t'

res = re.findall(pattern, text)
print(res)
'''

'''
# a$ -- ends with a
pattern = r'j$'
text = 'hot hit hate hitter hoot heart h@t h#t h$t sjaesdghj'

res = re.findall(pattern, text)
print(res)
'''
'''
# 'ab*'
pattern = r'ab*\b'
text = 'a abb abba abab aaaabbbb abababbb'

res = re.findall(pattern, text)
print(res)
'''
'''
# 'ab+'
pattern = r'ab+\b'
text = 'a abb abba abab aaaabbbb abababbb'

res = re.findall(pattern, text)
print(res)
'''

'''
# 'ab?'
pattern = r'ab?\b'
text = 'a abb abba abab aaaabbbb abababbb'

res = re.findall(pattern, text)
print(res)
'''
'''
pattern = r'[a-z]{4,5}'
text = 'a abb abba abab aaaabbbb abababbb'

res = re.findall(pattern, text)
print(res)
'''

'''
pattern = r'[a-z]{5}'
text = 'a abb abba abab aaaabbbb abababbb'

res = re.findall(pattern, text)
print(res)
'''


'''
pattern = r'[a-z]{5}'
text = 'a abb abba abab aaaabbbb abababbb'

res = re.findall(pattern, text)
print(res)
'''

'''
pattern = r'(python)'
text = 'py pyth python pythonon pypyththonon pythonpython'

res = re.findall(pattern, text)
print(res)
'''

# valid name or not

'''
    #import re

pattern = r'^[a-zA-Z]{2,15}( [a-zA-Z]{2,15})+$'

text = input("Enter the Text: ")

res = re.fullmatch(pattern, text)

print("Valid format" if res else "Invalid format")
'''

# valid email or not
'''
pattern = r'^[a-zA-Z0-9._]+@[a-zA-Z0-9._]+\.[a-zA-Z]{2,}$'

text = input("Enter the Email: ")

res = re.fullmatch(pattern, text)

print("Valid format" if res else "Invalid format")
'''


# valid number or not
'''
pattern = r'^(?:\+91|0)?[6-9]\d{9}$'

text = input("Enter the Number: ")

res = re.fullmatch(pattern, text)

print("Valid format" if res else "Invalid format")
'''

# Valid Password or not
'''
pattern = r'^(?-.*[A-Z]) (?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}'

text = input("Enter the Password: ")

res = re.fullmatch(pattern, text)

print("Valid format" if res else "Invalid format")
'''

pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'

text = input("Enter the Password: ")

res = re.fullmatch(pattern, text)

print("Valid format" if res else "Invalid format")
