class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = {}
        def dfs(k):
            if k >= len(cost):
                return 0
            if k in dp:
                return dp[k]
            include1 = dfs(k+1)+cost[k]
            include2 = dfs(k+2)+cost[k]
            dp[k] = min(include1,include2)
            return dp[k]

        return(min(dfs(0),dfs(1)))
