# Problem: Find if Path Exists in Graph - https://leetcode.com/problems/find-if-path-exists-in-graph/

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for ui, vi in edges:
            graph[ui].append(vi)
            graph[vi].append(ui)
            
        visited = set([source])
        def dfs(node, visited):
            if node is destination:
                return True
            
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    if dfs(neighbor, visited):
                        return True
            return False
        return dfs(source, set())
        