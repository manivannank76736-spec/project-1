try:
    # Accept two numbers from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # operator
    operator = input("Enter an operator (+, -, *, /): ")
    
    #Compute and display the result
    if operator == "+":
        print(f"Result: {num1} + {num2} = {num1 + num2}")
    elif operator == "-":
        print(f"Result: {num1} - {num2} = {num1 - num2}")
    elif operator == "*":
        print(f"Result: {num1} * {num2} = {num1 * num2}")
    elif operator == "/":
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            print(f"Result: {num1} / {num2} = {num1 / num2}")
    else:
        print("Error: Invalid operator. Please choose +, -, *, or /.")

except ValueError:
    print("Error: Invalid input. Please enter valid numbers only.")
