class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        list1 = []
        for i in range(1,n):
            list1.append(i)
        dp = {}

        def dfs(k,amount):
            if amount > n:
                return 0
            if k >= len(list1):
                if amount <= n:
                    return 1
                else:
                    return 0
            if (k,amount) in dp:
                return dp[(k,amount)]

            include = dfs(k,amount+list1[k])*list1[k]
            exclude = dfs(k+1,amount)
            dp[(k,amount)] = max(include,exclude)
            return dp[(k,amount)]


        return(dfs(0,0))
