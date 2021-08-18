import random
number = random.randint(1, 10)
guess = ''

print("Hello! Welcome to Guess the Number!")
name = input("\nWhat is your name? ")
print("\nExcellent " + name + "! Let's play!")
print("\nYou may type 'quit' to quit the game at anytime.\n")


while guess != 'quit':
    guess = input("\nPlease guess a number between 1 and 10: ")
    guess = int(guess)

    if guess > number:
        print("Your guess is too high")

    if guess < number:
        print("Your guess is too low.")

    if guess == number:
        break
    
print('You are correct! \nYou guessed the mystery number: ' + str(number))
