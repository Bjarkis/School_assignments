import random
number = random.randint(0, 100)

print("Hi-Lo Number Guessing Game: Between 0 and 100 inclusive.")
print()

guess = int(input("Guess a number: "))

while 0 <= guess <= 100:
    if guess > number:
        print("Guessed Too High.")
    elif guess < number:
        print("Guessed To Low.")
    else:
        print("You guessed it. The number was: ", number)
        break
    guess = int(input("Guess a number: "))
else:
    print("You quit early, the number was: ", number)