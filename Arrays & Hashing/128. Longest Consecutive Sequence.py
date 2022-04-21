class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        streak = 0
        if len(nums) == 0:
            return 0
        else:
            max1 = 1
            for i in range(1,len(nums)):
                if nums[i] - nums[i-1] == 1:
                    streak+=1
                if i == len(nums)-1:
                    if streak > 0:
                        if streak + 1>max1:
                            max1 = streak + 1
                    streak = 0
                elif nums[i] - nums[i-1] != 1:
                    if streak > 0:
                        if streak + 1>max1:
                            max1 = streak + 1
                    streak = 0

            return(max1)
