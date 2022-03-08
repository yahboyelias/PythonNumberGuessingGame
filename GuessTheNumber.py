import random

# User Input/Number Randomness
number_input = int(input('Guess a number between 1 and 50: '))
correct_number = random.randrange(1, 50)

# Number Logic
while number_input != correct_number:

    if number_input > correct_number:
        print('You need to guess lower. Try again')
        number_input = int(input('\nGuess a number between 1 and 50: '))
    elif number_input < correct_number:
        print('You need to guess higher. Try again')
        number_input = int(input('\nGuess a number between 1 and 50: '))

# Runs if number_input == correct_number
if number_input == correct_number:
    print(f'You guessed the correct number! Which was {correct_number}')
