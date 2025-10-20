class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        myMap = defaultdict(int)
        for num in nums :
            myMap[num] += 1
        for  key , value in myMap.items():
            if value > n/2 :
                return key 
        return -1 