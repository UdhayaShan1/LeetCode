class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {}
        @functools.lru_cache(None)
        def CanWin(Alice,score1,score2,i,j):

            if Alice == True:
                if i == j:
                    if score1 > score2:
                        return True
                    else:
                        return False
                if i+1 == j:
                    if score1 + max(piles[i],piles[j]) > score2:
                        return True
                    else:
                        return False

                for k in [i,j]:
                    if k == i:
                        y1 = CanWin(False,score1+piles[k],score2,i+1,j)
                        if not y1:
                            return True
                    else:
                        y1 = CanWin(False,score1+piles[k],score2,i,j-1)
                        if not y1:
                            return True
                return False
            else:
                if i == j:
                    if score2 > score1:
                        return True
                    else:
                        return False
                if i+1 == j:
                    if score2 + max(piles[i],piles[j]) > score1:
                        return True
                    else:
                        return False

                for k in [i,j]:
                    if k == i:
                        y1 = CanWin(False,score1,score2+piles[k],i+1,j)
                        if not y1:
                            return True
                    else:
                        y1 = CanWin(False,score1,score2+piles[k],i,j-1)
                        if not y1:
                            return True
                return False
        return CanWin(True,0,0,0,len(piles)-1)
