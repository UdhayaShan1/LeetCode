from typing import (
    List,
)

class Solution:
    """
    @param nums: a list of integer
    @return: return a integer, denote  the maximum number of consecutive 1s
    """
    def find_max_consecutive_ones(self, nums: List[int]) -> int:
        # write your code here
        dp_flip = {}
        dp_og = {}

        if nums[0] == 1:
            dp_og[0] = 1
            dp_flip[0] = 1
        else:
            dp_og[0] = 0
            dp_flip[0] = 1

        for i in range(1,len(nums)):
            if nums[i] == 1:
                dp_og[i] = 1 + dp_og[i-1]
            else:
                dp_og[i] = 0
            
        for i in range(1,len(nums)):
            if nums[i] == 1:
                dp_flip[i] = 1 + max(dp_og[i-1],dp_flip[i-1])
            else:
                dp_flip[i] = 1 + dp_og[i-1]

        return(max(list(dp_flip.values())))
