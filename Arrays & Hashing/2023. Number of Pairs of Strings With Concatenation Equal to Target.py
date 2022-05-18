class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        dp = {}
        count = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                temp = [i,j]
                if tuple(temp) in dp:
                    continue
                if nums[i]+nums[j] == target:
                    count+=1
                    dp[tuple(temp)] = 1
        return count
