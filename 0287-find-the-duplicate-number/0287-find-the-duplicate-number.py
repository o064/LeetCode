class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mySet = set()
        for i in nums:
            if i in mySet :
                return i
            else:
                mySet.add(i)
        return -1
        