class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        leftPq = []
        rightPq = []
        totalCost = 0
        iter = 0
        left = 0
        right = len(costs)-1
        while(iter<k):
            while(len(leftPq) < candidates and left<=right):
                heapq.heappush(leftPq, costs[left])
                left+=1
            while(len(rightPq) < candidates and right>=left):
                heapq.heappush(rightPq, -costs[right])
                right-=1
            ele1 = leftPq[0] if len(leftPq) > 0 else float('inf')
            ele2 = -rightPq[0] if len(rightPq) > 0 else float('inf')
            if(ele1 <= ele2):
                totalCost += ele1
                heapq.heappop(leftPq)
            else:
                totalCost += ele2
                heapq.heappop(rightPq)
            iter+=1 
        return totalCost