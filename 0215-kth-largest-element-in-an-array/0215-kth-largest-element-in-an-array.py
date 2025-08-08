class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = [-1 * x for x in nums ]
        heapq.heapify(heap)
        for i in range(k-1):
            heapq.heappop(heap)
        return -1 * heapq.heappop(heap) 
        