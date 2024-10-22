# Problem: Almost Prime - https://codeforces.com/problemset/problem/26/A

n = int(input())
is_prime = [True] * (n + 1)
primes = []

for i in range(2, n + 1):
    if is_prime[i]:
        primes.append(i)
        for multiple in range(i * 2, n + 1, i):
            is_prime[multiple] = False

distinct_prime_factors_count = [0] * (n + 1)

for prime in primes:
    for multiple in range(prime, n + 1, prime):
        distinct_prime_factors_count[multiple] += 1

almost_prime_count = sum(1 for count in distinct_prime_factors_count if count == 2)

print(almost_prime_count)
