class Solution:
    def maxLength(self, arr1: List[str]) -> int:
        global max1
        char_count = 0
        for i in arr1:
            char_count+=len(i)

        res = []
        max1 = 0
        def recurse(arr,k):
            global max1
            if len(arr) < char_count:
                temp = ''.join(arr.copy())
                if len(set(temp)) == len(temp):
                    if len(temp) > max1:
                        max1 = len(temp)
                    res.append(temp)
            if len(arr) == char_count:
                temp = ''.join(arr.copy())
                if len(set(temp)) == len(temp):
                    if len(temp) > max1:
                        max1 = len(temp)
                    res.append(temp)
                return True
            if len(arr) > char_count:
                return False
              
            for i in range(k,len(arr1)):
                count = len(arr1[i])
                arr += (list(arr1[i]))
                recurse(arr,i+1)
                for j in range(count):
                    arr.pop()

        recurse([],0)

        return(max1)
