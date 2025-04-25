# num1 = float(input("Enter the first number: "))
# operation = input("Enter an operation (+, -, *, /): ")
# num2 = float(input("Enter the second number: "))
#
# if operation == '+':
#     result = num1 + num2
# elif operation == '-':
#     result = num1 - num2
# elif operation == '*':
#     result = num1 * num2
# elif operation == '/':
#     result = num1 / num2
# else:
#     result = "Invalid operation!"
#
# print("Result:", result)


expression = input("Enter an arithmetic expression (e.g., 5 + 3): ")

# Evaluating the expression
result = eval(expression)

print("Result:", result)
