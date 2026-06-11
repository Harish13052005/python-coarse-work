p = input()
if len(p) >= 8:
    s=set()
    for i in p:
        if i.isupper():
            s.add('u')
        elif i.islower():
            s.add('l')
        elif i.isdigit():
            s.add('d')
        else:
            s.add('s')
    if len(s)==4:
        print("strong password")
    else:
        print("weak password")

else:
    print("weak password")
