import random
import art
from game_data import data
CURRENT_SCORE = 0
IS_GAME_RUNNING = True
#create a compare function that compares the number of followers
def compare(a_option, b_option, fan_count):
    global CURRENT_SCORE
    global IS_GAME_RUNNING
    a_option = first_option['follower_count']
    b_option = second_option['follower_count']
    if choice == "a" and a_option > b_option:
        CURRENT_SCORE += 1
        print(f"You're right! current score: {CURRENT_SCORE}")
    elif choice == "b" and b_option > a_option:
        CURRENT_SCORE += 1
        print(f"You're right! current score: {CURRENT_SCORE}")
    else:
        IS_GAME_RUNNING = False
        print(f"Sorry, that's wrong final score: {CURRENT_SCORE}")

print(art.logo)
#randomly pick a data from our game data module
second_option = random.choice(data)
while IS_GAME_RUNNING:
    first_option = second_option
    #i convert the v to str, loop through the key value pairs and keep all key that is
    #not follower_count
    values = [str(v) for k, v in first_option.items() if k != "follower_count"]
    #i insert a in value at position 1 and from to the value at position 2
    values[1] = f"a {values[1]}"
    values[2] = f"from {values[2]}"
    print("Compare A: " + ", ".join(values))
    print(art.vs)
    second_option = random.choice(data)
    values = [str(v) for k, v in second_option.items() if k != "follower_count"]
    values[1] = f"a {values[1]}"
    values[2] = f"from {values[2]}"
    print("Against B: " + ",".join(values))
    if first_option == second_option:
        second_option = random.choice(data)
    choice = input("who has more followers: Type A or B\n").lower()
    print("\n" * 100)
    print(art.logo)
    compare(first_option, second_option, choice)