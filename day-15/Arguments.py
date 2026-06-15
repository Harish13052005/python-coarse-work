# Arguments

# 1. Positional arguments
'''
def display(name, email, pwd):
    print("Name:", name)
    print("Email:", email)
    print("Password:", pwd)

display('Harish', 'harish@gmail.com', 'harish@123')
display('harish@gmail.com', 'harish@123', 'harish@123')
display('harish@123', 'harish@gmail.com', 'harish@gmail.com')
'''

#2. keyword argumets
'''
def display(name, email, pwd):
    print("Name:", name)
    print("Email:", email)
    print("Password:", pwd)

display(name='Harish', email='harish@gmail.com', pwd='harish@123')
display(email='harish@gmail.com', pwd='harish@123', name='Harish')
display(pwd='harish@123', email='harish@gmail.com', name='Harish')
'''

#3. default arguments
'''
def display(name, email='', pwd=''):
    print("Name:", name)
    print("Email:", email)
    print("Password:", pwd)

display('Harish','harish@gmail.com','harish@123')
display('harish@gmail.com', 'harish@123',)
display('harish@123', 'Harish')
'''

#4. variable lenguth argument
'''
def display(*names):
    print("Name:", names)

display('Harish', 'sahith', 'rishi', 'vamshi')
display('Harish')
display('Harish', 'rishi')
display('Rishi', 'sahith')
'''

# keyword variable length arguments

def display(**names):
    print("Name:", names)

display(k1='Harish', k2='sahith', k3='rishi', k4='vamshi')
display(k1='Harish')
display(k1='Harish',k2='rishi')
display(k1='Rishi', k2='sahith')
