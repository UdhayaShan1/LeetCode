class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        import math

        start = max(nums)
        end = 1


        b1 = False
        while b1==False:
            mid = (start+end)//2
            count = 0
            if start == end:
                break
            for i in nums:
                count += math.ceil(i/mid)
            if count > threshold:
                end = mid+1
                continue
            if count <= threshold:
                start = mid
                continue

        return(start)
