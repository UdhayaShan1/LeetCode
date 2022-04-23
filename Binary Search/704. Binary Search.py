class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = -1
        nums.sort()
        b1 = False
        compen = 0
        while b1==False:
            middle = len(nums)//2
            if nums[middle] == target:
                index = middle
                break
            if nums[middle] > target:
                nums = nums[:middle]
            else:
                nums = nums[middle+1:]
                compen += (middle+1)
            if len(nums) == 0:
                break

        if index == -1:
            return(-1)
        else:
            return(index+compen)
