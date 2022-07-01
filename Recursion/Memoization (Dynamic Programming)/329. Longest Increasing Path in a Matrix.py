class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        import sys
        dp = {}
        dp2 = {}
        def dfs(i,j,prev):
            if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]):
                return 0
            if (i,j) in dp2:
                return 0
            if matrix[i][j] <= prev:
                return 0

            if (i,j,prev) in dp:
                return dp[(i,j,prev)]

            if prev == -1:
                dp2[(i,j)] = 1
                y1 = dfs(i-1,j,matrix[i][j])+1
                y2 = dfs(i+1,j,matrix[i][j])+1
                y3 = dfs(i,j-1,matrix[i][j])+1
                y4 = dfs(i,j+1,matrix[i][j])+1
                del dp2[(i,j)]
                dp[(i,j,prev)] = max(y1,y2,y3,y4)
            else:
                if matrix[i][j] > prev:
                    dp2[(i,j)] = 1
                    y1 = dfs(i-1,j,matrix[i][j])+1
                    y2 = dfs(i+1,j,matrix[i][j])+1
                    y3 = dfs(i,j-1,matrix[i][j])+1
                    y4 = dfs(i,j+1,matrix[i][j])+1
                    del dp2[(i,j)]
                    dp[(i,j,prev)] = max(y1,y2,y3,y4)

            return dp[(i,j,prev)]


        max1 = -sys.maxsize

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                x = dfs(i,j,-1)
                if x > max1:
                    max1 = x
        return(max1)
