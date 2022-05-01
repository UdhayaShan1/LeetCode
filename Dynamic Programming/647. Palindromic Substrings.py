class Solution:
    def countSubstrings(self, s: str) -> int:
        min1 = 0
        final_str = ""
        final_list = []
        for i in range(len(s)):
            b1 = False
            count1 = i
            count2 = i
            while b1==False:
                if count1 < 0 or count2 >= len(s):
                    break
                if s[count1] != s[count2]:
                    break
                final_list.append(s[count1:count2+1])
                count1 -= 1
                count2 += 1

            count1 = i
            count2 = i+1
            while b1==False:
                if count1 < 0 or count2 >= len(s):
                    break
                if s[count1] != s[count2]:
                    break
                final_list.append(s[count1:count2+1])
                count1 -= 1
                count2 += 1


        return(len(final_list))
