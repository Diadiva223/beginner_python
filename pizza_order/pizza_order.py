print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0
if size == "s":
    bill = 15
    print("small pizza is $15")
    if pepperoni == "y":
        bill += 2
        print(f"with pepperoni, your bill is ${bill}")
    if extra_cheese == "y":
        bill += 1
        print(f"with extra cheese you will be paying a total of ${bill}")
elif size == "m":
    bill = 20
    print("medium pizza is $20")
elif size == "l":
    bill = 25
    print("large pizza is $25")
    if pepperoni == "y":
        bill += 3
        print(f"with pepperoni, your bill is ${bill}")
    if extra_cheese == "y":
        bill += 1
        print(f"with extra cheese you will be paying a total of ${bill}")
else:
    print("choose a correct option")
