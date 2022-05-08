class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        dp = {}
        for i in arr:
            if i not in dp:
                dp[i] = 1
            else:
                dp[i] += 1

        values = list(dp.values())
        values.sort()
        values = values[::-1]
        count = 0
        count2 = 0
        for i in values:
            count += i
            count2 += 1
            if count >= len(arr)/2:
                break
        return(count2)
