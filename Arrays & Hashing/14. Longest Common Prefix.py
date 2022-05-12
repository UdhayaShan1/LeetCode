class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        str1 = strs[0]
        for i in range(len(str1),-1,-1):
            flag = 0
            prefix = str1[0:i]
            for j in strs:
                if j[0:i] == prefix:
                    flag+=1
                    continue
            if flag == len(strs):
                break
        return(prefix) 
