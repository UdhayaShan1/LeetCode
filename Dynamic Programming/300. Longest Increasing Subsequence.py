class Solution:
    def lengthOfLIS(self, list1: List[int]) -> int:
        length = len(list1)
        dp = {}
        dp[length-1] = 1
        if list1[length-2] >= list1[-1]:
            dp[length-2] = 1
        elif list1[length-2] < list1[-1]:
            dp[length-2] = 2
        max2 = max(dp[length-1],dp[length-2])
        for i in range(length-3,-1,-1):
            dp[i] = 1
            max1 = 0
            for j in range(i+1,length):
                if list1[i] < list1[j]:
                    if dp[j] > max1:
                        max1 = dp[j]
                else:
                    continue
            dp[i] += max1
            if dp[i] > max2:
                max2 = dp[i]
        return(max2)
