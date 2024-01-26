import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def display_result(user_choice, computer_choice, result):
    print(f"\nYour choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")
    print(result)

def rock_paper_scissors_game():
    user_score = 0
    computer_score = 0

    while True:
        print("\nRock, Paper, Scissors Game")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Quit")

        user_choice_index = input("Enter your choice (1/2/3/4): ")

        if user_choice_index == '4':
            print("\nGame Over. Final Scores:")
            print(f"You: {user_score}")
            print(f"Computer: {computer_score}")
            break

        choices = ['rock', 'paper', 'scissors']
        user_choice = choices[int(user_choice_index) - 1]

        computer_choice = random.choice(choices)

        result = determine_winner(user_choice, computer_choice)
        display_result(user_choice, computer_choice, result)

        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1

if __name__ == "__main__":
    rock_paper_scissors_game()
