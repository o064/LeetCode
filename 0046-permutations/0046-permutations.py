class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        perm=[]
        sub=[]
        n= len(nums)
        def helper(nums):
            if not nums:
                perm.append(sub[:])
                return;
            for i in range(len(nums)):
                num = nums[i]
                sub.append(num)
                helper(nums[:i]+nums[i+1:])
                sub.pop()
        helper(nums)
        return perm
        



        