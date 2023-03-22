# A program to look at loops in python
# Give the player some help:
# Only allow 3 tries
# Bug handled

import random

random_number = random.randint(1, 10)
guess = 0
max_tries = 3
num_tries = 0

while guess != random_number and num_tries < max_tries:
    guess = input("Guess my random number: ")
    num_tries += 1
    guess = int(guess)
    if guess < random_number:
        print('Too Low')
    else:
        print('Too High')
if guess == random_number:
    print("You guesssed right !!")
else:
    print("You guesssed WRONG !!")
