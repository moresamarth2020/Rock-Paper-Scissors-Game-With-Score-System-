import random

def rock_paper_scissors():
    print("----- Rock–Paper–Scissors Game -----\n")

    choices = ["rock", "paper", "scissors"]
    user_score = 0
    computer_score = 0

    while True:
        user_choice = input("Enter rock, paper, scissors or quit: ").lower()

        if user_choice == "quit":
            print("\nGame Over!")
            print(f"Your Score: {user_score}")
            print(f"Computer Score: {computer_score}")

            if user_score > computer_score:
                print("🎉 You WIN the game!")
            elif user_score < computer_score:
                print("😔 Computer wins the game.")
            else:
                print("🤝 It's a TIE!")
            break

        if user_choice not in choices:
            print("❌ Invalid choice. Try again.\n")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("🤝 It's a tie!\n")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("🎉 You win this round!\n")
            user_score += 1
        else:
            print("😔 Computer wins this round!\n")
            computer_score += 1

rock_paper_scissors()
