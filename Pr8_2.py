#Write a python program to demonstrate use of finally and else keywords.

x = int(input("Enter number: "))
try:
    if x < 0:
        raise ValueError("Value is less than zero")
except ValueError as e:
    print(e)
else:
    print("Value is positive")
finally:
    print("Finally block excuted.")