# Problem: All Nodes Distance K in Binary Tree - https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        g = defaultdict(list)
        q = deque( [root] )
        
        while q:
            cur = q.popleft()
            
            if cur.left:
                q.append(cur.left)
                g[cur.val].append(cur.left.val)
                g[cur.left.val].append(cur.val)
            if cur.right:
                q.append(cur.right)
                g[cur.val].append(cur.right.val)
                g[cur.right.val].append(cur.val)
        
        q = deque( [target.val] )
        seen = set( [target.val] )
        
        while k and q:
            k -= 1
            for _ in range(len(q)):
                cur = q.popleft()
                
                for nei in g[cur]:
                    if nei not in seen:
                        q.append(nei)
                        seen.add(nei)

        return list(q)