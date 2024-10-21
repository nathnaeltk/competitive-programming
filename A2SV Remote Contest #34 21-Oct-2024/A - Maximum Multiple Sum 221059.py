# Problem: A - Maximum Multiple Sum - https://codeforces.com/gym/559568/problem/A

# Input
t = int(input())  # number of test cases
test_cases = [int(input()) for _ in range(t)]

# Process each test case
results = []
for n in test_cases:
    max_sum = 0
    best_x = 2
    for x in range(2, n + 1):
        k = n // x
        current_sum = x * k * (k + 1) // 2
        if current_sum > max_sum:
            max_sum = current_sum
            best_x = x
    print(best_x)
