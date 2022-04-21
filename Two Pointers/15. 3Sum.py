class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        dp = {}
        for i in range(len(nums)):
            if nums[i] not in dp:
                dp[nums[i]] = []
                dp[nums[i]].append(i)
            else:
                dp[nums[i]].append(i)


        b1 = False
        start = 0
        final = []
        dp_2 = {}
        while b1==False:
            if start == len(nums):
                break
            ref1 = nums[start]
            if ref1 not in dp_2:
                dp_2[ref1] = 1
            else:
                start+=1
                continue
            c1 = False
            count = 1
            while c1==False:
                if start + count >= len(nums):
                    break
                ref2 = nums[start+count]
                diff = 0-(ref1+ref2)
                flag = 0
                if diff in dp:
                    for j in dp[diff]:
                        if j <= start+count:
                            continue
                        if j != (start) and j != (start+count):
                            temp = [nums[start],nums[start+count],nums[j]]
                            temp.sort()
                            if len(final) > 0:
                                if temp != final[-1]:
                                    final.append(temp)
                            else:
                                final.append(temp)
                            break
                count+=1
            start+=1

        return(final)
      
