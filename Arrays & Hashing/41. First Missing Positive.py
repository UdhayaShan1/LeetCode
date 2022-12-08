class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        dp = {}
        for i in nums:
            if i not in dp:
                dp[i] = 1
            else:
                dp[i] += 1
        for i in range(1,2**31):
            if i not in dp:
                return i
