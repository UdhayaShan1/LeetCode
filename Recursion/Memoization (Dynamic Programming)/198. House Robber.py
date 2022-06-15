class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        def dfs(k):
            if k >= len(nums):
                return 0
            if k in dp:
                return dp[k]
            include = dfs(k+2)+nums[k]
            exclude = dfs(k+1)
            dp[k] = max(include,exclude)
            return dp[k]

        return(dfs(0))
