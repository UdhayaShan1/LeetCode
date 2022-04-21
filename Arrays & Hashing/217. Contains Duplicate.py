class Solution:
    def containsDuplicate(self, nums: List[int], dp1 = {}) -> bool:
        dp = {}
        flag = 0
        for i in range(len(nums)):
            if nums[i] not in dp:
                dp[nums[i]] = 0
            else:
                flag+=1
                break
                dp[nums[i]] += 1
        if flag > 0:
            return True
        else:
            return False
