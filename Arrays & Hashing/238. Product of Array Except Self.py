class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        dp = {}
        for i in range(len(nums)):
            if i == 0:
                dp[0] = nums[0]
            else:
                dp[i] = 1
                dp[i] = dp[i-1] * nums[i]

        dp1 = {}

        for i in range(len(nums)-1,-1,-1):
            if i == len(nums)-1:
                dp1[i] = nums[-1]
            else:
                dp1[i] = 1
                dp1[i] = dp1[i+1] * nums[i]

        final = []


        for i in range(len(nums)):
            if i == 0:
                final.append(dp1[i+1])
            elif i == len(nums)-1:
                final.append(dp[i-1])
            else:
                final.append(dp[i-1] * dp1[i+1])


        return(final)
