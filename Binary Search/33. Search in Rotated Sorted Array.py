class Solution:
    def search(self, nums: List[int], target: int) -> int:
        b1 = False
        left = 0
        while b1==False:
            mid = len(nums) // 2
            flag = 0
            if nums[mid] >= nums[0]:
                if target >= nums[0] and target <= nums[mid]:
                    nums = nums[0:mid+1]
                else:
                    nums = nums[mid:]
                    left += (mid-0)
            elif nums[mid] <= nums[-1]:
                if target >= nums[mid] and target <= nums[-1]:
                    nums = nums[mid:]
                    left += mid
                else:
                    nums = nums[:mid+1]
            if len(nums) <= 2:
                break

        if target not in nums:
            return(-1)
        else:
            return(left + nums.index(target))
        
