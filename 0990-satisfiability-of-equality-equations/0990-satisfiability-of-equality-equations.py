from collections import defaultdict

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        equals = defaultdict(set)
        not_equals = []
        for eq in equations:
            if eq[1] == "=":
                equals[eq[0]].add(eq[3])
                equals[eq[3]].add(eq[0])
            else:
                not_equals.append((eq[3],eq[0]))
                
                
        for key in equals:
            dfs(key,key,set(),equals)
                
        
        for node1,node2 in not_equals:
            if node1 == node2:
                return False
            if node1 in equals and node2 in equals[node1]:
                return False
        return True
                
def dfs(start,curr,visited,equals):
    if curr in visited:
        return
    visited.add(curr)
    equals[start].add(curr)
    for v in list(equals[curr]):
        dfs(start,v,visited,equals)