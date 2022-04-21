class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max1 = nums[0]
        dp = {}
        dp1 = {}
        dp[0] = nums[0]
        dp1[0] = nums[0]
        for i in range(1,len(nums)):
            dp[i] = max(nums[i],nums[i]*dp[i-1],nums[i]*dp1[i-1],nums[i]*nums[i-1])
            dp1[i] = min(nums[i],nums[i]*dp[i-1],nums[i]*dp1[i-1],nums[i]*nums[i-1])
            if dp[i] > max1:
                max1 = dp[i]
            if dp1[i] > max1:
                max1 = dp1[i]



        return(max1)
