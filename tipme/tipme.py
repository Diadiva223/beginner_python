# print("Welcome to the tip calculator!")
# bill = float(input("What was the total bill? $"))
# tip = int(input("What percentage tip would you like to give? 10 12 15: \n"))
# people = int(input("How many people to split the bill? "))
# total_tip = bill * (tip / 100)
# total_bill = round((bill + total_tip) / people, 2)
# print(f"Each person will pay: {total_bill}")
scores = {"Alice": 85, "Bob": 92, "Charlie": 78}

highest_name = ""
highest_score = -1

for name, score in scores.items():
    if score > highest_score:
        highest_score = score
        highest_name = name
        print(highest_score)