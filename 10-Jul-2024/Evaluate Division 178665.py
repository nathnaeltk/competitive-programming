# Problem: Evaluate Division - https://leetcode.com/problems/evaluate-division/

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        
        # Building the graph
        for i, (a, b) in enumerate(equations):
            adj[a].append((b, values[i]))
            adj[b].append((a, 1 / values[i]))
        
        def bfs(source: str, target: str) -> float:
            if source not in adj or target not in adj:
                return -1.0
            
            q = deque([(source, 1.0)])
            visit = set([source])
            
            while q:
                n, w = q.popleft()
                
                if n == target:
                    return w
                
                for neighbor, weight in adj[n]:
                    if neighbor not in visit:
                        q.append((neighbor, w * weight))
                        visit.add(neighbor)
            
            return -1.0
        
        return [bfs(q[0], q[1]) for q in queries]