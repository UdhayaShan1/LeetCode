class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dp = {}
        for i in wordDict:
            dp[i] = 1

        res = []

        def recurse(k,arr):
            if len(''.join(arr)) == len(s):
                res.append(' '.join(arr))
                return True
            if len(''.join(arr)) > len(s):
                return False

            for i in range(k,len(s)):
                temp = s[k:i+1]
                if temp in dp:
                    arr.append(temp)
                    recurse(i+1,arr)
                    arr.pop()

        recurse(0,[])
        return(res)
