class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp = [amount+1] * (amount+1)
        dp[0] = 0 
        for i in range(1,amount+1):
            for j in coins:
                if i >= j:
                    remainder = i-j
                    dp[i] = min((dp[i]),1+dp[remainder])

        if dp[amount] == amount+1:
            return -1
        else:
            return dp[amount]
