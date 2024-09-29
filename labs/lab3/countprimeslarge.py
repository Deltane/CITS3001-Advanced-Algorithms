def count_primes(N):
    if N < 2:
        return 0

    is_prime = [True] * (N + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers

    p = 2
    while p * p <= N:
        if is_prime[p]:
            for i in range(p * p, N + 1, p):
                is_prime[i] = False
        p += 1

    # Count the primes
    prime_count = sum(is_prime)
    return prime_count


# Read input
N = int(input().strip())
# Get the count of primes
print(count_primes(N))
