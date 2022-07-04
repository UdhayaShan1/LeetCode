class Solution:
    def uniquePathsIII(self, obstacleGrid: List[List[int]]) -> int:
        can_walk = 0
        for i in range(len(obstacleGrid)):
            for k in obstacleGrid[i]:
                if k == -1:
                    continue
                can_walk+=1

        import sys
        dp = {}
        dp2 = {}
        def dfs(i,j):
            if i < 0 or j < 0 or i >= len(obstacleGrid) or j >= len(obstacleGrid[0]):
                return 0
            if obstacleGrid[i][j] == 2:
                if len(dp2.keys()) == can_walk-1:
                    return 1
                else:
                    return 0
            if obstacleGrid[i][j] == -1:
                return 0
            if (i,j) in dp2:
                return 0


            dp2[(i,j)] = 1
            y1 = dfs(i+1,j)
            y2 = dfs(i,j+1)
            y3 = dfs(i,j-1)
            y4 = dfs(i-1,j)
            del dp2[(i,j)]
            dp[(i,j)] = y1+y2+y3+y4
            return dp[(i,j)]

        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    return dfs(i,j)
