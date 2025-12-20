class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        lastValid = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == val : 
                nums[i],nums[lastValid] =nums[lastValid], nums[i]
                k += 1 
                lastValid -= 1
        return lastValid + 1 