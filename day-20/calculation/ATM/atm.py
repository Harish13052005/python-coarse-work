import logic as lg

if lg.login():
    print("______welcome to ATM_______")
    while True:
        lg.menu()
        ch = input("enter your choice:").lower()
        if ch == 'c':
            lg.check_balance()
        elif ch == 'd':
            lg.deposit()
        elif ch == 'w':
            lg.withdraw()
        elif ch == 'h':
            lg.history()
        elif ch == 'e':
            lg.exit()
            break
        
