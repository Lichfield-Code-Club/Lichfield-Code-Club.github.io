# Guess a letter
import random

words = ['Hello','World','the','sun','is','shining','everyone','is','pleased','its','not','raining']
random_number = random.randint(0,len(words)-1)

a_word = words[random_number]
guess_me = [x for x in a_word]
my_guess = ['_' for x in a_word]

while my_guess != guess_me:
    letter = input("Guess a letter ")
    letter = letter[0]
    if letter in guess_me:
        for i,c in enumerate(guess_me):
            if c == letter:
                my_guess[i] = guess_me[i]
    print('My Guess:', ''.join(my_guess))
if my_guess == guess_me:
    print('Good guess')
else:
    print('Bad guess')