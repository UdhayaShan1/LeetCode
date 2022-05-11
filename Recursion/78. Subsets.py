class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        global res
        global dp
        res = []
        dp = {}
        def subsets(arr,nums,min1):
            global res
            global dp
            if len(arr) <= len(nums):
                res.append(arr.copy())
            if len(arr) > len(nums):
                return False

            for i in range(len(nums)):
                if nums[i] <= min1:
                    continue
                if nums[i] not in arr:
                    arr.append(nums[i])
                    subsets(arr,nums,nums[i])
                    arr.pop()

        subsets([],nums,-21)

        return(res)
