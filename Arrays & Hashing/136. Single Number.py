class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dp = {}
        dp2 = {}
        for i in nums:
            if i not in dp:
                dp[i] = 1
                dp2[i] = 1
            else:
                dp[i] += 1
                del dp2[i]

        return(list(dp2.keys())[0])
