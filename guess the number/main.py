import random

EASY_LEVEL = 10
HARD_LEVEL = 5

def check_guess(user_guess, actual_number, turns):
    if user_guess > actual_number:
        print("too high")
        return turns - 1
    elif user_guess < actual_number:
        print("too low")
        return turns - 1
    else:
        print(f"You win, the random number is {actual_number}")

def choose_diffculty():
    level = input("Choose a level. Type 'easy' or 'hard'")
    if level == "easy":
        return EASY_LEVEL
    elif level == "hard":
        return HARD_LEVEL

def play():
    print("Welcome to the number guessing game")
    print("I am thinking of a number between 1 and 100")
    answer = random.randint(1, 101)
    print(answer)
    turns = choose_diffculty()

    user_input = 0
    while user_input != answer:
        print(f"You have {turns} attempts remaianing!")
        user_input = int(input("Guess a number"))
        turns = check_guess(user_input, answer, turns)

        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif user_input != answer:
                print("Guess again.")

play()