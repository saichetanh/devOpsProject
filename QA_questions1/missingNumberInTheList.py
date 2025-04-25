numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

n = max(numbers)
full_set = set(range(1, n + 1))
missing_numbers = full_set - set(numbers)

if missing_numbers:
    print("The missing numbers are:", sorted(missing_numbers))
    print("FULL SET", full_set)
else:
    print("No missing numbers!")
