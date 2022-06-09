class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if len(pattern) != len(s.split()):
            return False
        s = s.split()

        dp = {}
        dp2 = {}

        list1 = [pattern[0]]
        dp[s[0]] = pattern[0]
        dp2[pattern[0]] = s[0]
        for i in range(1,len(s)):
            if s[i] not in dp:
                if pattern[i] in dp2:
                    continue
                list1.append(pattern[i])
                dp[s[i]] = pattern[i]
                dp2[pattern[i]] = s[i]
            else:
                list1.append(dp[s[i]])

        return(''.join(list1) == pattern)
