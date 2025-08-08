class MedianFinder(object):

    def __init__(self):
        self.minheap = []
        self.maxheap = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        # max heap for small elements 
        # min heap for  large element
        if len(self.maxheap) == 0  or num <= -1 * self.maxheap[0]:
            heapq.heappush(self.maxheap, -1 * num)
        else :
            heapq.heappush(self.minheap,num)
        
        if len(self.minheap) + 1 < len(self.maxheap) :
            heapq.heappush(self.minheap,-1 * heapq.heappop(self.maxheap))
        elif len(self.minheap)  > len(self.maxheap):
            heapq.heappush(self.maxheap,-1 * heapq.heappop(self.minheap))


        

    def findMedian(self):
        """
        :rtype: float
        """
        maxheapval = float(-1*self.maxheap[0])
        if len(self.maxheap) ==len(self.minheap) : 
            return (maxheapval +self.minheap[0])/2
        else :
            return maxheapval

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()