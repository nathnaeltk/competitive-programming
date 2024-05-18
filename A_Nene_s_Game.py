num_tests = int(input())

for _ in range(num_tests):
    seq_length, num_queries = list(map(int, input().split()))
    sequence = list(map(int, input().split()))
    query_values = list(map(int, input().split()))

    for value in query_values:
        if value >= sequence[0]:
            print(sequence[0] - 1, end=' ')
        else:
            print(value, end=' ')
    print()
