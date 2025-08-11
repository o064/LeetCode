class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        n = len(matrix)  # rows
        m = len(matrix[0]) # columns
        col = -1 
        top ,bottom = 0 , n - 1 
        # seach for the row 
        while top <= bottom :
            mid = top + (bottom - top )//2      
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] >  target:
                bottom = mid-1
            else :
                if mid == n-1 or (mid+1 < n and matrix[mid+1][0] >  target):
                    col = mid
                    break
                else :
                    top = mid + 1
        # search for the column 
        low , high = 0,m-1
        while high >= low : 
            mid = low + (high-low)//2
            if matrix[col][mid] == target :
                return True
            elif matrix[col][mid] > target :
                high = mid - 1
            else:
                low = mid+ 1   
        return  False 

        
