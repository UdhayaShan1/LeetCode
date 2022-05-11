class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pop_count = 0
        for i in range(len(nums)):
            if nums[i-pop_count] == 0:
                nums.pop(i-pop_count)
                pop_count+=1
        for i in range(pop_count):
            nums.append(0)
