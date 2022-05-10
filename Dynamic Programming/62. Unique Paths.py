class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1:
            return 1
        dp = {}
        for i in range(m):
            dp[i] = {}
            for j in range(n):
                if i == m-1:
                    dp[i][j] = 1
                    continue
                if j == n-1:
                    dp[i][j] = 1
                    continue
                dp[i][j] = 0


        dp[m-1][n-2] = 1
        dp[m-2][n-1] = 1

        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                dp[i][j] += dp[i+1][j] + dp[i][j+1]
        return(dp[0][0])
