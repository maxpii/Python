import random

upper_range = input("Welcome to my guessing game!\nWhat is the highest number that can be guessed? ")
if not upper_range.isdigit() or int(upper_range) <= 0:
    print("Please enter a positive integer next time")
    quit()
upper_range = int(upper_range)
random_num = random.randint(1, upper_range)
guesses = 0
while True:
    guesses += 1
    user_guess = input("Make a guess (q to quit): ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    elif user_guess == 'q':
        print("have a nice day")
        quit()
    else:
        print("Type a number please")
        continue


    if (user_guess == random_num):
        print("yay you got it right\n")
        break
    else:
        if user_guess > random_num:
            print("Sorry, you were above the number!")
        else:
            print("You were below the number")
print(f"You got it in {guesses} guesses")