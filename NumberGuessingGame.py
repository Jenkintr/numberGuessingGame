#Taylor Jenkins
#04-28-16

#Higher/Lower Game

#Generate random number between 1-1000.
import random
random.seed()
number = random.randint(1, 1000)
tries = 0

print ("\t\tHigher/Lower Game")
print ("\nYou must try to guess the number that")
print ("I've chosen in as few quesses as possible.\n")

#Get input from user
guess = int(input("Guess a number between 1 and 1000: "))


#Determine if number is correct and count total guesses.


while guess != number:
    if guess > number:
        print("Try again. You guessed too high.")
        guess = int(input("Guess a number between 1 and 1000: "))
        tries += 1
    elif guess < number:
        print("Try again. You guessed too low.")
        guess = int(input("Guess a number between 1 and 1000: "))
        tries += 1

print("Congratulations! You guessed correctly!")
print("It only took you ", tries, " tries!" )

