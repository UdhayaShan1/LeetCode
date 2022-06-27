class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        start = 1
        end = 10**9
        
        b1 = False
        while b1==False:
            middle = (start+end)//2
            if abs(start-end) <= 1:
                break
            nums = []
            for i in bloomDay:
                if i <= middle:
                    nums.append(1)
                else:
                    nums.append(0)

            dp = {}
            if nums[0] == 0:
                dp[0] = 0
            else:
                dp[0] = 1
            for i in range(1,len(nums)):
                if nums[i] == 0:
                    dp[i] = 0
                else:
                    dp[i] = 1 + dp[i-1]
                    dp[i-1] = 0

            bouquets = 0
            for i in dp.values():
                bouquets += (i//k)
            if bouquets < m:
                start = middle+1
                continue
            if bouquets >= m:
                end = middle
                continue
        
        for j in [min(start,end),max(start,end)]:
            nums = []
            for i in bloomDay:
                if i <= j:
                    nums.append(1)
                else:
                    nums.append(0)

            dp = {}
            if nums[0] == 0:
                dp[0] = 0
            else:
                dp[0] = 1
            for i in range(1,len(nums)):
                if nums[i] == 0:
                    dp[i] = 0
                else:
                    dp[i] = 1 + dp[i-1]
                    dp[i-1] = 0
                    
            bouquets = 0
            for i in dp.values():
                bouquets += (i//k)

            if bouquets >= m:
                return j
        return -1
