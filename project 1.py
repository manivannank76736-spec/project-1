#compute and display the result
def calculate(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
    else:
        return "Error: Invalid operator."

#title
print("----- Simple Calculator Using Python -----")
#repeates until the user enters a valid input
while True:
    choice = input("\nPress Enter to continue or type 'quit' to exit: ")

    if choice.lower() == "quit":
        print("Calculator closed. Goodbye!")
        break

    try:
#accepting two numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
#entering the operatoe
        operator = input("Enter an operator (+, -, *, /): ")

        result = calculate(num1, num2, operator)

        if isinstance(result, str):
            print(result)
        else:
            print(f"Result: {num1} {operator} {num2} = {result}")

    except ValueError:
        print("Error: Invalid input. Please enter valid numbers only.")
