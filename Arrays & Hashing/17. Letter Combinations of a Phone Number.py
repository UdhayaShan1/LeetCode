class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dp = {}
        dp[2] = "abc"
        dp[3] = "def"
        dp[4] = "ghi"
        dp[5] = "jkl"
        dp[6] = "mno"
        dp[7] = "pqrs"
        dp[8] = "tuv"
        dp[9] = "wxyz"
        if len(digits) == 0:
            return []
        digits = str(digits)
        final = []
        for i in digits[0]:
            for j in dp[int(i)]:
                final.append(j)

        for i in range(1,len(digits)):
            temp1 = final.copy()
            final2 = []
            for j in dp[int(digits[i])]:
                temp2 = temp1.copy()
                for k in range(len(temp2)):
                    temp2[k] += j
                final2+=temp2
            final = final2

        return(final)
