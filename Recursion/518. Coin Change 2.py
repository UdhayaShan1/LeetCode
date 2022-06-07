# also DP problem
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        def dfs(k,amount):
            if amount == 0:
                return 1
            if amount < 0 or k >= len(coins):
                return 0
            key = (k,amount)
            if key in dp:
                return dp[key]

            include = dfs(k,amount-coins[k])
            exclude = dfs(k+1,amount)
            dp[key] = include+exclude
            return dp[key]

        return dfs(0,amount)
        

        
