import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choices = [rock,paper,scissors]
computer_choice = random.choice(choices)
user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n")

if user_choice == "0":
    user_choice = 0
    print(choices[user_choice])
    print("Computer chose:\n")
    print(computer_choice)
    if computer_choice == rock:
        print("It's a draw")
    elif computer_choice == paper:
        print("You lose")
    elif computer_choice == scissors:
        print("You Win!")
elif user_choice == "1":
    user_choice = 1
    print(choices[user_choice])
    print("Computer chose:\n")
    print(computer_choice)
    if computer_choice == rock:
        print("You win!")
    elif computer_choice == paper:
        print("It's a draw")
    elif computer_choice == scissors:
        print("You lose")
elif user_choice == "2":
    user_choice = 2
    print(choices[user_choice])
    print("Computer chose:\n")
    print(computer_choice)
    if computer_choice == rock:
        print("You lose")
    elif computer_choice == paper:
        print("You win!")
    elif computer_choice == scissors:
        print("It's a draw")
else:
    print("Invalid input")

