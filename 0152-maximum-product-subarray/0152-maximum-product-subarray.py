class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = cur_max =  cur_min = nums[0]
        for num in nums[1:]:
            temp_max , temp_min = cur_max ,cur_min
            cur_max = max(num , temp_max * num , temp_min * num)
            cur_min = min(num , temp_max * num , temp_min * num)
            ans = max(ans , cur_max)
        return ans
