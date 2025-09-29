class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        A_visited = [[False] * cols  for _ in range(rows)]
        P_visited = [[False] * cols  for _ in range(rows)]
        def dfs(i,j, visited,prev ):
            if i< 0 or j < 0 or i >= rows  or j >= cols or visited[i][j] or heights[i][j] < prev :
                return 
            visited[i][j] = True
            # dfs in all directions
            dfs(i+1,j,visited,heights[i][j])
            dfs(i-1,j,visited,heights[i][j])
            dfs(i,j + 1,visited,heights[i][j])
            dfs(i,j - 1,visited,heights[i][j])
        # Pacific border (top row + left col)
        for i in range(rows):
            dfs(i, 0, P_visited, -1)
        for j in range(cols):
            dfs(0, j, P_visited, -1)

        # Atlantic border (bottom row + right col)
        for i in range(rows):
            dfs(i, cols-1, A_visited, -1)
        for j in range(cols):
            dfs(rows-1, j, A_visited, -1)

        res =[]
        for row in range(rows):
            for col in range(cols):
                if P_visited[row][col] and A_visited[row][col]:
                    res.append([row,col])
        return res


            
