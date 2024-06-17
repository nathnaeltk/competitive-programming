# Problem: Maximal Network Rank - https://leetcode.com/problems/maximal-network-rank/description/

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(set)
        res = 0

        for a, b in roads:
            graph[a].add(b)
            graph[b].add(a)

        for i in range(n):
            for j in range(i+1, n):
                curr = len(graph[i]) + len(graph[j])

                if i in graph[j] or j in graph[i]:
                    curr -= 1

                res = max(res, curr)

        return res