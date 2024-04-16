n, x = map(int, input().split())
l = list(map(int, input().split()))

prefix_sum = 0
count = 1
for i in range(len(l)):
    prefix_sum += l[i]
    if prefix_sum <= x:
        count += 1

print(count)