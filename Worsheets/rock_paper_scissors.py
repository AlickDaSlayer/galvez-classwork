from random import randint

choice = ["rock", "paper", "scissors"]
user_input = str.lower(input("Please enter rock, paper, scissors:  "))

while user_input != "rock" and user_input != "paper" and user_input != "scissors":
    user_input = str.lower(input("Invalid input, please enter rock or paper or scissors only:  "))
computer_choice = choice[randint(0, 2)]
print("computer has chosen", computer_choice)
if (computer_choice == "rock" and user_input == "scissors") or (computer_choice == "paper" and user_input == "rock") or (computer_choice == "scissors" and user_input == "paper"):
    print("You Lose!")
elif computer_choice == user_input:
    print("Tie!")
else:
    print("You Win!")
