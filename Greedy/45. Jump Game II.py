class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = {}
        dp2 = {}
        dp[len(nums)-1] = True
        dp2[len(nums)-1] = 0

        for i in range(len(nums)-2,-1,-1):
            flag = 0
            min1 = 1000000000
            for j in range(i+1,i+nums[i]+1):
                if j >= len(nums):
                    break
                if dp[j] == True:
                    flag+=1
                    if dp2[j] <= min1:
                        min1 = dp2[j]
            if flag >= 1:
                dp[i] = True
                dp2[i] = 1+min1
            else:
                dp[i] = False

        return dp2[0]
