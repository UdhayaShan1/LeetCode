class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dp = {}
        max1 = 0
        flag = 0
        for i in range(len(s)):
            if flag == 0:
                start = s[i]
                start1 = i
                flag+=1
            if s[i] not in dp:
                dp[s[i]] = 1
            else:
                dp[s[i]] += 1
            if (sum(list(dp.values())))-max(list(dp.values())) <= k:
                if (sum(list(dp.values()))) > max1:
                    max1 = sum(list(dp.values()))
            else:
                dp[start] -= 1
                if dp[start] <= 0:
                    dp[start] = 0
                start = s[start1+1]
                start1 += 1

        return(max1)
