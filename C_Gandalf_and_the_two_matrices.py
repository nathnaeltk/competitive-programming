from math import inf

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

v = []
for i in range(n - 1):
    for j in range(m - 1):
        if a[i][j] == 1 and a[i + 1][j] == 1 and a[i][j + 1] == 1 and a[i + 1][j + 1] == 1:
            v.append((i, j))

b = [[0] * m for _ in range(n)]
for i in range(len(v)):
    x, y = v[i]
    b[x][y] = 1
    b[x + 1][y] = 1
    b[x][y + 1] = 1
    b[x + 1][y + 1] = 1

z = all(a[i][j] == b[i][j] for i in range(n) for j in range(m))

if z:
    print(len(v))
    for i in range(len(v)):
        print(v[i][0] + 1, v[i][1] + 1)
else:
    print(-1)
