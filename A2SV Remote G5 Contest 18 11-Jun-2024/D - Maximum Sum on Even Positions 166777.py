# Problem: D - Maximum Sum on Even Positions - https://codeforces.com/gym/528793/problem/D

def max_even_index_sum(test_cases):
    results = []
    for _ in range(test_cases):
        size = int(input())
        nums = list(map(int, input().split()))

        sum_even_indices = sum(nums[i] for i in range(0, size, 2))
        max_sum = sum_even_indices
        min_even_diff = 0
        min_odd_diff = 0
        current_diff = 0

        for i in range(size):
            if i % 2 == 1:
                current_diff += nums[i]
                max_sum = max(max_sum, sum_even_indices + current_diff - min_odd_diff)
                min_odd_diff = min(min_odd_diff, current_diff)
            else:
                current_diff -= nums[i]
                max_sum = max(max_sum, sum_even_indices + current_diff - min_even_diff)
                min_even_diff = min(min_even_diff, current_diff)

        results.append(max_sum)
    
    for result in results:
        print(result)

test_cases = int(input())
max_even_index_sum(test_cases)
