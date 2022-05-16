class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        b1 = False
        while b1==False:
            flag = 0
            for i in range(1,len(words)):
                temp1 = list(words[i])
                temp2 = list(words[i-1])
                temp1.sort()
                temp2.sort()
                if temp1 == temp2:
                    words.pop(i)
                    flag+=1
                    break
            if flag == 0:
                break

        return(words)
    
        
    
