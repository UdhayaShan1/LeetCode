class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        global flag
        res = []
        flag = 0
        def recurse(arr,k):
            global flag
            if len(''.join(arr)) == len(num) and len(arr)>=3:
                flag+=1
                res.append(arr.copy())
                return True
            if len(''.join(arr)) > len(num):
                return False


            for i in range(k,len(num)):
                temp = num[k:i+1]
                if len(str(int(temp))) != len(temp):
                    continue
                if len(arr) <= 1:
                    arr.append(temp)
                    recurse(arr,i+1)
                    arr.pop()
                else:
                    if int(temp) == (int(arr[-1])+int(arr[-2])):
                        arr.append(temp)
                        recurse(arr,i+1)
                        arr.pop()

        recurse([],0)


        return flag>=1
