class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        import math
        first_digit = math.ceil(k / math.factorial(n-1))
        nums = []
        for i in range(1,n+1):
            if i == first_digit:
                continue
            nums.append(i)


        res = []
        dp2 = {}

        def recurse(str1):
            if len(str1) == n-1:
                res.append(str(first_digit)+str1)
                return    

            for i in range(len(nums)):
                if i in dp2:
                    continue
                dp2[i] = 1
                str2 = str1
                str2 += str(nums[i])
                y1 = recurse(str2)
                del dp2[i]
        recurse("")
        return(res[k%math.factorial(n-1)-1])
    
