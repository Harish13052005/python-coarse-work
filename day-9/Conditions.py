'''s = "python programming"

if "python" in s:
    print("found")
'''

'''
if s[0]=='p':
    print("True")
'''

'''
data =(['abc', '1234')
username,password = input("enter the username and password:").split()

if data == (username,password):
    print("Login Successful")
else:
    print("Invalid Login")
'''

'''
n = int(input())

if n>0:
    print("+ve")
elif n<0:
    print("-ve")
else:
    print("zero")
'''

products = {
    'laptops':0,
    'mouse':10,
    'charger':5,
    'phone':30,
    'keyboard':0
}

product = input("enter the product:")
if product in products:
    if products[product] != 0:
        print(f" You can buy {product}")
    else:
        print(f" {product} out of stock")
else:
    print(f"{product} is unavailable")

        
