# Problem: Gas Station - https://leetcode.com/problems/gas-station/

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        gas_cost = []
        for i in range(len(cost)):
            gas_cost.append(gas[i]-cost[i])
        
        answer_index = 0
        total = 0

        for i in range(len(gas)):
            total += gas_cost[i]

            if total < 0:
                total = 0
                answer_index = i + 1

        return answer_index 
    
# 1, -2, 1
# 
