# Problem: Combination Sum - https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        from collections import deque
        candidates.sort()
        ans = []
        def backtrack(remaining, ans, ptr, collection=[]):
            if not remaining: 
                ans.append(collection[:])
                return
            for i in range(ptr, len(candidates)):
                c = candidates[i]
                if c <= remaining: 
                    collection += [c]
                    backtrack(remaining-c, ans, i, collection)
                    collection.pop()
            return
        backtrack(target, ans, 0, [])
        return ans