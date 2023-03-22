# A program to look at loops in python

import random

random_number = random.randint(1, 10)
guess = 0

while guess != random_number:
    guess = input("Guess my random number: ")
    guess = int(guess)
print("You guesssed right !!")
