import time
import os

t = 3 # 3 seconds

def sleep():
    print("\nSleeping for 3 seconds...\n")
    time.sleep(t)


def sum(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x*y


def divide(x, y):
    return x/y

def square(x):
    return x*x


def square_root(x):
    return x**0.5


def cls():
    os.system('cls') # clear console in windows


def exit():
    print("Goodbye!")
    cls()


while True:
    cls()
    print(f"CALCULATOR APP\n")
    print(f"1. Addition")
    print(f"2. Subtraction")
    print(f"3. Multiplication")
    print(f"4. Division")
    print(f"5. Square")
    print(f"6. Square Root\n")

    choice = input("Select operation (1/2/3/4/5/6) or type 'quit' to exit: ")
    print(f"\n")
    cls()

    if choice == "1":
        print(f"1. Addition")
        x = int(input("Enter your first number: "))
        y = int(input("Enter your second number: "))
        print(f"The Result from {x} + {y} is {sum(x, y)}.")
    elif choice == "2":
        print(f"2. Subtraction")
        x = int(input("Enter your first number: "))
        y = int(input("Enter your second number: "))
        print(f"The Result from {x} - {y} is {subtract(x, y)}.")
    elif choice == "3":
        print(f"3. Multiplication")
        x = int(input("Enter your first number: "))
        y = int(input("Enter your second number: "))
        print(f"The Result from {x} * {y} is {multiply(x, y)}.")
    elif choice=="4":
        print(f"4. Division")
        x = int(input("Enter your first number: "))
        y = int(input("Enter your second number: "))
        print(f"The Result from {x} / {y} is {divide(x, y)}.")
    elif choice=="5":
        print(f"5. Square")
        x = int(input("Enter your number: "))
        print(f"The Square of {x} is {square(x)}.")
    elif choice=="6":
        print(f"6. Square Root")
        x = int(input("Enter your number: "))
        print(f"The Square of {x} is {square_root(x)}.")
    elif choice=="quit":
        exit()
        break
    else:
        print("Invalid input! Please try again.")

    sleep()
else:
    print("Invalid Input.")
    print("you can also type 'quit' to exit the program.")