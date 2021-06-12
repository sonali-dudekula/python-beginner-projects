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

#method 1
my_hand = None
choice = int(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors \n"))
if choice >= 3 or choice < 0 :
  print("You typed an invalid number. You lose!")
else :
  if choice == 0 :
    my_hand = rock
    print(rock)
  elif choice == 1 :
    my_hand = paper
    print(paper)
  else choice == 2 :
    my_hand = scissors
    print(scissors)

  rock_paper_scissors = [rock, paper, scissors]
  computer_choice = random.choice(rock_paper_scissors)
  print(f"Computer's choice: \n{computer_choice}")
  if my_hand == computer_choice :
    print("It's a draw.")
  elif my_hand == rock :
    if computer_choice == paper:
      print("You lose!")
    else :
      print("You Win!")
  elif my_hand == paper :
    if computer_choice == scissors :
      print("You lose!")
    else :
      print("You Win!")
  elif my_hand == scissors :
    if computer_choice == paper :
      print("You Win!")
    else :
      print("You lose!")

#method 2
game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice >= 3 or user_choice < 0 :
  print("You typed an invalid number, you lose!")
else :
  print(game_images[user_choice])

  computer_choice = random.randint(0, 2)
  print("Computer chose:")
  print(game_images[computer_choice])

  if user_choice == 0 and computer_choice == 2:
    print("You win!")
  elif computer_choice == 0 and user_choice == 2:
    print("You lose")
  elif computer_choice > user_choice:
    print("You lose")
  elif user_choice > computer_choice:
    print("You win!")
  elif computer_choice == user_choice:
    print("It's a draw")
