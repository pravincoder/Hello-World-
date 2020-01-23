# Creating a small 3 time guessing game (1 to 9)
import random

guess_taken = 0

# Using random module to get a random number every time

number = random.randint(1, 9)
print("Well, I am guessing a number  between 1 to 9 ")

for guess_taken in range(4):
    print("Take a guess !")
    guess = (input())
    guess = int(guess)
    # Letting the user know about his guess
    if guess < number:
        print("Pls think more higher number !")
    if guess > number:
        print("Pls think a smaller number! ")
    if guess == number:
        break

if guess == number:
    print("Wow you won")
    guess_taken = str(guess_taken + 1)
# If player losses the turns
if guess != number:
    print("The Number was ", number)
