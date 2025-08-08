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
        q= deque()
        time = 0 
        while maxheap or q :
            time += 1
            if not maxheap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxheap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxheap, q.popleft()[0])
        return time
