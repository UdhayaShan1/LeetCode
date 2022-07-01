class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = {}
        dp2 = {}
        dp[0] = 1
        dp2[0] = [nums[0]]

        for i in range(1,len(nums)):
            max1 = 0
            temp = -1
            for j in range(0,i):
                if nums[i] % nums[j] == 0:
                    if dp[j] >= max1:
                        max1 = dp[j]
                        temp = dp2[j].copy()
            dp[i] = 1+max1
            if temp != -1:
                temp.append(nums[i])
                dp2[i] = temp
            else:
                dp2[i] = [nums[i]]

        max1 = max(dp.values())
        for i in dp.keys():
            if dp[i] == max1:
                return dp2[i]
