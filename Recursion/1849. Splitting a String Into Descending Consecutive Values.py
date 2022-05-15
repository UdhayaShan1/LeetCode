class Solution:
    def splitString(self, s: str) -> bool:
        global flag
        if len(s) == 1:
            return False
        list1 = []
        b1 = False
        start = 1
        while b1==False:
            list1.append(s[:start])
            start+=1
            if start == len(s):
                break

        res = []
        flag = 0
        def recurse(arr,s2):
            global flag
            if len(s2) == 0:
                res.append(arr.copy())
                flag+=1
                return True
            for i in range(0,len(s2)+1):
                temp = s2[:i]
                if temp == "":
                    continue
                if int(temp) + 1 == int(arr[-1]):
                    arr.append(temp)
                    s3 = s2[i:]
                    recurse(arr,s3)
                    arr.pop()

        for i in list1:
            recurse([i],s[len(i):])

        return(flag>=1)
