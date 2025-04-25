word1 = input("Enter the first word: ").strip().lower()
word2 = input("Enter the second word: ").strip().lower()

if sorted(word1) == sorted(word2):

    print("The words are anagrams!")
else:
    print("The words are NOT anagrams!")
