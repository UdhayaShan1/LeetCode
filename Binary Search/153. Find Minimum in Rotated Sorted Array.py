class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[-1] > nums[0]:
            return(nums[0])
        else:
            b1 = False
            ref = nums.copy()
            min1 = 1000000
            b1 = False
            while b1==False:
                mid = len(ref)//2
                if ref[mid] < ref[0]:
                    ref = ref[0:mid+1]
                else:
                    ref = ref[mid:]
                if len(ref) <= 2:
                    break
            return(min(ref))
