
def get_number(number):
    while True:
        operand = input("Number " + str(number) + ":")
        try:
            return float(operand)
        except:
            print("Invalid input. Please enter a valid number.")
    

operand = get_number(1)
operand2 = get_number(2)
sign = input("Sign: ")

result = 0
if sign == "+":
    result = operand + operand2
elif sign == "-":
    result = operand - operand2
elif sign == "*":
    result = operand * operand2
elif sign == "/":
    if operand or operand2 != 0:
        result = operand / operand2
    else:
        print("Division by zero")
elif sign == "**":
    result = operand ** operand2
else:
    print("Invalid sign. Please enter a valid sign (+, -, *, /, **).")

print(result)