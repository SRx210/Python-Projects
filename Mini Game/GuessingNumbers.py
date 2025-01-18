import random

number_to_guess = random.randrange(100)
guess_counter = 7

while guess_counter > 0:
    user_number = int(input(f"Enter a number to guess ({guess_counter} chances left): "))

    if user_number == number_to_guess:
        print(f"Yayy!!, you have guessed the number {number_to_guess} correctly!")
        break
    elif user_number < number_to_guess:
        print("Your guessed number is less")
    elif user_number > number_to_guess:
        print("Your guessed number is higher")

    guess_counter -= 1

    if guess_counter == 0:
        print(f"Oops! Your chances are over. The number was {number_to_guess}.")
        break
