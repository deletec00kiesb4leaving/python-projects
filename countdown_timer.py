import time

try:
    user_input = int(input("You are setting a timer for how many seconds? "))
    print(f"Timer set for {user_input} seconds.")
    while user_input != 0:
        print(f"Timer: {user_input} left.")
        user_input -= 1
        time.sleep(1)
    else:
        print(f"Timer: {user_input}!\nTime's Up!")
except ValueError:
    print("Value not a number! Exiting program.")