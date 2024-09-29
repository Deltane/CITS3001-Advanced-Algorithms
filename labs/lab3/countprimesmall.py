def count_primes(N):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    prime_count = 0
    for num in range(2, N + 1):
        if is_prime(num):
            prime_count += 1
    return prime_count

def main():
    N = int(input())  # Directly read the value of N from input
    print(count_primes(N))  # Print only the result

main()