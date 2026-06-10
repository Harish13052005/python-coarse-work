budget = int(input())

if budget > 50000:
    print("you can go for a trip")
elif budget > 20000:
    print("you can go for a pub")
elif budget > 10000:
    print("you can go for the shopping")
elif budget > 5000:
    print("you can go for a cafe")
elif budget > 2000:
    print("you can go for a movie")
elif budget > 500:
    print("you can recharge your phone")
else:
    print("Take Rest")
