class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cols = amount + 1
        rows =len(coins) + 1
        dp = [[0] * cols for _ in range(rows)]
        for i in range(rows):
            dp[i][0] = 1
        for row in range(1, rows):
            for col in range(1,cols):
                dp[row][col]  += dp[row-1][col]
                if col - coins[row-1] >= 0 :
                    dp[row][col]  += dp[row][col - coins[row-1]]
        return dp[-1][-1]
        
            