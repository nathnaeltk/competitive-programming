class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        result = [0] * n
        
        total_balls, total_ops = 0, 0
        for i in range(n):
            result[i] += total_ops
            total_balls += int(boxes[i])
            total_ops += total_balls
        
        total_balls, total_ops = 0, 0
        for i in range(n - 1, -1, -1):
            result[i] += total_ops
            total_balls += int(boxes[i])
            total_ops += total_balls
        
        return result