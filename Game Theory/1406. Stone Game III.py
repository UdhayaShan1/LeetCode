class Solution:
    def stoneGameIII(self, values: List[int]) -> str:
        import sys
        @functools.lru_cache(None)
        def CanWin(Alice,k1):
            if k1 >= len(values):
                return 0

            if Alice == True:
                y1 = -sys.maxsize
                for i in range(1,4):
                    x = CanWin(False,k1+i)+sum(values[k1:k1+i])
                    if x > y1:
                        y1 = x
                return y1
            else:
                y1 = sys.maxsize
                for i in range(1,4):
                    x = CanWin(True,k1+i)-sum(values[k1:k1+i])
                    if x < y1:
                        y1 = x
                return y1

        x=(CanWin(True,0))
        if x == 0:
            return "Tie"
        elif x > 0:
            return "Alice"
        else:
            return "Bob"
