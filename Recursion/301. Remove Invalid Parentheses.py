class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        global max1
        global res
        import sys
        max1 = sys.maxsize
        @functools.lru_cache(None)
        def recurse(str1,count):
            global max1
            global res
            flag = 0
            left = 0
            right = 0
            for i in str1:
                if i == "(":
                    right+=1
                elif i == ")":
                    left+=1
                if left > right:
                    flag+=1
                    break
            if left != right:
                flag = 1
            
            if flag == 0 and count < max1:
                max1 = count
                res = []
                res.append(str1)
            if flag == 0 and count == max1:
                res.append(str1)
            if len(str1) == 0:
                return 0

            for i in range(len(str1)):
                if str1[i] != ")" and str1[i] != "(":
                    continue
                recurse(str1[:i]+str1[i+1:],count+1)
        recurse(s,0)
        return list(set(res))
