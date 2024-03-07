n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

i, j = 0, 0
count = 0

while i < n and j < m:
    if a[i] < b[j]:
        i += 1
        count += 1
    else:
        print(count)
        j += 1

while j < m:
    print(count)
    j += 1