def count_unique_chars(s):
    return len(set(s))

string = input("Enter a string: ")
print(set(string))
print(f"Total number of unique characters: {count_unique_chars(string)}")