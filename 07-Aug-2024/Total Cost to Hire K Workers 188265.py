# Problem: Total Cost to Hire K Workers - https://leetcode.com/problems/total-cost-to-hire-k-workers/description/

import heapq
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:



        h1 = []
        h2 = []

        n = len(costs)
        for i in range(candidates):
            heapq.heappush(h1, costs[i])

        for i in range(n-1, max(candidates-1, n-candidates-1), -1):
            heapq.heappush(h2, costs[i])
        res = 0

        startP = candidates
        endP = n-candidates-1

        while k  > 0:

            if len(h1) > 0 and len(h2) > 0:
                t1 = h1[0]
                t2 = h2[0]

                if t1 <= t2:
                    res += t1
                    heapq.heappop(h1)
                    if startP <= endP:
                        
                        heapq.heappush(h1, costs[startP])
                        startP += 1
                else:
                    res += t2
                    heapq.heappop(h2)
                    if endP >= startP:
                        heapq.heappush(h2, costs[endP])
                        endP -= 1
            elif len(h2) == 0:
                res += h1[0]
                heapq.heappop(h1)
            elif len(h1) == 0:
                res += h2[0]
                heapq.heappop(h2)

            k -= 1
     

        return res