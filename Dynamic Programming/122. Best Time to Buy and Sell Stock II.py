class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min1 = prices[0]
        count = 0
        for i in range(1,len(prices)):
            if prices[i] < prices[i-1]:
                min1 = prices[i]
            else:
                count += (prices[i] - prices[i-1])
                min1 = prices[i]

        return(count)
