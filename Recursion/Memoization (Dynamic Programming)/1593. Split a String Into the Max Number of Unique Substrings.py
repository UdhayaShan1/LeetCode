class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        import sys
        dp = {}
        dp2 = {}
        def dfs(k1,arr):
            if k1 >= len(s):
                return 0

            if (k1,tuple(arr)) in dp:
                return dp[(k1,tuple(arr))]

            y1 = -sys.maxsize
            for i in range(k1,len(s)):
                temp = s[k1:i+1]
                if temp in dp2:
                    continue
                arr.append(temp)
                dp2[temp] = 1
                x = dfs(i+1,arr)+1
                if x > y1:
                    y1 = x
                del dp2[temp]
                arr.pop()
            dp[(k1,tuple(arr))] = y1
            return y1

        return(dfs(0,[]))
