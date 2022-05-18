class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums2 = nums.copy()
        res = []
        b1 = False
        dp = {}
        dp_list = {}
        dp2 = {}
        for i in range(len(nums)):
            if nums[i] not in dp_list:
                dp_list[nums[i]] = []
                dp_list[nums[i]].append(i)
            else:
                dp_list[nums[i]].append(i)

        while b1==False:
            start = len(nums2)-1
            ref = target-nums2[start]
            ref2 = nums2[start]
            nums2 = nums2[:start]
            if len(nums2) <= 2:
                break
            for i in range(len(nums2)):
                for j in range(i+1,len(nums2)):
                    temp1 = nums2[i]
                    temp2 = nums2[j]
                    to_find = ref - (temp1+temp2)
                    temp3 = [temp1,temp2,to_find]
                    temp3.sort()
                    if tuple(temp3) not in dp2:
                        dp2[tuple(temp3)] = 1
                    else:
                        continue
                    if to_find not in dp_list:
                        continue
                    for k in dp_list[to_find]:
                        if k <= i or k <= j or k >= start:
                            continue
                        y1 = [temp1,temp2,to_find,ref2]
                        y1.sort()
                        if tuple(y1) not in dp:
                            res.append(y1)
                            dp[tuple(y1)] = 1


        return(res)

