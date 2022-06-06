class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        def recurse(index,able_to_buy):
            if index >= len(prices)-1:
                return 0
            if (index,able_to_buy) in dp:
                return dp[(index,able_to_buy)]

            if able_to_buy == True:
                y1 = recurse(index+1,False)-prices[index+1]
                y2 = recurse(index+1,True)
                dp[(index,able_to_buy)] = max(y1,y2)
            else:
                y1 = recurse(index+2,True)+prices[index+1]
                y2 = recurse(index+1,False)
                dp[(index,able_to_buy)] = max(y1,y2)
            return dp[(index,able_to_buy)]

        return(recurse(-1,True))
