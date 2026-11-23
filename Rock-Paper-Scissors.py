import random

print("welcome to rock paper scissors game")
print()

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_images = [rock, paper, scissors]
user=0
computer=0

while True:
    user_choice = int(input("\nEnter your choice: 0 for rock, 1 for paper, 2 for scissors : "))
    computer_choice = random.randint(0, 2)

    if user_choice < 0 or user_choice > 2:
        print("Invalid input. Please enter a number between 0 and 2.")
    else:
        print(f"You chose {user_choice}")
        print(game_images[user_choice])

        print(f"Computer chose {computer_choice}")
        print(game_images[computer_choice])

        if user_choice == computer_choice:
            print("Both players selected the same. It's a tie!")
        elif ((user_choice == 0 and computer_choice == 2) or
              (user_choice == 1 and computer_choice == 0) or
              (user_choice == 2 and computer_choice == 1)):
            print("You win!")
            user=user + 1
        else:
            print("You lose!")
            computer=computer + 1

    play_again = input("\nDo you want to play again? (y/n): ")
    
    if play_again != "y":
        print("Thanks for playing! Goodbye!")
        print(f"Final Score - You: {user}, Computer: {computer}")
        break