#solution_python1_chapter03.py
"A solution to Chapter 3's exercise"

import random

#here's a "pragma" to switch execution modes depending on circumstances
LIVE_MODE=False
if LIVE_MODE:
    magic_number=random.randint(1, 100)
else:
    magic_number=50

MAX_GUESSES=5
counter=0

while True:
    guess = input("Please guess a number between 1 and 100:  ")
    counter += 1

    #we've captured the guess "from the wild", let's clean it up and test it.

    #this block uses the break keyword  in an if/else block
    clean_guess = guess.strip()
    if not clean_guess.isdigit():
        print("C'mon  {} is not an integer".format(clean_guess))
        break
    else:
        clean_guess = int(clean_guess)

    #this block uses the break keyword  in an if/elif block	
    if clean_guess < 0:
        print("Your guess needs to be at least 0")
        break
    elif clean_guess > 100:
        print("Your guess is over 100.  Please try again")
        break

    #here, we take advantage of the fact that only one suite can execute	
    if int(guess) == magic_number:
        print("Yea!  You guessed the correct number, {}.".format(magic_number))
        break
    elif counter >= MAX_GUESSES:
        print("Sorry, but you've run out of guesses")
        break
    elif int(guess) < magic_number:
        print("Good try, but you're a bit low.")
    else:
        print("Getting there, but you're on the high side.")