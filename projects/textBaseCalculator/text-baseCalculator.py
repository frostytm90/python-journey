# Text-Based Calculator Code with Comments

# Function to get a valid number input from the user
def get_number(number):
    while True:
        # Prompt the user to enter a number
        operand = input("Number " + str(number) + ":")
        try:
            # Try converting the input to a float
            return float(operand)
        except:
            # If conversion fails, print an error message
            print("Invalid input. Please enter a valid number.")

# Get the first number from the user
operand = get_number(1)
# Get the second number from the user
operand2 = get_number(2)
# Get the operation sign from the user
sign = input("Sign: ")

# Initialize the result variable
result = 0

# Perform the calculation based on the operation sign
if sign == "+":
    # Addition
    result = operand + operand2
elif sign == "-":
    # Subtraction
    result = operand - operand2
elif sign == "*":
    # Multiplication
    result = operand * operand2
elif sign == "/":
    # Division
    if operand != 0 and operand2 != 0:
        result = operand / operand2
    else:
        # Handle division by zero
        print("Division by zero")
elif sign == "**":
    # Exponentiation
    result = operand ** operand2
else:
    # Handle invalid operation signs
    print("Invalid sign. Please enter a valid sign (+, -, *, /, **).")

# Print the result of the calculation
print(result)

# Comments for Future Improvement:
# - Add input validation for the operation sign to ensure valid inputs.
# - Refactor the code to modularize the arithmetic operations into separate functions for better readability.
# - Improve division by zero handling to give a clearer error message.
# - Allow the user to perform multiple calculations without restarting the program by adding a loop.
