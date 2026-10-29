# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
import art
print(art.logo)
def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bidder = 0
    for bid_person in bidding_dictionary:
        bid_number = bidding_dictionary[bid_person]
        if bid_number > highest_bidder:
            highest_bidder = bid_amount
            winner = bid_person
    print(f"the winner is {winner}, with a bid amount of {highest_bidder}")



bidders = {}
more_bidder = True
while more_bidder:
    name = input("Type in your name:\n")
    bid_amount = int(input("type in your bid amount\n"))
    bidders[name] = bid_amount
    right_answer = True
    while right_answer:
        add = input("do you want another add bid?\nType yes or no:\n")
        if add == "no":
            more_bidder = False
            right_answer = False
            find_highest_bidder(bidders)
            # highest_value = max(bidders, key=bidders.get)
            # highest_name =bidders[highest_value]
            # print(highest_value)
        elif add == "yes":
            right_answer =False
            print("\n" * 100)
        else:
            print("you type in a wrong answer")

