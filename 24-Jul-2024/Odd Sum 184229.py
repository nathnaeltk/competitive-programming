# Problem: Odd Sum - https://codeforces.com/problemset/problem/797/B

n = int(input())
a = list(map(int, input().split()))

total_sum = 0
min_odd_positive = float('inf')
max_odd_negative = -float('inf')

for num in a:
    if num > 0:
        total_sum += num
        if num % 2 == 1: 
            min_odd_positive = min(min_odd_positive, num)
    elif num < 0:
        if num % 2 == 1:
            max_odd_negative = max(max_odd_negative, num)

if total_sum % 2 == 1:
    print(total_sum)
else:
    options = []
    options.append(total_sum - min_odd_positive)
    options.append(total_sum + max_odd_negative)

    print(max(options))