class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left, right = 0, len(people)-1
        total_boats = 0

        while left <= right:
            free_space = limit - people[right]
            right -= 1
            total_boats += 1
            if left <= right and free_space >= people[left]:
                left += 1
                
        return total_boats