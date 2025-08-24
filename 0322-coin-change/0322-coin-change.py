class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0 :return 0
        res = [-1] * (amount+1)
        res[0] = 0 
        for i in range(1,len(res)):
            q = sys.maxsize
            for coin in coins :
                if i - coin >= 0 :
                    q = min(q, 1+ res[i - coin])
            res[i] = q
        return -1 if res[-1] == sys.maxsize else res[-1]

        