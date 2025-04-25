def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

N = int(input("Enter the range (N): "))

primes = [num for num in range(2, N + 1 ) if is_prime(num)]

print("Prime numbers:", primes)
