class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        dp = {}
        for i in nums:
            if i not in dp:
                dp[i] = 1
            else:
                dp[i] += 1
                
        set1 = list(set(nums))
        count = 0
        for i in range(len(set1)):
            if (k-set1[i]) not in dp:
                continue
            count1 = dp[set1[i]]
            count2 = dp[k-set1[i]]
            if set1[i] == k-set1[i]:
                count += count2//2
                dp[set1[i]] = count % 2
                continue
            dp[set1[i]] -= min(count1,count2)
            dp[k-set1[i]] -= min(count1,count2)
            count += min(count1,count2)
        return(count)
