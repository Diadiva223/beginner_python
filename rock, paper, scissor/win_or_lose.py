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
image = [rock, paper, scissors]

#option = ["rock", "paper", "scissors"]
user = input("Enter your name:\n")
user_input = int(input("Type 1, 2 or 3 "))
print(image[user_input])
computer = random.randint(0, 2)
#print(option[randon_option])
print(f"computer choose {computer}")
print(image[computer])

if user_input == 0 and computer == 2:
    print(f"{user} wins")
elif user_input == 1 and computer == 0:
    print(f"{user} wins")
elif user_input == 2 and computer == 1:
    print(f"{user} wins")
elif user_input == computer:
    print("its a draw")
else:
    print(f"{user}, you lose!")