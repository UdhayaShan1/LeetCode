class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = {}
        for i in range(len(text1)+1):
            dp[i] = {}
            for j in range(len(text2)+1):
                dp[i][j] = 0

        max1 = 0

        for i in range(len(text1)-1,-1,-1):
            for j in range(len(text2)-1,-1,-1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                    if dp[i][j] > max1:
                        max1 = dp[i][j]
                else:
                    dp[i][j] = max(dp[i+1][j],dp[i][j+1])
                    if dp[i][j] > max1:
                        max1 = dp[i][j]
        return(max1)
