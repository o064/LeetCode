class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        def powHalf(x,n):
            if(n == 0):return 1;
            mult = powHalf(x * x ,(n//2))
            return mult * x if n % 2 else mult
        res = powHalf(x,abs(n))
        return res if n >0  else 1/res