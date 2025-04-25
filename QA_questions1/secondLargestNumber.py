# numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
# numbers.sort(reverse=True)
# second_largest = numbers[1] if len(set(numbers)) > 1 else "No second largest number"
# print("The second largest number is:", second_largest)


numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
numbers.sort()
print("The second largest number is:", numbers[-2])
