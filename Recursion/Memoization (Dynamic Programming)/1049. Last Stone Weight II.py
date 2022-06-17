class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        import sys
        dp = {}
        def dfs(k1,amount):
            if k1>=len(stones):
                if amount < 0:
                    return sys.maxsize
                return amount

            if (k1,amount) in dp:
                return dp[(k1,amount)]

            pos = dfs(k1+1,amount+stones[k1])
            neg = dfs(k1+1,amount-stones[k1])
            dp[(k1,amount)] = min(pos,neg)
            return dp[(k1,amount)]

        return(dfs(0,0))
