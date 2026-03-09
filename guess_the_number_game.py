#Guess the number game
#number between 1 and 20

number = 13
count = 0
print("Guess a number between 1 and 20")


while True :
    try:
        guess = int(input("Take a guess: "))  # try converting to an integer
        count += 1

    except ValueError: # error when the input is letter or symbol
        print("Please enter a number") 
        continue # back to the beginning of the loop

    if guess < 1 or guess > 20:
        print("That number is out of range. Try again.")
        
    elif guess < number: 
        print("too low, try again.")

    elif guess > number: 
        print("too high, try again.")

    else:
        guess == number 
        print(f"You got it right in {count} tries !")
        break 