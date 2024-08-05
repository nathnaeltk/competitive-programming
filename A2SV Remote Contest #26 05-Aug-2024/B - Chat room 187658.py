# Problem: B - Chat room - https://codeforces.com/gym/540348/problem/B

s = input().strip()
target = "hello"
j = 0

for i in range(len(s)):
    if s[i] == target[j]:
        j += 1
    if j == len(target):
        print("YES")
        break
else:
    print("NO")
