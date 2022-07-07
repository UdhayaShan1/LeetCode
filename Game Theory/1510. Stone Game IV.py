class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        nums = []
        for i in range(1,n+1):
            if int(i**0.5) == i**0.5:
                nums.append(i)
        @functools.lru_cache(None)
        def CanWin(n):
            if n == 1:
                return True
            if n == 0:
                return False

            for i in range(len(nums)):
                if nums[i] > n:
                    continue
                y1 = CanWin(n-nums[i])
                if not y1:
                    return True
            return False

        return(CanWin(n))
