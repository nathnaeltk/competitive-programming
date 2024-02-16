class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        water = capacity
        steps = 0
        for i in range(len(plants)):
            if plants[i] > water:
                water = capacity
                steps += 2*(i)
                
            steps += 1
            water -= plants[i]
        return steps