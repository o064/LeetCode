class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        freq = {}
        for ch in tasks:
            freq[ch] = freq.get(ch, 0) + 1
        maxheap=[-1 * value for  value in freq.values()]
        heapq.heapify(maxheap)
        time = 0 
        while maxheap:
            temp = [] 
            for _ in range(n + 1):
                if maxheap : 
                    count = heapq.heappop(maxheap)
                    if count + 1 != 0 : 
                        temp.append(count+1)
                    time +=1
                else:
                    if not temp:
                        break
                    time +=1  
            for item in temp :
                heapq.heappush(maxheap,item)
        return time
