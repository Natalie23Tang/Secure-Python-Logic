#Guess the random number game
#number between 1 and 20

import random 

secret = random.randint(1,20) # a<= scret <= b
tries = 0
guess = 0 # start with a value that cannot be the secret (since secret is 1...20)

print("I'm thinking of a number between 1 and 20")

while guess != secret:
    try:
        guess = int(input("Take a guess: " )) # try converting to an integer
        tries += 1

    except ValueError: # error when the input is letter or symbol
        print("Please enter a number") 
        continue # back to the beginning of the loop

    if guess < 1 or guess > 20:
        print("That number is out of range. Try again.")

    elif guess < secret: 
        print("too low, try again.")

    elif guess > secret: 
        print("too high, try again.")

    else:
        print(f"You got it right in {tries} tries !")
        break 
