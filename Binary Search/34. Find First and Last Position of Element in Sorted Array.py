class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        nums2 = nums.copy()
        nums3 = nums.copy()
        b1 = False
        left = 0
        while b1==False:
            if len(nums2) <= 0:
                break
            middle = len(nums2)//2
            if target > nums2[middle]:
                left += middle+1
                nums2 = nums2[middle+1:]
            elif target < nums2[middle]:
                nums2 = nums2[:middle]
            elif target == nums2[middle]:
                nums2 = nums2[:middle]

        left1 = 0
        while b1==False:
            if len(nums3) <= 0:
                break
            middle = len(nums3)//2
            if target > nums3[middle]:
                left1 += middle+1
                nums3 = nums3[middle+1:]
            elif target < nums3[middle]:
                nums3 = nums3[:middle]
            elif target == nums3[middle]:
                nums3 = nums3[middle+1:]
                left1+=middle+1
        if left == left1:
            return([-1,-1])
        return(left,left1-1)
