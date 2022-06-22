class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dp = {}
        dp2 = {}
        str2 = ""

        for i in range(len(s)):
            ref1 = s[i]
            ref2 = t[i]
            if ref1 not in dp:
                if ref2 in dp2:
                    str2 += "!"
                    continue
                dp[ref1] = ref2
                dp2[ref2] = ref1
                str2+=dp[ref1]
            else:
                if ref2 not in dp2:
                    str2 += "!"
                    continue
                if dp2[ref2] != ref1:
                    str2 += "!"
                str2+=dp[ref1]

        return(str2==t)
