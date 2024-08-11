# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def dfs(self, node, parents, ancestors):

        if len(ancestors[node]) != 0:
            return ancestors[node]

        for p in parents[node]:
            ancestors[node].add(p)
            ancestors[node].update(self.dfs(p, parents, ancestors))
        return ancestors[node]

    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        parents = [] 
        ancestors = []
        for i in range(n):
            parents.append([])
            ancestors.append(set())
        for edge in (edges):
            parents[edge[1]].append(edge[0])
        for node in range(n):
            self.dfs(node, parents, ancestors)
        return map(lambda x: sorted(list(x)), ancestors)