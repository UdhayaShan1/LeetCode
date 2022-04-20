class Solution:
    def maxSubArray(self, list1: List[int]) -> int:
        max1 = -100000000
        dp = {}
        dp[0] = list1[0]
        if dp[0] > max1:
            max1 = dp[0]
        for i in range(1,len(list1)):
            dp[i] = list1[i]
            dp[i] += max(0,dp[i-1])
            if dp[i] > max1:
                max1 = dp[i]

        return(max1)
