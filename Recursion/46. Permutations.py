class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        global res
        res = []
        def permute(nums,i):
            global res
            if i == len(nums):
                return True
            for i in range(i,len(nums)):
                for j in range(i+1,len(nums)):
                    temp1 = nums[i]
                    temp2 = nums[j]
                    nums2 = nums.copy()
                    nums2[i] = temp2
                    nums2[j] = temp1
                    res.append(nums2)
                    permute(nums2,i+1)

        permute(nums,0)
        res.append(nums)

        return(res)
