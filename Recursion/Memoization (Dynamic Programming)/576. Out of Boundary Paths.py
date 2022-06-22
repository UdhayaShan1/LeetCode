class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        M = 1000000007
        import sys
        dp = {}
        
        def dfs(i,j,moves):
            if i < 0 or i >= m or j < 0 or j >= n:
                if moves <= maxMove:
                    return 1
                else:
                    return 0
            if moves > maxMove:
                return 0
            if (i,j,moves) in dp:
                return dp[(i,j,moves)]

            y1 = dfs(i-1,j,moves+1)%M
            y2 = dfs(i+1,j,moves+1)%M
            y3 = dfs(i,j+1,moves+1)%M
            y4 = dfs(i,j-1,moves+1)%M
            dp[(i,j,moves)] = (y1+y2+y3+y4)%M
            return dp[(i,j,moves)]

        return(dfs(startRow,startColumn,0))
