class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        global count
        import sys
        dp = {}
        count = 0
        def dfs(arr1,nums):
            global count
            key = (tuple(arr1),tuple(nums))
            if len(nums) == 0:
                count+=1
                return 1

            if key in dp:
                return dp[key]

            y1 = 0
            for i in range(len(nums)):
                if len(arr1) == 0:
                    arr1.append(nums[i])
                    y1 += dfs(arr1,nums[:i]+nums[i+1:])
                    arr1.pop()
                else:
                    if (nums[i] + arr1[-1])**0.5 == int((nums[i] + arr1[-1])**0.5):
                        arr1.append(nums[i])
                        y1 += dfs(arr1,nums[:i]+nums[i+1:])
                        arr1.pop()
            dp[key] = y1
            return y1

        (dfs([],nums))
        return count
