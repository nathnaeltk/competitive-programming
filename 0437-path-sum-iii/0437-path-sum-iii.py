# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node,currentSum):
            if not node:
                return 0
            currentSum += node.val
            pathCount = prefixSum[currentSum - targetSum]
            prefixSum[currentSum] += 1

            pathCount += dfs(node.left,currentSum)
            pathCount += dfs(node.right,currentSum)

            prefixSum[currentSum] -= 1

            return pathCount

        prefixSum = defaultdict(int)
        prefixSum[0] = 1
        return dfs(root,0)