class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        import sys
        @functools.lru_cache(None)
        def CanWin(player1,i,j):
            if i > j:
                return 0

            if player1 == True:
                y1 = CanWin(False,i+1,j)+nums[i]
                y2 = CanWin(False,i,j-1)+nums[j]
                return max(y1,y2)
            else:
                y1 = CanWin(True,i+1,j)-nums[i]
                y2 = CanWin(True,i,j-1)-nums[j]
                return min(y1,y2)
        x=(CanWin(True,0,len(nums)-1))
        y = (x+sum(nums))//2
        z = sum(nums)-y
        if y >= z:
            return True
        else:
            return False
