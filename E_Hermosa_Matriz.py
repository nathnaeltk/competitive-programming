for _ in range(int(input())):
    n = int(input())
    q = n
    n_squared = n * n
    ascending_range = list(range(1, n_squared + 1))

    matrix = []
    for i in range(n):
        row = ascending_range[i * n : (i + 1) * n]
        matrix.append(row if i % 2 == 0 else row[::-1])

    for row in matrix:
        print(' '.join(map(str, row)))
