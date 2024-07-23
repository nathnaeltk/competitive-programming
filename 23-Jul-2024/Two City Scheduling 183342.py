# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costAdv = []
        for costA, costB in costs:
            costAdv.append([costB - costA, costA, costB])

        costAdv.sort()
        minCost = 0
        for i in range(len(costAdv)):
            if i < len(costAdv)//2:
                minCost += costAdv[i][2]
            else:
                minCost += costAdv[i][1]
        
        return minCost