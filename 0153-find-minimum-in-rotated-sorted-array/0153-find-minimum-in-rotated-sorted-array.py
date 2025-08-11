class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l , r = 0,len(nums)-1
        res = nums[0]
        while l <=r :
            if nums[l] < nums[r]:
                res = min(nums[l] , res)
                break
            m =  l + (r-l)//2
            res = min(res , nums[m])
            if nums[m] < nums[l] :
                r = m - 1
            else : 
                l = m + 1
        return res 
            