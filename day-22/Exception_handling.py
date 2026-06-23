# Exception handling: Try -> Except -> Else -> Finally
'''
try:
    a = int(input("Enter the age:"))
except ValueError:
    print("Enter the age in a number format:")
else:
    print("Age:", a)
finally:
    print("Thank You")
'''

# Handling Multiple Errors - method1

'''
try:
   # a = int(input("Enter te age:"))
   # print(12/0)
   # print(b)
   # print(13+'14')

    d = {1:1, 2:2, 3:3, 4:4}
   # print(d[5])

    l = [1,2,3]
   # print(l[5])

except ValueError:
    print("Enter the age in a digit format:")
except ZeroDivisionError:
    print("can't didvide with zero")
except NameError:
    print("Define the Variable")
except TypeError:
    print("Add the same Datatypes")
except KeyError:
    print("Key is not present")
except IndexError:
    print("Index out of range")
else:
    print("Age:",a)
finally:
    print("Thank You")
'''
# Handling multiple errors - Method2
'''
try:
   # a = int(input("Enter te age:"))
   # print(12/0)
   # print(b)
   # print(13+'14')

    d = {1:1, 2:2, 3:3, 4:4}
   # print(d[5])

    l = [1,2,3]
   # print(l[5])

except (ValueError, ZeroDivisionError, NameError, TypeError, KeyError, IndexError) as e :
    print("Error occured", e)
else:
    print("No error occured")
finally:
    print("Thank You")
'''

# Handling all errors - Optimal method

'''
try:
   # a = int(input("Enter te age:"))
   # print(12/0)
   # print(b)
   # print(13+'14')

    d = {1:1, 2:2, 3:3, 4:4}
   # print(d[5])

    l = [1,2,3]
   # print(l[5])

except Exception as e :
    print("Error occured", e)
else:
    print("No error occured")
finally:
    print("Thank You")
'''

# User defined Exception

try:
    amt = int(input("enter the amount to withdraw:"))
    if amt <0:
        raise Exception("Enter amt greater than zero")

except Exception as e:
    print("Error occured:", e)
else:
    print("No Error occured")
finally:
    print("Thank You")
            
