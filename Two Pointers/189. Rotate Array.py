class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        dp = {}
        for i in range(len(nums)):
            dp[(i+k)%len(nums)] = nums[i]

        for i in range(len(nums)):
            nums[i] = dp[i]
