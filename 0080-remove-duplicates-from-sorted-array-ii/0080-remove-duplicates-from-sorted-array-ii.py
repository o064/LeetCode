class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k =  1
        counts = defaultdict(int)
        counts[nums[0]] += 1 
        for j in range(1 , len(nums)):
            if  counts[nums[j]] < 2 : 
                nums[k] =nums[j]
                k += 1
                counts[nums[j]] += 1
        return k
        