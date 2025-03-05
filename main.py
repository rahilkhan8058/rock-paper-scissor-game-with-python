import random

def play_game():
    select = ["rock", "paper", "scissor"]

    while True:
        try:
            total_match = int(input("How many matches do you want to play? "))
            if total_match <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    user_score = 0
    computer_score = 0

    for match_number in range(1, total_match + 1):
        print(f"\n Match {match_number} of {total_match}")

        while True:
            user_press = input("Enter rock, paper, or scissor (or type 'quit' to exit): ")
            if user_press == "quit":
                print("Thanks for playing! ")
            if user_press not in select:
                print("INVALID INPUT! Please enter rock, paper, or scissor.")
                continue  
            break  

        computer_select = random.choice(select)

        print(f"\n USER SELECTED: {user_press}")
        print(f" COMPUTER SELECTED: {computer_select}")

        if user_press == computer_select:
            print(" TIE! No points awarded.")
        elif (user_press == "rock" and computer_select == "scissor") or \
             (user_press == "paper" and computer_select == "rock") or \
             (user_press == "scissor" and computer_select == "paper"):
            print(" USER WINS THIS ROUND!")
            user_score += 1
        else:
            print(" COMPUTER WINS THIS ROUND!")
            computer_score += 1

    print("\n...........***FINAL RESULTS***............")
    print(f" User Wins: {user_score}")
    print(f" Computer Wins: {computer_score}")

    if user_score > computer_score:
        print("\n USER WINS THE GAME ")
    elif user_score < computer_score:
        print("\n COMPUTER WINS THE GAME  ")
    else:
        print("\n IT'S A TIE ")

while True:
    play_game()
    while True:
        play_again = input("\nDo you want to play again? (yes/no): ")
        if play_again == "yes":
            break  
        elif play_again == "no":
            print("Thanks for playing!")
            exit()
        else:
            print("Invalid input, please enter 'yes' or 'no'.")
