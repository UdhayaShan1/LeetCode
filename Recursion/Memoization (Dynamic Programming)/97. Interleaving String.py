class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        global x
        if len(s1)+len(s2)!=len(s3):
            return False
        x = 0
        dp = {}
        dp[(len(s1),len(s2))] = True
        def dfs(i,j):
            global x
            if i > len(s1) or j > len(s2):
                return False
            if (i,j) == (len(s1),len(s2)):
                x = 1
                return True
            if (i,j) in dp:
                return dp[(i,j)]

            if i >= len(s1):
                if s3[i+j] != s2[j]:
                    dp[(i,j)] = False
                else:
                    y = dfs(i,j+1)
                    dp[(i,j+1)] = y
            elif j >= len(s2):
                if s3[i+j] != s1[i]:
                    dp[(i,j)] = False
                else:
                    y = dfs(i+1,j)
                    dp[(i,j+1)] = y        

            elif s3[i+j] == s1[i] and s3[i+j] != s2[j]:
                dp[i,j+1] = False
                y = dfs(i+1,j)
                dp[(i+1,j)] = y
            elif s3[i+j] != s1[i] and s3[i+j] == s2[j]:
                dp[i+1,j] = False
                y = dfs(i,j+1)
                dp[(i,j+1)] = y
            elif s3[i+j] == s1[i] and s3[i+j] == s2[j]:
                y = dfs(i+1,j)
                y1 = dfs(i,j+1)
                dp[(i+1,j)] = y
                dp[(i,j+1)] = y1
            else:
                dp[(i,j)] = False

        dfs(0,0)
        return(x==1)
