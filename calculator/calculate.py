#create a function for each operation and return the value , so the reuslt of the value can be reuse
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
# i creatyed a dictionary where i added all the symbols as key and the functions as values
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
history = {}
def calcualtor():
    keep_calculating = True
    
    num1 = float(input("Enter your first number:\n"))
    while keep_calculating:
        for signs in operations:
            print(signs)
        operator = ""
        while True:
            operator = input("Enter the operation you want do\n")
            if operator in "+-*/":
                break
        num2 = float(input("Enter the next number:\n"))
        result = operations[operator](num1, num2)
        print(f"{num1} {operator} {num2} = {result}")
        next_step = input("if you want to continue type yes or start a new calculation type no\n").lower()
        if next_step == "yes":
            num1 = result
        else:
            keep_calculating = False
            history["key1"] = f"{num1} {operator} {num2} = {result}"
            print("\n"*100)
            print(history["key1"])
            calcualtor()
print(history)
calcualtor()



# Program asks the user to type the first number.
# Program asks the user to type a mathematical operator (a choice of "+", "-", "*" or "/")
# Program asks the user to type the second number.
# Program works out the result based on the chosen mathematical operator.
# Program asks if the user wants to continue working with the previous result.
# If yes, program loops to use the previous result as the first number and then repeats the calculation process.
# If no, program asks the user for the fist number again and wipes all memory of previous calculations.
# Add the logo from art.py