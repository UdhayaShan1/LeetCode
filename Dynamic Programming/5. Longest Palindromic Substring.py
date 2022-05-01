class Solution:
    def longestPalindrome(self, s: str) -> str:
        min1 = 0
        final_str = ""
        for i in range(len(s)):
            b1 = False
            count1 = i
            count2 = i
            while b1==False:
                if count1 < 0 or count2 >= len(s):
                    break
                if s[count1] != s[count2]:
                    break
                if len(s[count1:count2+1]) > len(final_str):
                    final_str = s[count1:count2+1]
                count1 -= 1
                count2 += 1

            count1 = i
            count2 = i+1
            while b1==False:
                if count1 < 0 or count2 >= len(s):
                    break
                if s[count1] != s[count2]:
                    break
                if len(s[count1:count2+1]) > len(final_str):
                    final_str = s[count1:count2+1]
                count1 -= 1
                count2 += 1


        return(final_str)
        
