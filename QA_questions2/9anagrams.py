word1 = input("String1 ").lower()
word2 = input("String2 ").lower()
if sorted(word2) == sorted(word1):
    print("anagram")
else:
    print("not anagram")
