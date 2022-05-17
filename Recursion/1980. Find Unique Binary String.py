class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        global count
        dp = {}
        for i in nums:
            dp[i] = 1
        res = []
        count = 0
        def recurse(arr):
            global count
            if count > 0:
                return False
            if len(arr) == len(nums[0]):
                temp = ''.join(arr[:])
                if temp not in dp:
                    count+=1
                    res.append(temp)
                return True
            if len(arr) > len(nums[0]):
                return False
            arr.append("1")
            recurse(arr)
            arr.pop()
            arr.append("0")
            recurse(arr)
            arr.pop()

        recurse([])
        return(res[0])
