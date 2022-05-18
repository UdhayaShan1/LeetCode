class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        def recurse(arr,k,str1):
            if len(arr) > 4:
                return False
            temp1 = ''.join(arr[:])
            if len(temp1) == len(s) and len(arr) == 4:
                res.append('.'.join(arr[:]))
                return True
            if len(temp1) > len(s):
                return False

            for i in range(len(str1)):
                temp = str1[:i+1]
                str2 = str1[i+1:]
                temp = str(int(temp))
                if int(temp) <= 255:
                    arr.append(temp)
                    recurse(arr,i+1,str2)
                    arr.pop()

        recurse([],0,s)

        return(res)
            
        
