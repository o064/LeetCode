class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        delay = [float("inf")] * (n) 
        delay[k-1] = 0 
        def relax(u,v,w):
            if delay[v-1] > delay[u-1] + w :
                delay[v-1] = delay[u-1] + w
        for i in range(n-1):
            for u,v,w in times:
                relax(u,v,w)
        minTime =max(delay)
        return minTime if  minTime != float("inf") else -1

                