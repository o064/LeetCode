class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        aSum = nums[0]
        for i  in range(1,n):
            aSum = max(nums[i] + aSum , nums[i]) 
            dp[i] = max(dp[i-1] ,aSum)
        return dp[-1]