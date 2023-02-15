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
import random
choices = [rock,paper,scissors]
print("WELCOME TO THE ROCK PAPER AND SCISSORS GAME!!!")
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors "))
computer_choice = random.randint(0,2)
print("You chose")
print(choices[user_choice])
print("Computer chose")
print(choices[computer_choice])
if user_choice == 0:
  if computer_choice == 0:
    print("Draw")
  elif computer_choice == 1:
    print("You Lose")
  elif computer_choice == 2:
    print("You Win!")
elif user_choice == 1:
  if computer_choice == 0:
    print("You Win!")
  elif computer_choice == 1:
    print("Draw")
  elif computer_choice == 2:
    print("You Lose")
elif user_choice == 2:
  if computer_choice == 0:
    print("You Lose")
  elif computer_choice == 1:
    print("You Win!")
  elif computer_choice == 2:
    print("Draw")
else:
  print("Invalid Input")
print("Thankyou for playing")


