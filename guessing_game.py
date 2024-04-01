import random

number = random.randint(1,100)
attempts = 1

print("\nNUMBER GUESSING GAME\n")
print("Guess the number between 1 and 100:")
while True:
    try:
        user_guess = int(input("> "))
        if user_guess not in range(1,101):
            print("Number out of range! Please insert a number between 1 an 100:")
        elif user_guess == number:
            print(f"You've Won in {attempts} attempts! {number} is right.")
            break
        elif user_guess > number:
            print(f"Your number is higher than mine.")
        elif user_guess < number:
            print(f"Your number is lower than mine.")
        attempts += 1
    except ValueError:
        print("Value not a number!")
        break