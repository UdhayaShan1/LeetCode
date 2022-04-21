class Solution:
    def isPalindrome(self, s: str) -> bool:
        str1 = ""
        for i in s:
            if i.isalpha() == True or i.isdigit() == True:
                str1 += i.lower()

        return(str1 == str1[::-1])
