# Problem: Coin Change II - https://leetcode.com/problems/coin-change-ii/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        dp = [[0 for i in range(amount+1)] for j in range(n+1)]

        for i in range(amount+1):
            if i % coins[0] == 0:
                dp[0][i] = 1

        for ind in range( 1 , n ):
            for cur_amount in range( amount+1 ):
    
                not_take = dp[ind-1][cur_amount]

                take = 0
                if cur_amount >= coins[ind]:
                    take = dp[ind][cur_amount - coins[ind]]
                
                dp[ind][cur_amount] = take + not_take
        
        return dp[n-1][amount]