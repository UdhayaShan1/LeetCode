class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        dp = {}
        def recurse(k,arr,prev):
            key = tuple(arr)
            if len(arr) < len(nums) and len(arr) > 1:
                if key in dp:
                    return False
                res.append(arr[:])
                dp[key] = 1
            if len(arr) == len(nums) and len(arr) > 1:
                if key in dp:
                    return False
                res.append(arr[:])
                dp[key] = 1
                return True
            if len(arr) > len(nums):
                return False


            for i in range(k,len(nums)):
                if nums[i] >= prev:
                    arr.append(nums[i])
                    recurse(i+1,arr,nums[i])
                    arr.pop()

        recurse(0,[],min(nums))

        return(res)
