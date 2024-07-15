# Problem: c - Reposts - https://codeforces.com/gym/533316/problem/c

class Solution:

	def solve(self, reposts, n):
		lookup = {'polycarp': 1}

		for repost in reposts:
			name1, _, name2 = repost.split(" ")
			lookup[name1] = 1 + lookup[name2]
		print(max(lookup.values()))
		return


t = 1
sol = Solution()
while t:
    n = int(input())
    reposts = []
    for _ in range(n):
        reposts.append(input().lower())
    sol.solve(reposts, n)
    t -= 1