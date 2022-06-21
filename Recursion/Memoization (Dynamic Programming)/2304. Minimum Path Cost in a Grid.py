class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        import sys
        dp = {}
        def dfs(i,j):
            if i == len(grid)-1:
                return grid[i][j]
            if i >= len(grid):
                return sys.maxsize

            if (i,j) in dp:
                return dp[(i,j)]


            y1 = sys.maxsize
            for k in range(len(moveCost[grid[i][j]])):
                x = dfs(i+1,k)+moveCost[grid[i][j]][k]+grid[i][j]
                if x < y1:
                    y1 = x
            dp[(i,j)] = y1
            return y1
        
        x2 = sys.maxsize
        for k in range(len(grid[0])):
            y2 = dfs(0,k)
            if y2 < x2:
                x2 = y2
        return x2
