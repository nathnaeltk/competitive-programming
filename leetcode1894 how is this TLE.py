class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        i = 0
        while(k>=0):
            k - chalk[i%len(chalk)]
            i+=1

        return i%len(chalk)