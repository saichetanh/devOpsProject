text = input("Enter a string: ")

if text == text[::-1]:
    print("It's a palindrome!")
else:
    print("It's NOT a palindrome.")
