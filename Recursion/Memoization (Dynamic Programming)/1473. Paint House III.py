class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:

        import sys
        dp = {}
        def dfs(k1,prevPaint,neighbourhoodcount):
            if k1 >= len(houses):
                if neighbourhoodcount == target:
                    return 0
                else:
                    return sys.maxsize

            if (k1,prevPaint,neighbourhoodcount) in dp:
                return dp[(k1,prevPaint,neighbourhoodcount)]



            if houses[k1] != 0:
                if houses[k1] != prevPaint:
                    y1 = dfs(k1+1,houses[k1],neighbourhoodcount+1)
                else:
                    y1 = dfs(k1+1,houses[k1],neighbourhoodcount)
                dp[(k1,prevPaint,neighbourhoodcount)] = y1
            else:
                y1 = sys.maxsize
                for i in range(n):
                    if (i+1) == prevPaint:
                        x = dfs(k1+1,i+1,neighbourhoodcount)+cost[k1][i]
                        if x < y1:
                            y1 = x
                    else:
                        x = dfs(k1+1,i+1,neighbourhoodcount+1)+cost[k1][i]
                        if x < y1:
                            y1 = x
                    dp[(k1,prevPaint,neighbourhoodcount)] = y1

            return dp[(k1,prevPaint,neighbourhoodcount)]

        x=(dfs(0,-1,0))
        if x >= sys.maxsize:
            return -1
        else:
            return x
