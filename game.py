import random

# -------- ASCII ART --------
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _________
---'   _______)
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

ascii_art = {
    "rock": rock,
    "paper": paper,
    "scissors": scissors
}

# -------- FUNCTIONS --------
def get_user_choice():
    print("\nChoose one:")
    print("1. rock")
    print("2. paper")
    print("3. scissors")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        return "rock"
    elif choice == "2":
        return "paper"
    elif choice == "3":
        return "scissors"
    else:
        print(" Invalid choice! Try again.")
        return None


def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])


def decide_winner(user, computer):
    if user == computer:
        return "draw"
    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        return "user"
    else:
        return "computer"


# -------- MAIN GAME --------
print(" Welcome to Rock Paper Scissors (ASCII Edition)!")
print(" Best of 3 — First to 2 wins\n")

user_wins = 0
computer_wins = 0
round_no = 1

while user_wins < 2 and computer_wins < 2:
    print(f"\n--- Round {round_no} ---")

    user_choice = None
    while user_choice is None:
        user_choice = get_user_choice()

    computer_choice = get_computer_choice()

    print("\n You chose:")
    print(ascii_art[user_choice])

    print(" Computer chose:")
    print(ascii_art[computer_choice])

    winner = decide_winner(user_choice, computer_choice)

    if winner == "user":
        print("🎉 You win this round!")
        user_wins += 1
    elif winner == "computer":
        print("🎉 Computer wins this round!")
        computer_wins += 1
    else:
        print(" It's a draw!")

    print(f"\n Best of 3 Score → You: {user_wins} | Computer: {computer_wins}")
    round_no += 1


# -------- FINAL RESULT --------
print("\n============================")
if user_wins == 2:
    print(" CONGRATULATIONS! You won the Best of 3!")
else:
    print(" Computer won the Best of 3!")
print("============================")

input("\nPress Enter to exit...")
