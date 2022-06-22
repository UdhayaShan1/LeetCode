class Solution:
    def minSteps(self, n: int) -> int:
        import sys
        dp = {}
        def dfs(length,just_copied,copy):
            if length == n:
                return 0
            if length > n:
                return sys.maxsize

            if (length,just_copied,copy) in dp:
                return dp[(length,just_copied,copy)]



            if length == 1 and just_copied == False:
                y1 = dfs(length,True,length)+1
                dp[(length,just_copied,copy)] = y1
            else:
                if just_copied == True:
                    y1 = dfs(length+copy,False,copy)+1
                    dp[(length,just_copied,copy)] = y1
                else:
                    y1 = dfs(length+copy,False,copy)+1
                    y2 = dfs(length,True,length)+1
                    dp[(length,just_copied,copy)] = min(y1,y2)

            return dp[(length,just_copied,copy)]

        return(dfs(1,False,0))
