class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = {}
        def dfs(k1,k2,length):
            if length > len(t):
                return 0
            if k2 >= len(t):
                return 1
            if k1 >= len(s):
                return 0

            if (k1,k2,length) in dp:
                return dp[(k1,k2,length)]


            if s[k1] == t[k2]:
                y1 = dfs(k1+1,k2+1,length+1)
                y2 = dfs(k1+1,k2,length)
                dp[(k1,k2,length)] = y1+y2
            else:
                y1 = dfs(k1+1,k2,length)
                dp[(k1,k2,length)] = y1

            return dp[(k1,k2,length)]

        return(dfs(0,0,0))
