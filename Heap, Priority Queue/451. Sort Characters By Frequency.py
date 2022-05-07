class Solution:
    def frequencySort(self, s: str) -> str:
        dp = {}
        for i in s:
            if i not in dp:
                dp[i] = 1
            else:
                dp[i] += 1

        dp2 = {k: v for k, v in sorted(dp.items(), key=lambda item: item[1])}

        str1 = ""

        for i in list(dp2.keys())[::-1]:
            str1 += dp2[i] * i

        return(str1)
