from art import logo
from random import randint

EASY = 10
HARD = 5

def check_number(user_guess, answer, tries):
    if user_guess > answer:
        print("Too high.")
        return tries - 1
    elif user_guess < answer:
        print("Too low.")
        return tries - 1
    else:
        print(f"You got it! The answer was {answer}")

def difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == 'easy':
        return EASY
    else:
        return HARD

def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")

    turns = difficulty()

    guess = 0

    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_number(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")

game()