#LintCode

from typing import (
    List,
)

class Solution:
    """
    @param nums: A list of integers
    @return: nothing
    """
    def wiggle_sort(self, nums: List[int]):
        # write your code here
        nums.sort()
        for i in range(1,len(nums)-1,2):
            tmp = nums[i]
            tmp2 = nums[i+1]
            nums[i] = tmp2
            nums[i+1] = tmp
