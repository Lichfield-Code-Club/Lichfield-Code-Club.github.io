# Guess a word

import random
random_number = random.randint(1, 10)

words = ['Hello','World','the','sun','is','shining','everyone','is','pleased','its','not','raining']

word_to_guess = words[random_number]
my_guess = '__________'
while my_guess != word_to_guess:
    my_guess = input("Guess my word ")
if my_guess == word_to_guess:
    print('Good guess')
else:
    print('Bad guess')