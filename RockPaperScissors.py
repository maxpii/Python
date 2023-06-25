import random

options = ["rock", "paper", "scissors"]
while True:
    user_input = input("Enter an option (q to quit): ").lower()
    if user_input == 'q':
        print("Have a nice day")
        quit()
    elif user_input not in options:
        print("That is not an option")
        continue
    computer_guess = options[random.randint(0,2)]
    print(f"The computer guessed {computer_guess}")
    if user_input == computer_guess:
        print("It was a tie!")
    elif user_input == "rock":
        if computer_guess == "scissors":
            print("You won!")
        else:
            print("You lost")
    elif user_input == "scissors":
        if computer_guess == "paper":
            print("You won")
        else:
            print("You lost")
    else:
        if computer_guess == "rock":
            print("You won")
        else:
            print("You lost")