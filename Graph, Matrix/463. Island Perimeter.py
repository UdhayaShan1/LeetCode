class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        dp2 = {}

        def dfs(i,j):
            print(dp2)
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                return 1
            if grid[i][j] == 0:
                return 1
            if (i,j) in dp2:
                return 0
            dp2[(i,j)] = 1
            y1 = dfs(i+1,j)
            y2 = dfs(i-1,j)
            y3 = dfs(i,j+1)
            y4 = dfs(i,j-1)
            del dp2[(i,j)]
            return y1+y2+y3+y4
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(i,j)
