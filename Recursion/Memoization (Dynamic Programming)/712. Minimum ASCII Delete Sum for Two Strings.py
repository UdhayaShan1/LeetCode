class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        import sys
        dp = {}
        def dfs(i,j):
            if i >= len(s1) and j >= len(s2):
                return 0
            if i >= len(s1):
                count = 0
                for k in s2[j:]:
                    count += ord(k)
                return count
            if j >= len(s2):
                count = 0
                for k in s1[i:]:
                    count += ord(k)
                return count
            if (i,j) in dp:
                return dp[(i,j)]

            if s1[i] == s2[j]:
                y1 = dfs(i+1,j+1)
                dp[(i,j)] = y1
            else:
                y1 = dfs(i+1,j)+ord(s1[i])
                y2 = dfs(i,j+1)+ord(s2[j])
                dp[(i,j)] = min(y1,y2)
            return (dp[(i,j)])

        return(dfs(0,0))
