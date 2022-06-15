class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        dp = {}
        def dfs(k1,k2):
            if k1 >= len(s) or k2 >= len(t):
                return 0
            if (k1,k2) in dp:
                return dp[(k1,k2)]
            
            if s[k1] == t[k2]:
                y1 = dfs(k1+1,k2+1)+1
                dp[(k1,k2)] = y1
            else:
                y1 = dfs(k1+1,k2)
                y2 = dfs(k1,k2+1)
                dp[(k1,k2)] = max(y1,y2)
            return dp[(k1,k2)]
            
        return dfs(0,0) == len(s)
