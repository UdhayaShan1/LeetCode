class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {}
        def dfs(k1,k2,op):
            if k1 >= len(word1) or k2 >= len(word2):
                return (len(word1) - k1 + len(word2) - k2 + op)

            if (k1,k2,op) in dp:
                return dp[(k1,k2,op)]

            if word1[k1] != word2[k2]:
                y1 = dfs(k1+1,k2,op+1)
                y2 = dfs(k1,k2+1,op+1)
                dp[(k1,k2,op)] = min(y1,y2)
            else:
                dp[(k1,k2,op)] = dfs(k1+1,k2+1,op)

            return dp[(k1,k2,op)]

        return(dfs(0,0,0))
