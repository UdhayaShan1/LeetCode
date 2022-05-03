class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {}
        dp_single = {}
        if s[0] == "0":
            dp[0] = 0
            dp_single[0] = 0
        else:
            dp[0] = 1
            dp_single[0] = 1

        for i in range(1,len(s)):
            if dp[i-1] == 0:
                dp[i] = 0
                continue
            if s[i] == "0" and s[i-1] == "0":
                dp[i] = 0 
                continue
            if s[i] == "0":
                if int(s[i-1]) >= 3:
                    dp[i] = 0
                    continue
                else:
                    dp[i] = dp_single[i-1]
                    dp_single[i] = dp[i-1]
                continue
            if s[i-1] == "0":
                dp[i] = dp[i-1]
                dp_single[i] = dp[i-1]
                continue
            if int(s[i-1]+s[i]) <= 26:
                dp[i] = dp_single[i-1]+dp[i-1]
                dp_single[i] = dp[i-1]
            else:
                dp[i] = dp[i-1]
                dp_single[i] = dp[i-1]

        return(dp[len(s)-1])
      
