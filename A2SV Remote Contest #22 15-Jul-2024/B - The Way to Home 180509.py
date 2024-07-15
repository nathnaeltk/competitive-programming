# Problem: B - The Way to Home - https://codeforces.com/gym/533316/problem/B

dp = [0]
n, d = map(int, input().split())
s = input()

for i in range(1, len(s)):

    if s[i] == '0':
        dp.append(10 ** 10)
    else:

        mn = 10 ** 10
        for j in range(max(0, i - d), i):
            mn = min(mn, dp[j])
        if mn == 10 ** 10:
            dp.append(10 ** 10)
        else:    
            dp.append(mn + 1)
abc = 1
if dp[-1] == 10 ** 10:
    print(-1)
else:
    print(dp[-1])

    