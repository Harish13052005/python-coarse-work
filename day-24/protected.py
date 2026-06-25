# Protected

'''
class Instagram:
    def __init__(self):
        self._post=[]

    @property
    def accesspost(self):
        return self._post

    @accesspost.setter
    def accesspost(self, newpost):
        self._post.append(newpost)


dinesh = Instagram()
print(dinesh.accesspost)
dinesh.accesspost = 'class and object'
print(dinesh.accesspost)
'''


# Inheretence in OOPS

# single inheretence

'''
class whatsappv1:
    def message(self):
        print("you can send messages to anyone")
class whatsappv2(whatsappv1):
    def calls(self):
        print("you can do video and audi cakks")

harish = whatsappv1()
print("v1 - harish")
harish.message()

naresh = whatsappv2()
print("v2 - naresh")
naresh.message()
naresh.calls              
'''

# multiple inheretence

'''
class whatsappv1:
    def message(self):
        print("you can send messages to anyone")
class whatsappv2:
    def calls(self):
        print("you can do video and audi chats")
class whatsappv3:
    def media(self):
        print("you can share your  photo and videos")
class whatsappv4(whatsappv1, whatsappv2, whatsappv3):
    def status(self):
        print("you can share status for 24 hours")

harish = whatsappv1()
print("v1 - harish")
harish.message()
# harish.calls()
# harish.media()
# harish.status()

naresh = whatsappv2()
print("v2 - naresh")
# naresh.message()
naresh.calls()
# naresh.media()
# naresh.status()

rishi = whatsappv3()
print("v3- rishi")
# rishi.message()
# rishi.calls()
rishi.media()
# rishi.status()

vamsi = whatsappv4()
print("v4- vamsi")
vamsi.message()
vamsi.calls()
vamsi.media()
vamsi.status()
'''

# Multi level inheretence
'''
class whatsappv1:
    def message(self):
        print("you can send messages to anyone")
class whatsappv2(whatsappv1):
    def calls(self):
        print("you can do video and audi chats")
class whatsappv3(whatsappv2):
    def media(self):
        print("you can share your  photo and videos")
class whatsappv4(whatsappv3):
    def status(self):
        print("you can share status for 24 hours")

harish = whatsappv1()
print("v1 - harish")
harish.message()
#harish.calls()
#harish.media()
#harish.status()

naresh = whatsappv2()
print("v2 - naresh")
naresh.message()
naresh.calls()
#naresh.media()
#naresh.status()

rishi = whatsappv3()
print("v3- rishi")
rishi.message()
rishi.calls()
rishi.media()
#rishi.status()

vamsi = whatsappv4()
print("v4- vamsi")
vamsi.message()
vamsi.calls()
vamsi.media()
vamsi.status()
'''

# Hierarchical inheretence

'''
class whatsappv1:
    def message(self):
        print("you can send message")
class whatsappv2(whatsappv1):
    def emojis(self):
        print("you can send emojis")
class whatsappv3(whatsappv1):
    def stickers(self):
        print("you can send stickers")
class whatsappv4(whatsappv1):
    def status(self):
        print("you can hide your chats")

harish = whatsappv1()
print("v1 - harish")
harish.message()
#harish.emojis()
#harish.stickers()
#harish.status()

naresh = whatsappv2()
print("v2 - naresh")
naresh.message()
naresh.emojis()
#naresh.stickers()
#naresh.status()

rishi = whatsappv3()
print("v3- rishi")
rishi.message()
#rishi.emojis()
rishi.stickers()
#rishi.status()

vamsi = whatsappv4()
print("v4- vamsi")
vamsi.message()
#vamsi.emojis()
#vamsi.stickers()
vamsi.status()

'''

# Hybris inheretence

'''
class whatsappv1:
    def message(self):
        print("you can send message")
class whatsappv2(whatsappv1):
    def emojis(self):
        print("you can send emojis")
class whatsappv3(whatsappv1):
    def stickers(self):
        print("you can send stickers")
class whatsappv4(whatsappv3,whatsappv2):
    def status(self):
        print("you can hide your chats")

harish = whatsappv1()
print("v1 - harish")
harish.message()
#harish.emojis()
#harish.stickers()
#harish.status()

naresh = whatsappv2()
print("v2 - naresh")
naresh.message()
naresh.emojis()
#naresh.stickers()
#naresh.status()

rishi = whatsappv3()
print("v3- rishi")
rishi.message()
#rishi.emojis()
rishi.stickers()
#rishi.status()

vamsi = whatsappv4()
print("v4- vamsi")
vamsi.message()
vamsi.emojis()
vamsi.stickers()
vamsi.status()
'''

# Accessing the parent class methods

class wp1:
    def status(self):
        print("you can upload images / videos")
class wp2(wp1):
    def status(self):
        super().status()
        print("you can react and reply")
class wp3(wp2):
    def status(self):
        super().status()
        print("you can like and reshare")

harish = wp1()
harish.status()

rishi = wp2()
rishi.status()

vamsi = wp3()
vamsi.status()


# in case of multiple inheretence
'''
class wp1:
    def status(self):
        print("you can upload images / videos")
class wp2:
    def status(self):
        super().status()
        print("you can react and reply")
class wp3(wp2, wp1):
    def status(self):
        wp1.status(self)
        wp2.status(self)
        print("you can like and reshare")

harish = wp3()
harish.status()
'''
