class Solution:
    def cost(self, u,v):
        x1,y1= u
        x2,y2 = v
        x = abs(x1-x2)
        y = abs(y1-y2)
        return x + y 
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # disjoint initialization
        v = len(points)
        par = list(range(v))
        rank = [0] * v
        def find_set(i):
            if par[i] != i :
                par[i] = find_set(par[i])
            return par[i]
        def union(u, v):
            s1 = find_set(u)
            s2 = find_set(v)
            if s1 == s2:
                return False  # already in same set
            if rank[s1] < rank[s2]:
                par[s1] = s2
            elif rank[s2] < rank[s1]:
                par[s2] = s1
            else:
                rank[s1] += 1
                par[s2] = s1
            return True
        
             
            
        #  connect edges 
        connectedPoints  = []
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                connectedPoints.append([i ,j, self.cost(points[i] , points[j])])
        #  sort in non decreasing order
        connectedPoints.sort(key=lambda x: x[2])
        # form mst
        cost =0
        for u, v , w in connectedPoints:
            if union(u,v):
                cost += w
        return cost
        