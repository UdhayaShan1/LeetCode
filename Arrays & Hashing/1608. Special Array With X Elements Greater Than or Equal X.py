class Solution:
    def specialArray(self, nums: List[int]) -> int:
        final = -1
        for i in range(0,max(nums)+1):
            count = 0
            for j in nums:
                if j >= i:
                    count+=1
            if count == i:
                final = count
                break

        if final == -1:
            return -1
        else:
            return final
