class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = {}
        def dfs(k,sum1):
            if sum1 == target:
                return 1
            if k > len(nums):
                return 0
            if sum1 > target:
                return 0
            if (k,sum1) in dp:
                return dp[(k,sum1)]

            y1 = 0
            for i in range(len(nums)):
                y1 += dfs(i,sum1+nums[i])
                dp[(k,sum1)] = y1

            return dp[(k,sum1)]

        return(dfs(0,0))
