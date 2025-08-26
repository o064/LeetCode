class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n= len(nums)
        dp = [-1] * n 
        def rec(idx):
            # reutrn the lis if computed
            if dp[idx] != -1:
                return dp[idx]
            # compute
            ans = 1
            for j in range(idx + 1, n):
                if nums[j] > nums[idx]:
                    ans = max(ans, 1 + rec(j))
            # store solution
            dp[idx] =ans
            return dp[idx] 
        # compute LIS for specific element 
        for i  in range(n):
            rec(i)
        return max(dp) 