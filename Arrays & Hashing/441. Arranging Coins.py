class Solution:
    def arrangeCoins(self, n: int) -> int:
        sum1 = 0
        count = 0
        for i in range(1,10**6):
            sum1 += i
            count += 1
            if sum1 > n:
                break
        return count-1
