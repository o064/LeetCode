class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] *n  
        prices[src] = 0 

        for _ in range(k+1):
            tempPrices = prices[:]
            for s ,d ,  p in flights : 
                if prices[s] == float("inf"):
                    continue
                if tempPrices[d] > prices[s] + p :
                    tempPrices[d] = prices[s]+p
            prices = tempPrices
        return -1 if prices[dst] == float("inf") else prices[dst]