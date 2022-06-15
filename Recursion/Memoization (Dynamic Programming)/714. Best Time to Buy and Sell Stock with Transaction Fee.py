class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp = {}
        def dfs(k,holding):
            if k >= len(prices):
                return 0
            if (k,holding) in dp:
                return dp[(k,holding)]
            if holding == False:
                y1 = dfs(k+1,True) - prices[k]
                y2 = dfs(k+1,False)
                dp[(k,holding)] = max(y1,y2)
            else:
                y1 = dfs(k+1,False) + prices[k] - fee
                y2 = dfs(k+1,True)
                dp[(k,holding)] = max(y1,y2)
            return dp[(k,holding)]

        return(dfs(0,False))
