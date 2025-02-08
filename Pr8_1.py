#Write a Python program which will throw exception if the value entered by user is less than zero.

x = int(input("Enter number: "))
try:
    if x < 0:
        raise ValueError("Value is less than zero")
except ValueError as e:
    print(e)