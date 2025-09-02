class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        i = 0 
        while i < len(triplets):
            for j in range(3):
                if triplets[i][j] >  target[j]:
                    triplets.pop(i)
                    i -= 1
                    break
            i += 1  
            if len(triplets) == 0:
                return False
        for j in range(3):
            isFound = False
            for i in range(len(triplets)) : 
                if triplets[i][j] == target[j]:
                   isFound= True
                   break 
            if not isFound : return False

        return True


        