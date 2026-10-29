import random
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "IT'S A DRAW!!!"
    elif c_score == 0:
        return "YOU LOSE, OPPONENT HAS A BLACKJACK!!!"
    elif u_score == 0:
        return "YOU WIN WITH A BLACKJACK!!!"
    elif u_score > 21:
        return "YOU WENT OVER, YOU LOSE!!!"
    elif c_score > 21:
        return "OPPONENT WENT OVER, YOU WIN!!!"
    elif u_score > c_score:
        return "YOU WIN!!!"
    else:
        return "YOU LOSE!!!"
def play_blackjack():
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False
    #Deal the user and computer 2 cards each using deal_card() and append().
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"your card are : {user_cards}; the sum of your card: {user_score}")
        print(f"computer's first card: {computer_cards[0]}")
        if computer_score == 0 or user_score == 0 or user_score > 21:
            is_game_over = True
        else:
            next_card = input("Type 'yes' to deal another card or 'no' to pass\n").lower()
            if next_card == "yes":
                user_cards.append(deal_card())
            else:
                is_game_over = True
    while computer_score < 17 and computer_score != 0:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print("*" * 100)
    print(f"your final hand: {user_cards}; total: {user_score}")
    print("*" * 100)
    print(f"computer final hand: {computer_cards}=; total: {computer_score}")
    print("*" * 100)
    print(compare(user_score, computer_score))
    print("*" * 100)
    start_again = input("type yes to start over or type no to end game\n").lower()
    while start_again == "yes":
        print("\n"*100)
        play_blackjack()

play_blackjack()

# Create a deal_card() function that uses the List below to return a random card.
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#
# Remember that 11 is the Ace.
#
#  Hint 5
# Deal the user and computer 2 cards each using deal_card() and append().
# user_cards = []
#
# computer_cards = []
#
#  Hint 6
# Create a function called calculate_score() that takes a List of cards as input and returns the sum of all the cards in the List as the score. Google the sum() function to help you do this.
#  Hint 7
# Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
#  Hint 8
# Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to Google to find the documentation on the Python built-in functions append() and remove().
# https://developers.google.com/edu/python/lists#list-methods
#
#  Hint 9
# Call the functioncalculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
#  Hint 10
# If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
#  Hint 11
# The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
#  Hint 12
# Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
#  Hint 13
# Create a function called compare() and pass in the user_score and computer_score.
# If the computer and user both have the same score, then it's a draw.
# If the computer has a blackjack (0), then the user loses.
# If the user has a blackjack (0), then the user wins.
# If the user_score is over 21, then the user loses.
# If the computer_score is over 21, then the computer loses.
# If none of the above, then the player with the highest score wins.
#  Hint 14
# Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.