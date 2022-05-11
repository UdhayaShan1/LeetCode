class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        global res
        global dp
        res = []
        dp = {}
        def subsets(arr,nums,k):
            global res
            if len(arr) <= len(nums):
                y1 = arr.copy()
                y1.sort()
                y1 = tuple(y1)
                if y1 not in dp:
                    dp[y1] = 1
                    res.append(list(y1))
            if len(arr) > len(nums):
                return False

            for i in range(k,len(nums)):
                arr.append(nums[i])
                subsets(arr,nums,i+1)
                arr.pop()

        subsets([],nums,0)

        return(res)
