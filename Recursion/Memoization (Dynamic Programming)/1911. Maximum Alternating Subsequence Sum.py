class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        dp = {}
        def dfs(k1,even):
            if k1 >= len(nums):
                return 0
            if (k1,even) in dp:
                return dp[(k1,even)]

            if even == True:
                y1 = dfs(k1+1,False)+nums[k1]
                y2 = dfs(k1+1,True)
                dp[(k1,even)] = max(y1,y2)
            else:
                y1 = dfs(k1+1,True)-nums[k1]
                y2 = dfs(k1+1,False)
                dp[(k1,even)] = max(y1,y2)

            return dp[(k1,even)]

        return(dfs(0,True))
