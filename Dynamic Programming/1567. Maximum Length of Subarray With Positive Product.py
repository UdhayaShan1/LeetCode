class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        zero = [i for i, x in enumerate(nums) if x == 0]
        if len(zero) > 0:
            list1 = []
            start = 0
            for i in range(len(zero)):
                list1.append(nums[start:zero[i]])
                start = zero[i]+1  
            list1.append(nums[zero[-1]+1:])
        else:
            list1 = [nums[:]]

        def Check(list2):
            if len(list2) == 1:
                if list2[0] > 0:
                    return 1
                else:
                    return 0
            dp1 = {}
            dp2 = {}
            max1 = 0
            if list2[0] > 0:
                dp1[0] = 1
                dp2[0] = 0
            else:
                dp1[0] = 0
                dp2[0] = 1

            for i in range(1,len(list2)):
                dp1[i] = 0
                dp2[i] = 0
                if list2[i] > 0:
                    dp1[i] = 1+dp1[i-1]
                    if dp2[i-1] > 0:
                        dp2[i] = 1 + dp2[i-1]
                    if dp1[i] > max1:
                        max1 = dp1[i]
                else:
                    if dp2[i-1] > 0:
                        dp1[i] = 1 + dp2[i-1]
                    if dp1[i-1] >= 0:
                        dp2[i] = 1 + dp1[i-1]
                    if dp1[i] > max1:
                        max1 = dp1[i]
            return max1
        max2 = 0
        for i in list1:
            if len(i) == 0:
                continue
            y = Check(i)
            if y > max2:
                max2 = y

        return(max2)
