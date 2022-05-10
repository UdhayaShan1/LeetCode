class Solution:
    def partition(self, s: str) -> List[List[str]]:
        global res
        global part
        res = []
        part = []
        
        def recurse(str1):
            global res
            if len(str1) == 0:
                res.append(part.copy())
                return True
            for i in range(len(str1)):
                temp = str1[:i+1]
                if list(temp)[::-1] == list(temp):
                        part.append(temp)
                        recurse(str1[i+1:])
                        part.pop()

        recurse(s)
        return(res)
