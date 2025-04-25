numbers= list(map(int, input("Enter numbers separated by spaces: ").split()))
count = 0
for i in numbers:
    count =count + i

print(count)

print("Sum of numbers",sum(numbers))