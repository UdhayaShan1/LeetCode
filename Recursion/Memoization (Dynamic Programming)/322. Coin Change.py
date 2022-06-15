#is also a DP problem, solution under DP tab
class Solution:
    def coinChange(self, coins: List[int], amount1: int) -> int:
        import sys
        dp = {}
        def dfs(k,amount):
            if amount == amount1 :
                return 0
            if k >= len(coins) or amount > amount1:
                return sys.maxsize
            if (k,amount) in dp:
                return dp[(k,amount)]
            include = dfs(k,amount+coins[k])+1
            exclude = dfs(k+1,amount)
            dp[(k,amount)] = min(include,exclude)
            return dp[(k,amount)]

        x = (dfs(0,0))
        if x == 9223372036854775807:
            return -1
        else:
            return x
