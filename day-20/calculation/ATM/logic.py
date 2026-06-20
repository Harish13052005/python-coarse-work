data ={
    123456:{'pin':1234, 'balance':5000, 'history':[]},
    345612:{'pin':1234, 'balance':5000, 'history':[]},
    456123:{'pin':1234, 'balance':5000, 'history':[]},
    561234:{'pin':1234, 'balance':5000, 'history':[]}
    }

def login():
    global acc_num
    acc_num = int(input("enter the account number:"))
    pin = int(input("enter the pin:"))

    if acc_num in data and data[acc_num]['pin']==pin:
        print("Login Successful")
        return True
    else:
        print("login Failed")
        return False

    
def menu():
    print("[C]heck balance")
    print("[D]eposit")
    print("[W]ithdraw")
    print("[H]istory")
    print("[E]xit")

def check_balance():
    print("Current Balance:", data[acc_num]['balance'])

def deposit():
    amt = int(input("enter amount to deposit:"))
    data[acc_num]['balance'] += amt
    data[acc_num]['history'].append(f"{amt} added +++")
    print("deposit successful")

def withdraw():
    amt = int(input("enter the amount to withdraw:"))
    if data[acc_num]['balance'] >= amt:
        data[acc_num]['balance'] -= amt
        data[acc_num]['history'].append(f"{amt} withdrawn ---")
        print("withdrawn successful")
    else:
        print("Insufficient Balance")

def history():
    if data[acc_num]['history']:
        print("Transaction Details:")
        for i in data[acc_num]['history']:
            print(i)
    else:
        print(" No Transaction ")
        
def exit():
    print("Thank You")
    return 0    
