class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        """
        :type n: int
        :rtype: int
        """
        result = 0
        j=1
        while True:
            if (j%2 == 0 and j%n == 0):
                result = j
                break
            j+=1
        return result
