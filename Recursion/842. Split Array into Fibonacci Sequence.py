class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:

        res = []

        def dfs(k,arr):
            if k == len(num) and len(arr) >= 3:
                res.append(arr[:])
                return True

            for i in range(k,len(num)):
                temp = num[k:i+1]
                if int(temp) >= 2**31:
                    continue
                if len(arr) <= 1:
                    if len(str(int(temp))) != len(temp):
                        continue
                    arr.append(temp)
                    dfs(i+1,arr)
                    arr.pop()
                else:
                    if len(str(int(temp))) != len(temp):
                        continue
                    if int(temp) != (int(arr[-1])+int(arr[-2])):
                        continue
                    arr.append(temp)
                    dfs(i+1,arr)
                    arr.pop()

        dfs(0,[])
        if len(res) == 0:
            return []
        return(res[0])
