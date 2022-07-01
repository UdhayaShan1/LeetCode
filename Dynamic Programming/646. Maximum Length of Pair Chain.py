class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        dp = {}
        dp[0] = 1

        for i in range(1,len(pairs)):
            max1 = 0
            for j in range(0,i):
                if pairs[i][0] > pairs[j][-1]:
                    if dp[j] > max1:
                        max1 = dp[j]
            dp[i] = 1+max1

        return(max(dp.values()))
