n, s = map(int, input().split())
a = list(map(int, input().split()))

max_ans = 0
left = 0
right = 0

for left in range(len(a)):

    right = left
    while right<len(a) and sum(a[left:right]) <= s:
        max_ans = max(max_ans, right-left)
        right += 1
    

print(max_ans)