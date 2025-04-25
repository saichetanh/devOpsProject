numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
numbers.sort(reverse=True)
print("largest number is:", numbers[0])

numbers.sort()
print("largest number is:", numbers[-1])