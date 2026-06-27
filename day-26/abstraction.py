from abc import ABC, abstractmethod

class BankAccount(ABC):
    def checkbalance(self):
        print("you can checkout your balance")

    def viewhistory(self):
        print("you can view your history")

    def userinfo(self):
        print("you can view your details")

    def transactions(self):
        print("you can tranfer your money through net banking")

    @abstractmethod
    def deposit(self):
        pass
    
    @abstractmethod
    def withdraw(self):
        pass

class SavingsAccount(BankAccount):

    def deposit(self):
        print("you can deposit money to SA")


    def withdraw(self):
        print("you can withdraw from SA")


class CurrentAccount(BankAccount):

    def deposit(self):
        print("you can deposit money to CA")


    def withdraw(self):
        print("you can withdraw from CA")
        
class SalaryAccount(BankAccount):

    def deposit(self):
        print("you can deposit money to SAA")


    def withdraw(self):
        print("you can withdraw from SAA")

class FixedDepositAccount(BankAccount):

    def deposit(self):
        print("you can deposit money to FDA")


    def withdraw(self):
        print("you can withdraw from FDA")

class ZerobalanceAccount(BankAccount):

    def deposit(self):
        print("you can deposit money to ZBA")


    def withdraw(self):
        print("you can withdraw from ZBA")

print(" Savings Account")
harish = SavingsAccount()
harish.checkbalance()
harish.viewhistory()
harish.userinfo()
harish.transactions()
harish.deposit()
harish.withdraw()
print()

print(" Fixed Deposit Account")
rishi = SavingsAccount()
rishi.checkbalance()
rishi.viewhistory()
rishi.userinfo()
rishi.transactions()
rishi.deposit()
rishi.withdraw()
print()

print(" Salary Account")
vamsi = SavingsAccount()
vamsi.checkbalance()
vamsi.viewhistory()
vamsi.userinfo()
vamsi.transactions()
vamsi.deposit()
vamsi.withdraw()
print()

print(" current Account")
sahith = CurrentAccount()
sahith.checkbalance()
sahith.viewhistory()
sahith.userinfo()
sahith.transactions()
sahith.deposit()
sahith.withdraw()
print()

