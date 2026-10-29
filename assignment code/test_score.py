students = {
    "Rose": [45, 70, 95],
    "Micheal": [55, 40, 66],
    "Philip": [79, 72, 96],
    "Eliza": [80, 55, 80],
    "Simon": [53, 70, 67]
}

def average_score(name):
    if name in students:
        result = sum(students[name]) / len(students[name])
        average = round(result, 2)
        print(f"{name} has an average of {average}")
    else:
        print("Student Name not found!!!")

def add_score(name, score):
    if name in students:
        students[name].append(score)
        print(f"Added {score} to {name}. New scores: {students[name]}")
    else:
        print("Student Name not found!!!")
def view_scores(name):
    if name in students:
        print(f"{name}: {students[name]}")
    else:
        print("Student Name not found!!!")
def delete_student(name):
    if name in students:
        del students[name]
    else:
        print("Student Name not found!!!")
# Map menu choices to functions
function_map = {
    "1": add_score, # Choice 1 adds score
    "2": average_score, # Choice 2 calculates average
    "3": view_scores,
    "4": delete_student
}

while True:
    print("\n--- Student Records ----")
    print("1. Add new score")
    print("2. Calculate Average")
    print("3. print out a student's score")
    print("4. delete a student record")
    print("5. Exit")

    choice = input("Enter the number of your choice: ") # keep as string

    if choice == "5":
        print("Goodbye!")
        break
    elif choice in function_map:
        name = input("Enter the name of student: ")

        if choice == "1": # add_score needs 2 args
            score = float(input("Enter score: "))
            function_map[choice](name, score)
        elif choice == "2": # average_score needs 1 arg
            function_map[choice](name)
        elif choice == "3":
            function_map[choice](name)
        elif choice == "4":
            function_map["4"](name)
    else:
        print("Invalid choice, try again")