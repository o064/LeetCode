class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones= [x * -1 for x in stones]
        heapq.heapify(stones)
        while len(stones) >= 2 : 
            y = -1 * heapq.heappop(stones)
            x = -1 * heapq.heappop(stones)
            y = y-x 
            if y : 
                heapq.heappush(stones,-1 * y)
        return -1 * stones[0] if len(stones) else 0 
        