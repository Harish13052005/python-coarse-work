# python does not support method overloading.


# method overriding
'''
class hotstar:
    def __init__(self, name):
        self.name = name
        print(f"hii {self.name} welcome to hotstar")
    def login(self):
        print("you can login")
    def dashboard(self):
        print("you can see the dashboard items")
    def search(self):
        print("you can search")
    def languages(elf):
        print("you can select the languages")
    def playcontrollers(self):
        print("you can pause and play the video")

    def ads(self):
        print("ads will run")
    def movies(self):
        print("you have limited access to movies")
    def sports(self):
        print("limited time you can watch sports")
    def quality(self):
        print("you have limited quality")

class premium(hotstar):
    def __init__(self, name):
        self.name = name
        print(f"Hi {self.name}, welcome to premium hotstar")
    def ads(self):
        print("ads will not run")
    def movies(self):
        print("you have unlimited access to movies")
    def sports(self):
        print("unlimited time you can watch sports")
    def quality(self):
        print("you have better quality")



print("Non premium user:")
harish = hotstar('harish')
harish.login()
harish.dashboard()
harish.search()
harish.languages()
harish.playcontrollers()
harish.ads()
harish.movies()
harish.sports()
harish.quality()

print()

print("premium user:")
rishi = premium('rishi')
rishi.login()
rishi.dashboard()
rishi.search()
rishi.languages()
rishi.playcontrollers()
rishi.ads()
rishi.movies()
rishi.sports()
rishi.quality()
'''

# Operator overloading

class number:
    def __init__(self, n):
        self.n = n
    def __add__(self, other):
        return self.n + other.n
    def __sub__(self, other):
        return self.n - other.n
    def __mul__(self, other):
        return self.n * other.n
    def __truediv__(self, other):
        return self.n / other.n
    def __eq__(self, other):
        return self.n == other.n
    def __lt__(self, other):
        return self.n < other.n
    def __gt__(self, other):
        return self.n > other.n
    def __str__(self):
        return str(self.n)

n1 = number(10)
n2 = number(20)
print(n1+n2)
print(n1-n2)
print(n1*n2)
print(n1/n2)
print(n1==n2)
print(n1<n2)
print(n1>n2)
print(n1,n2)

