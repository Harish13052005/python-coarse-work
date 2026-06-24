# Flipcart demo
'''
class Flipcart:
    discount = 10
    products = ['laptop','phone','mouse','charger']

    @classmethod
    def showproducts(cls):
        print(cls.products)

    def login(self,username,password):
        self.username = username
        self.password = password
        print(f"welcome to the flipcart {self.username}")

    @staticmethod
    def banner():
        print("10% discount on flipcart, shop now!")

Harish = Flipcart()
Harish.login('Harish', 'Harsih@123')
Harish.banner()
Harish.showproducts()

Flipcart.showproducts()
Flipcart.banner()
'''

# Instagram demo

'''
class Instagram:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.followers = []
        print(f"welcome to ine instagram, {self.username}")

Harish = Instagram('Harish', 'Harish@123')
'''

# dealing public, private and protected variables

class Instagram:
    def __init__(self, username, password):
        self.username = username
        self.__password = password # __ is used for initialising an attribute as private
        self._followers = []  # _ is used to initialise an attribute as protected

    def getpassword(self):
        return self.__password
    


    def setpassword(self, newpassword):
        self.__password = newpassword

Harish = Instagram('Harish', 'Harish@123')

print("Before name:",Harish.username)
Harish.username = 'Rishi'
print("After name:", Harish.username)

print("Before password:", Harish.getpassword())
Harish.setpassword('Rishi@123')
print("After password:", Harish.getpassword())

