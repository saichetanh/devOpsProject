def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

num = int(input("Enter a number: "))
# print(f"The factorial of {num} is {factorial(num)}")
print(factorial(num))



# import math
#
# num = int(input("Enter a number: "))
# print(f"The factorial of {num} is {math.factorial(num)}")
