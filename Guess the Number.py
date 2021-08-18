import random
#import time...then have a wait time after line 10
number = random.randint(1, 10)
guess = ''
number_of_guesses = 0

print("Hello! Welcome to Guess the Number!")
print("\nYou may type 'quit' to quit the game at anytime.\n")
name = input("\nWhat is your name? ")
print("\nOkay " + name + "! Let's play! \nI am thinking of a number between 1 and 10.")

print("I have my number.")


while number_of_guesses < 3:
    guess = input("\nGuess a number between 1 and 10: ")
    guess = int(guess)
    number_of_guesses += 1

    if guess == 'q':
        print("Thank you for playing. Goodbye!")
        break

    if guess > number:
        print("Your guess is too high")
    elif guess < number:
        print("Your guess is too low.")
    elif guess == number:
        print("\nYou guessed the number in " + str(number_of_guesses) + ' tries!')
    elif number_of_guesses > 3:
        print("\nYou did not guess the number. The number was " + str(number))

print("Thank you again for playing.")
