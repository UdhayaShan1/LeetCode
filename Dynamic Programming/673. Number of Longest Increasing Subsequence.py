class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
            if len(set(nums)) == 1:
                return len(nums)
            dp = {}
            dp[0] = 1
            dp2 = {}
            dp2[0] = 1

            for i in range(1,len(nums)):
                max1 = 0
                for j in range(0,i):
                    if nums[i] > nums[j]:
                        if dp[j] > max1:
                            max1 = dp[j]
                dp[i] = 1 + max1
                dp2[i] = max1
            
            longest = max(dp.values())
            
            dp3 = {}
            dp3[0] = 1

            for i in range(1,len(nums)):
                find = dp2[i]
                count = 0
                for j in range(0,i):
                    if dp[j] == find and nums[i] > nums[j]:
                        count += dp3[j]
                dp3[i] = count
                if count == 0:
                    dp3[i] = 1
            count = 0
            for i in list(dp.keys()):
                if dp[i] == longest:
                    count += dp3[i]
            return count
