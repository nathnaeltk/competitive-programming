# Problem: Detonate the Maximum Bombs - https://leetcode.com/problems/detonate-the-maximum-bombs/description/

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        adj = collections.defaultdict(list)

        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if i != j:
                    x1, y1, r1 = bombs[i]
                    x2, y2, r2 = bombs[j]
                    
                    d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
                    
                    if d <= r1:
                        adj[i].append(j)
                    if d <= r2:
                        adj[j].append(i)

        def dfs(i, visit):
            if i in visit:
                return 0
            visit.add(i)
            for neighbor in adj[i]:
                dfs(neighbor, visit)
            return len(visit)

        res = 0

        for i in range(len(bombs)):
            res = max(res, dfs(i, set()))

        return res