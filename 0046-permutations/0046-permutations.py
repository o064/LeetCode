class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        perm=[]
        sub=[]
        n= len(nums)
        def helper(nums , perm ):
            
            if(len(sub)==n):
                perm.append(sub[:])
                return;
            for i in range(len(nums)):
                num = nums.pop(i)
                sub.append(num)
                helper(nums, perm)
                nums.insert(i,num)
                sub.remove(num)
        helper(nums,perm)
        return perm
        



        