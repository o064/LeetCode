class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # start from 1 
        # while j == i remove nums[j]
        # return nums.length
        i = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums) and nums[i] == nums[j]:
                nums.pop(i)
            i = j
        return len(nums)