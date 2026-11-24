print("Lets play a guessing game.")
import random
secret = random.randint(1, 50)
attempts = 5
while attempts >= 0:
    guess = int(input("Enter your guess from 1 - 50: "))
    attempts = attempts - 1
    if (guess - 48) >= secret:
        print("ICE COLD")
    elif (guess - 30) >= secret:
        print("COLD")
    elif (guess - 20) >= secret:
        print("WARM")
    elif (guess - 10) >= secret:
        print("HOT")
    elif (guess - 5) >= secret:
        print("BURNING HOT")
    elif guess > 50:
        print("INVALID GUESS")
    else:
        print("CORRECT! YOU WIN!")
        break
