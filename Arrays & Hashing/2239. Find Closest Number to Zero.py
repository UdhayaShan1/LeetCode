class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        max1 = 1000000000
        num1 = 0
        final = []
        for i in nums:
            diff = abs(i)
            if diff < max1:
                final = [i]
                max1 = diff
                num1 = i
            elif diff == max1:
                final.append(i)
        return(max(final))
