class Solution:
    def climbStairs(self, n: int) -> int:
        nums = [1,2]
        dp = {}
        def dfs(amount):
            if amount == n:
                return 1
            if amount > n:
                return 0
            if amount in dp:
                return dp[amount]
            y1 = 0
            for i in nums:
                y1 += dfs(amount+i)
            dp[amount] = y1
            return dp[amount]

        return(dfs(0))
