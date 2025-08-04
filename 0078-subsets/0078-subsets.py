class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res =[]
        subset = []
        n = len(nums)
        def recursion(i):
            if(i == n ):
                res.append(subset[:])
                return 
            subset.append(nums[i])
            recursion(i + 1);
            subset.pop()
            recursion(i + 1);
        recursion(0)
        return res

        