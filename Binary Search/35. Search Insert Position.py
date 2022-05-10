class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        b1 = False
        left = 0
        flag = 0
        while b1==False:
            if len(nums) == 0:
                break
            index = len(nums)//2
            if nums[index] < target:
                nums = nums[index+1:]
                left += index+1
            elif nums[index] > target:
                nums = nums[:index]
            else:
                nums = nums[index:]
                left += index
                flag+=1
                break
        return(left)
