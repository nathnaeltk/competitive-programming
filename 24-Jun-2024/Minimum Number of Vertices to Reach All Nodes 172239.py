# Problem: Minimum Number of Vertices to Reach All Nodes - https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        noIncomingEdgeNode = [False] * n 
        result = []
        for (srcNode, dstNode) in edges: 
            noIncomingEdgeNode[dstNode] = True
        for i, node in enumerate(noIncomingEdgeNode): 
            if not node: 
                result.append(i)
        
        return result 