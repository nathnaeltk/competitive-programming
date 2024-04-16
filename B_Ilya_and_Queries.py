s = input().strip()
n = len(s)
cumulative_counts = [0] * n
cumulative_counts[0] = 0

for i in range(1, n):
    val = 1 if s[i] == s[i - 1] else 0
    cumulative_counts[i] = cumulative_counts[i - 1] + val

num_queries = int(input())

for _ in range(num_queries):
    start_index, end_index = map(int, input().split())
    result = cumulative_counts[end_index - 1] - cumulative_counts[start_index - 1]
    print(result)