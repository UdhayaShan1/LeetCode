class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        dp = {}
        dp[0] = 1
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                dp[i] = 1 + dp[i-1]
            else:
                dp[i] = 1

        return(max(dp.values()))
