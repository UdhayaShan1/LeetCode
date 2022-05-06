class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        if len(nums) == 1:
            return(nums[0])
        elif len(nums) == 2:
            return(max(nums))
        elif len(nums) == 3:
            return(max(nums[0]+nums[2],nums[1]))
        dp[0] = nums[0]
        dp[1] = nums[1]
        dp[2] = nums[0] + nums[2]
        max1 = max(dp[0],dp[1],dp[2])
        for i in range(3,len(nums)):
            dp[i] = nums[i] + max(dp[i-2],dp[i-3])
            if dp[i] > max1:
                max1 = dp[i]

        return(max1)
