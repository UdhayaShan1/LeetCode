class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}
        dp[len(s)] = True
        for i in range(len(s)-1,-1,-1):
            flag = 0
            dp[i] = False
            for j in wordDict:
                length = len(j)
                if s[i:i+length] == j and len(s[i:i+length]) == length:
                    if dp[i+length] == True:
                        dp[i] = True
                        flag+=1
                        break
        return(dp[0])
