class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def dfs(no_of_trans,holding,k):
            if k >= len(prices):
                return 0
            if no_of_trans > 2:
                return False
            if (no_of_trans,holding,k) in dp:
                return dp[(no_of_trans,holding,k)]
            if holding == False:
                y1 = dfs(no_of_trans+1,True,k+1)-prices[k]
                y2 = dfs(no_of_trans,False,k+1)
                dp[(no_of_trans,holding,k)] = max(y1,y2)
            else:
                y1 = dfs(no_of_trans,False,k+1)+prices[k]
                y2 = dfs(no_of_trans,True,k+1)
                dp[(no_of_trans,holding,k)] = max(y1,y2)

            return dp[(no_of_trans,holding,k)]

        return(dfs(0,0,0))
