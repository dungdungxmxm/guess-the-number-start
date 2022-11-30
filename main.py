#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import art
import random
print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

number = random.randint(0, 100)
print(number)
mode = input("Choose a difficulty. Type 'easy' or 'hard': ")
attempts = 0

if mode == 'easy':
  attempts = 10
elif mode == 'hard':
  attempts = 5

guess = 0
while guess != number:
  print(f"You have {attempts} attempts remaining to guess the number.")
  guess = int(input("Make a guess: "))
  if guess > number:
    print("Too high.")
    print("Guess again.")
    print("------------------------------------------")
  elif guess < number:
    print("Too low.")
    print("Guess again.")
    print("------------------------------------------")
  else:
    print(f"You got it! The answer is was {number}")
    break;
  attempts -= 1
  if(attempts == 0):
    print("You lose!")
    break;
    
  
