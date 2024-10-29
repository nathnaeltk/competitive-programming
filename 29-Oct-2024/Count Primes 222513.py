# Problem: Count Primes - https://leetcode.com/problems/count-primes/

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        # Create a boolean list "is_prime" to track whether a number is prime
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes
        
        # Mark multiples of primes as non-prime
        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i*i, n, i):
                    is_prime[j] = False
        
        # Count primes by counting True values in the is_prime list
        return sum(is_prime)
