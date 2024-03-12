q = int(input())
for _ in range(q):
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    B.sort()


    # regular greed algorithm, smallest matched with biggest, second smallest with second biggest...
    x = 0
    for i in range(1, n + 1):
        x += abs(B[m - i] - A[i - 1])
  
    # when B>A, matching the best remaining item
    res = x
    for i in range(1, n + 1):
        x = x - abs(A[n - i] - B[m - (n - i) - 1]) + abs(A[n - i] - B[i - 1])
        res = max(res, x)

    print(x)