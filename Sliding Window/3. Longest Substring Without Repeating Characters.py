class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        list1 = []
        max1 = 0
        for i in range(len(s)):
            if s[i] not in list1:
                list1.append(s[i])
                if len(list1) > max1:
                    max1 = len(list1)
            else:
                index = [j for j, x in enumerate(list1) if x == s[i]][0]
                list1 = list1[index+1:]
                list1.append(s[i])
                if len(list1) > max1:
                    max1 = len(list1)
        return(max1)

            
            
        

    
        
