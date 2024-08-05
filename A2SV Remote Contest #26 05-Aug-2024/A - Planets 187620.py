# Problem: A - Planets - https://codeforces.com/gym/540348/problem/A

t = int(input())

for _ in range(t):
    n, c = map(int, input().split())
    orbits = list(map(int, input().split()))
    
    freq = {}
    for orbit in orbits:
        if orbit in freq:
            freq[orbit] += 1
        else:
            freq[orbit] = 1
    
    min_cost = 0
    for orbit, count in freq.items():
        min_cost += min(count, c)
    
    print(min_cost)
