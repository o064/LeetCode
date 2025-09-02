class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        rotated_Arr = [0] * n
        for i in range(n):
            rotated_Arr[(i+k)%n] = nums[i]
        nums[:] = rotated_Arr
        return 

        