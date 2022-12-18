class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        end = len(nums)-1
        count = 0
        for i in range(len(nums)):
            b1 = False
            while b1==False:
                if nums[i]+nums[end] <= target:
                    break
                end-=1
                if end < i:
                    break
            if end < i:
                break
            count += 2**(end-i)
        return count%(10**9+7) 
