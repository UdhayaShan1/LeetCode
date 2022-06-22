class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp_one = {}
        dp_zero = {}

        for i in range(len(strs)):
            dp_one[i] = len([k for k, x in enumerate(strs[i]) if x == "1"])
            dp_zero[i] = len([k for k, x in enumerate(strs[i]) if x == "0"])

        import sys
        dp = {}
        def dfs(k1,ones,zeros):
            if k1 >= len(strs):
                if zeros <= m and ones <= n:
                    return 0
                else:
                    return -sys.maxsize
            if (k1,ones,zeros) in dp:
                return dp[(k1,ones,zeros)]
            if zeros > m or ones > n:
                return -sys.maxsize


            y1 = dfs(k1+1,ones+dp_one[k1],zeros+dp_zero[k1])+1
            y2 = dfs(k1+1,ones,zeros)
            dp[(k1,ones,zeros)] = max(y1,y2)
            return max(y1,y2)

        return(dfs(0,0,0))
