class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        import sys
        @functools.lru_cache(None)
        def CanWin(Alice,k1,M):

            if Alice == True:
                if k1 >= len(piles):
                    return 0

                y1 = -sys.maxsize
                for i in range(1,2*M+1):
                    x = CanWin(False,k1+i,max(i,M))+sum(piles[k1:k1+i])
                    if x > y1:
                        y1 = x
                return y1
            else:
                if k1 >= len(piles):
                    return 0

                y1 = sys.maxsize
                for i in range(1,2*M+1):
                    x = CanWin(True,k1+i,max(i,M))-sum(piles[k1:k1+i])
                    if x < y1:
                        y1 = x
                return y1
        x = (sum(piles)+(CanWin(True,0,1)))//2
        return x
