class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target >= letters[-1]:
            return letters[0]
        b1 = False
        final = ""
        while b1==False:
            mid = len(letters)//2
            if len(letters) <= 2:
                break
            if letters[mid] == target:
                letters = letters[mid+1:]
                continue
            if letters[mid] < target:
                letters = letters[mid+1:]
                continue
            if letters[mid] > target:
                letters = letters[:mid+1]
                continue
        for i in letters:
            if i > target:
                final = i
                break
        return(final)
