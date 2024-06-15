# Problem: Operations on graphs - https://basecamp.eolymp.com/en/problems/2472

import sys
input = sys.stdin.read

data = input().split()

n = int(data[0])
k = int(data[1])

from collections import defaultdict

graph = defaultdict(set)

results = []

index = 2

for _ in range(k):
    operation = int(data[index])
    
    if operation == 1:
        u = int(data[index + 1])
        v = int(data[index + 2])
        graph[u].add(v)
        graph[v].add(u)
        index += 3
    elif operation == 2:
        u = int(data[index + 1])
        if u in graph:
            results.append(" ".join(map(str, sorted(graph[u]))))
        else:
            results.append("")
        index += 2

print("\n".join(results))
