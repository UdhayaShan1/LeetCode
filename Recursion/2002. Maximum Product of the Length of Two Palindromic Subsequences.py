class Solution:
    def maxProduct(self, s: str) -> int:
        global min1
        res = []

        import sys
        min1 = -sys.maxsize
        @functools.lru_cache(None)
        def dfs(arr1,arr2,k1):
            global min1
            if len(arr1) > 0 and len(arr2) > 0:
                str1 = ''.join(arr1)
                str2 = ''.join(arr2)
                if str1 == str1[::-1] and str2 == str2[::-1]:
                    if len(str1)*len(str2) > min1:
                        min1 = len(str1)*len(str2)
            if k1 >= len(s):
                return True

            excl = dfs(arr1,arr2,k1+1)

            arr1.append(s[k1])
            incl_one = dfs(arr1,arr2,k1+1)
            arr1.pop()

            arr2.append(s[k1])
            incl_one = dfs(arr1,arr2,k1+1)
            arr2.pop()

        dfs([],[],0)
        return(min1)
