class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        dp = {}
        def Permute2(nums,k):
            if k >= len(nums):
                return False
              
            for i in range(k,len(nums)):
                for j in range(i,len(nums)):
                    temp1 = nums[i]
                    temp2 = nums[j]
                    if i == j:
                        nums2 = nums.copy()
                        nums2[i] = temp2
                        nums2[j] = temp1
                        y1 = tuple(nums2)
                        if y1 not in dp:
                            dp[y1] = 1
                            res.append(nums2)
                        Permute2(nums2,i+1)
                    else:
                        if temp1 == temp2:
                            continue
                        nums2 = nums.copy()
                        nums2[i] = temp2
                        nums2[j] = temp1
                        y1 = tuple(nums2)
                        if y1 not in dp:
                            dp[y1] = 1
                            res.append(nums2)
                        Permute2(nums2,i+1)
        Permute2(nums,0)
        return(res)    
