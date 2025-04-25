def countVowels(text):
    vowels = 'aeiou'

    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count

text = input("Enter a string: ")
count1 = countVowels(text)
print(count1)







# count = sum(1 for char in text.lower() if char in vowels)