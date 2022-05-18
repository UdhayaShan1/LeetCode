class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        nums2 = nums.copy()
        res = []
        b1 = False
        dp = {}
        while b1==False:
            start = len(nums2)-1
            ref = nums2[start]
            nums2 = nums2[:start]
            if len(nums2) <= 2:
                break
            for i in range(len(nums2)):
                for j in range(i+1,len(nums2)):
                    for k in range(j+1,len(nums2)):
                        if nums2[i]+nums2[j]+nums2[k] == ref:
                            res.append([i,j,k])

        return(len(res))
