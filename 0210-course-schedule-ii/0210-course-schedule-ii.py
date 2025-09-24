class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        NOT_VISITED = 0 
        VISITING = 1
        VISITED =2 
        visited = [NOT_VISITED] * numCourses
        res =[]
        courses = prerequisites
        # adjancy list
        adj = defaultdict(list)
        for a,b in courses :
            adj[b].append(a)
        def dfs(node):
            if visited[node] == VISITING:
                return False
            if visited[node] == VISITED:
                return True
            visited[node] = VISITING
            for E in adj[node]:
                if not dfs(E):
                    return False
            visited[node] = VISITED
            res.insert(0,node)
            return True
        for v in range(numCourses):
            if not dfs(v):
                return []
        return res            
            

