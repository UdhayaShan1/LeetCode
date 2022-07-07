class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        nums = []
        for i in range(1,maxChoosableInteger+1):
            nums.append(i)

        dp = {}
        def CanWin(amount,nums):
            if nums[-1] + amount >= desiredTotal:
                return True
            if (amount,tuple(nums)) in dp:
                return dp[(amount,tuple(nums))]

            for i in range(len(nums)):
                y1 = CanWin(amount+nums[i],nums[:i]+nums[i+1:])
                if not y1:
                    dp[(amount,tuple(nums))] = True
                    return True
            dp[(amount,tuple(nums))] = False
            return False

        return(CanWin(0,nums))
