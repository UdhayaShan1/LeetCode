class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        dp = {}
        for i in range(len(s)):
            tmp = s[i:i+10]
            if len(tmp) == 10:
                if tmp not in dp:
                    dp[tmp] = 1
                else:
                    dp[tmp] += 1
        res = []
        for i in dp.keys():
            if dp[i] > 1:
                res.append(i)
        return res
