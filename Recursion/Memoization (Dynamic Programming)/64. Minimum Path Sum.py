class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        import sys
        dp = {}
        def dfs(i,j):
            if i >= len(grid) or j >= len(grid[0]):
                return sys.maxsize
            if i == len(grid)-1 and j == len(grid[0])-1:
                return grid[i][j]

            if (i,j) in dp:
                return dp[(i,j)]

            y1 = dfs(i+1,j)+grid[i][j]
            y2 = dfs(i,j+1)+grid[i][j]
            dp[(i,j)] = min(y1,y2)
            return dp[(i,j)]

        return(dfs(0,0))
