class Solution:
    def numTrees(self, n: int) -> int:
        res = [0] * (n+1)
        res[0] = 1
        res[1] = 1
        def calNum(n) : 
            if res[n] != 0 :
                return res[n]
            total = 0
            for i in range(1,n+1):
                left = calNum(i-1)
                right =calNum(n-i)
                total += left * right
            res[n] =total
            return  total

        return calNum(n)