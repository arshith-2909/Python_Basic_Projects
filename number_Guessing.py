import random

low = 1
high = 100

answer = random.randint(low,high)
guesses = 0

print("A Number Guessing Game ")

while True:
    guess = int(input(f"Select a number between {low} and {high} : "))
    
    guesses += 1
    if guess < low or guess > high:
        print("The number is out of range")
        print(f"Please select a number between {low} and {high} :")
    elif guess < answer:
        print("Too low! Try again!")
    elif guess > answer:
        print("Too high! Try again!")
    else:
        print("CORRECT!")
        print(f"NUmber of tries : {guesses}")
        break