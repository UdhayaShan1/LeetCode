class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = {}
        def dfs(i,j):

            if i == m-1 and j == n-1:
                if obstacleGrid[i][j] == 1:
                    return 0
                else:
                    return 1
            if i >= m or i < 0 or j >= n or j < 0:
                return 0
            if obstacleGrid[i][j] == 1:
                return 0
            if (i,j) in dp:
                return dp[(i,j)]

            y1 = dfs(i+1,j)
            y2 = dfs(i,j+1)
            dp[(i,j)] = y1+y2
            return dp[(i,j)]

        return(dfs(0,0))
