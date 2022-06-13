class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = {}
        def dfs(str1):
            if len(str1) == 1:
                return 1
            if len(str1) == 0:
                return 0 
            if str1 in dp:
                return dp[str1]

            if str1[0] == str1[-1]:
                y1 = dfs(str1[1:-1])+2
                dp[str1] = y1
            else:
                y1 = dfs(str1[1:])
                y2 = dfs(str1[:-1])
                dp[str1] = max(y1,y2)
            return dp[str1]

        return(dfs(s))
        
    
    
