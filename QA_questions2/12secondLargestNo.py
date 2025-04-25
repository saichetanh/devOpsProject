numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

numbers.sort()
print("largest number is:", numbers[-2])