class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        import sys
        dp = {}
        dp2 = {}
        def dfs(i,j,moves):
            if moves > k:
                return 0
            if i < 0 or i >= n or j < 0 or j >= n:
                return 0
            if moves == k:
                return 1

            if (i,j,moves) in dp:
                return dp[(i,j,moves)]


            y1 = 0
            if (i-2,j-1) not in dp2:

                y1 += dfs(i-2,j-1,moves+1)

            if (i-2,j+1) not in dp2:

                y1 += dfs(i-2,j+1,moves+1)

            if (i-1,j-2) not in dp2:

                y1 += dfs(i-1,j-2,moves+1)

            if (i-1,j+2) not in dp2:

                y1 += dfs(i-1,j+2,moves+1)

            if (i+1,j-2) not in dp2:

                y1 += dfs(i+1,j-2,moves+1)

            if (i+1,j+2) not in dp2:

                y1 += dfs(i+1,j+2,moves+1)

            if (i+2,j+1) not in dp2:

                y1 += dfs(i+2,j+1,moves+1)

            if (i+2,j-1) not in dp2:

                y1 += dfs(i+2,j-1,moves+1)

            dp[(i,j,moves)] = y1

            return dp[(i,j,moves)]

        return(dfs(row,column,0)/(8**k))
        
        
        
        
