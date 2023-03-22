# A program to look at loops in python
# Give the player some help:

import random

random_number = random.randint(1, 10)
guess = 0

while guess != random_number:
    guess = input("Guess my random number: ")
    guess = int(guess)
    if guess < random_number:
        print('Too Low')
    else:
        print('Too High')
print("You guesssed right !!")
