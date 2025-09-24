class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 0 -> not visited  , 1-> process  2-> visited
        visited= [0] *  numCourses
        adj =  [[0] * numCourses for _ in range(numCourses)]
        for a ,b in prerequisites :
            adj[a][b] = 1

        def dfs(v):
            if visited[v] == 1:
                return False
            if visited[v] == 2:
                return True
            visited[v] = 1 
            for i in range(numCourses):
                if adj[v][i] == 1 :
                    if not dfs(i):
                        return False
            visited[v] = 2 
            return True
                
        for v in range(numCourses):
            if visited[v] == 0 :
                if not dfs(v):
                    return False
        return True 