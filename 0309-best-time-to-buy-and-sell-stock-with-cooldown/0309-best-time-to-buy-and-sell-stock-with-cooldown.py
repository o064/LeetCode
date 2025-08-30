class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # cachinge
        dp = {}

        def dfs(i , buying) :
            if i >= len(prices):
                return 0 
            if (i,buying) in dp :
                return dp[(i,buying)]
            
            if buying:  # if i can buy
                buy = dfs(i+1, not buying) - prices[i] # i can choose to buy
                cooldown = dfs(i+1,  buying)  # i can choose to choose to cooldown
                dp[(i , buying)] = max(buy, cooldown)
            else :
                sell = dfs(i+2, not buying) + prices[i] # i can choose to buy
                cooldown = dfs(i+1,  buying)  # i can choose to choose to cooldown
                dp[(i , buying)] = max(sell, cooldown)
            return  dp[(i,buying)]

        return dfs(0,True)
