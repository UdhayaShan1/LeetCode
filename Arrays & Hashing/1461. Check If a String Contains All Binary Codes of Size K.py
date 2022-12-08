class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        dp2 = {}
        for i in range(len(s)):
            tmp = s[i:i+k]
            if len(tmp) != k:
                continue
            if tmp not in dp2:
                dp2[tmp] = 1
        return(len(dp2.keys())==2**k)
