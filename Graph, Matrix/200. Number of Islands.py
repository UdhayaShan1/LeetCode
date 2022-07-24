class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dp2 = {}
        @functools.lru_cache(None)
        def dfs(i,j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                return
            if grid[i][j] == "0":
                return 
            if (i,j) in dp2:
                return
            grid[i][j] = count
            dp2[(i,j)] = 1
            y1 = dfs(i+1,j)
            y2 = dfs(i-1,j)
            y3 = dfs(i,j-1)
            y4 = dfs(i,j+1)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count+=1
                    dfs(i,j)
        return(count)
