class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges) + 1))
        rank = [1] * (len(edges) + 1)
        def find(i) :
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]
        def union(x,y):
            s1,s2 = find(x),find(y)
            if s1 == s2 :
                return False
            if rank[s1] < rank[s2]:
                parent[s1] = s2 
            elif rank[s2] < rank[s1]:
                parent[s2] = s1 
            else:
                parent[s2] =s1
                rank[s1] += 1
            return True
        for u,v in edges :
            if not union(u,v):
                return [u,v]