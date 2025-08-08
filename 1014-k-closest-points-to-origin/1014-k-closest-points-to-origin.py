class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        heap =  [(point[0] ** 2 + point[1] **2  , point) for point in points]
        heapq.heapify(heap)
        res=[]
        for i in range(k): 
            res.append(heapq.heappop(heap)[1])
        return res

        