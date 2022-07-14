class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        import sys
        dp = {}
        def dfs(i,j):
            if j >= len(word2):
                return len(word1)-(i)
            if i >= len(word1):
                return len(word2)-(j)
            if (i,j) in dp:
                return dp[(i,j)]


            if word1[i] == word2[j]:
                y1 = dfs(i+1,j+1)
                dp[(i,j)] = y1
            else:
                y1 = dfs(i,j+1)+1
                y2 = dfs(i+1,j)+1
                y3 = dfs(i+1,j+1)+1
                dp[(i,j)] = min(y1,y2,y3)
            return dp[(i,j)]

        return(dfs(0,0))
