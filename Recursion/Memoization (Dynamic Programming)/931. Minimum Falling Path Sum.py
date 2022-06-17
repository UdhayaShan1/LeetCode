class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        import sys
        n = len(matrix)
        dp = {}
        def dfs(i,j):
            if i < 0 or i >= n:
                return 0
            if j < 0 or j >= n:
                if i >= n:
                    return 0
                else:
                    return sys.maxsize

            if (i,j) in dp:
                return dp[(i,j)]

            y1 = dfs(i+1,j)+matrix[i][j]
            y2 = dfs(i+1,j-1)+matrix[i][j]
            y3 = dfs(i+1,j+1)+matrix[i][j]
            dp[(i,j)] = min(y1,y2,y3)
            return dp[(i,j)]


        min1 = sys.maxsize
        for j in range(n):
            x = dfs(0,j)
            if x < min1:
                min1 = x
        return(min1)
