class Solution:
    def maxProfit(self, k1: int, prices: List[int]) -> int:
        import sys

        dp = {}

        def dfs(count,k,holding):
            if k == len(prices):
                if count <= k1:
                    return 0
                else:
                    return -sys.maxsize
            if k > len(prices) or count > k1:
                return -sys.maxsize
            if (count,k,holding) in dp:
                return dp[(count,k,holding)]

            if holding == False:
                y1 = dfs(count+1,k+1,True) - prices[k]
                y2 = dfs(count,k+1,False)
                dp[(count,k,holding)] = max(y1,y2)
            else:
                y1 = dfs(count,k+1,False) + prices[k]
                y2 = dfs(count,k+1,True)
                dp[(count,k,holding)] = max(y1,y2)
            return dp[(count,k,holding)]


        return(dfs(0,0,False))
