from collections import Counter

text = input("Enter a string: ")

char_count = Counter(text)

for char in text:
    if char_count[char] == 1:
        print("The first non-repeating character is:", char)
        break
else:
    print("No non-repeating character found!")
