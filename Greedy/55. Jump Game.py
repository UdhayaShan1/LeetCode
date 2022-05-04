class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = {}
        dp[len(nums)-1] = True

        for i in range(len(nums)-2,-1,-1):
            flag = 0
            if dp[i+1] == True and nums[i] != 0:
                dp[i] = True
                continue
            for j in range(i+1,i+nums[i]+1):
                if dp[j] == True:
                    flag+=1
                    break
            if flag == 1:
                dp[i] = True
            else:
                dp[i] = False

        return dp[0]
