class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dp = {}
        for i in nums:
            if i not in dp:
                dp[i] = 1
            else:
                dp[i] += 1
        for i in nums:
            if dp[i] >= 2:
                return i
