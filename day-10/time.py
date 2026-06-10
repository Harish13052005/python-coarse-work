hrs,min = list(map(int, input().split(':')))

if 0 <= hrs <= 23 and 0 <= mins <= 59:
    if 0 <= hrs <= 11:
        print(f'{str(hrs).zfill(2)}:{str(mins).zfill(2)} AM')
    elif hrs ==12:
        print(f'{str(hrs).zfill(2)}:{str(mins).zfill(2)} PM')
    else:
        print(f'{str(hrs-12).zfill(2)}:{str(mins).zfill(2)} PM')

    if 4<=hrs<=11:
        print("Good Morning, Have a nice day")
    elif 12 <= hrs <= 16:
        print("Good Afternoon, Have lunch")
    elif 17 <= hrs <= 19:
        print("Good Evening, Have Tea")
    elif 20 <= hrs <= 23:
        print("Good Night, Have a good sleep")
    elif 0 <= hrs <= 3:
        print("It's mid night. Have a sleep")

else:
    print("Invalid Time")
