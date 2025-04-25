from collections import Counter

# Taking input from the user
elements = input("Enter list elements separated by spaces: ").split()

# Counting the frequency of each element
frequency = Counter(elements)

print("Frequency of elements:", frequency)
