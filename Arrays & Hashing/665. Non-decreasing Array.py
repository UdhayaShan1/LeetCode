class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        import sys
        flag = 0
        flag1 = 0
        prev = -sys.maxsize
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                flag+=1
                if nums[i+1] < prev:
                    flag1+=1
            prev = nums[i]
        
        flag2 = 0
        flag3 = 0
        prev = sys.maxsize
        for i in range(len(nums)-1,0,-1):
            if nums[i] < nums[i-1]:
                flag2+=1
                if nums[i-1] > prev:
                    flag3+=1
            prev = nums[i]
        
        if flag > 1 or flag1 > 0:
            if flag2 > 1 or flag3 > 0:
                return False
        return True
