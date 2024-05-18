a, m = map(int, input().split())

if a == 1:
    print(-1)
if a % 2 == 0:
    print((a // 2) if (a // 2) % m == 0 else (a // 2) + 1)
else:
    print(-1)
