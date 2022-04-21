class Solution:
    def isValid(self, s: str) -> bool:
        dp = {}
        flag = 0
        open_first = []
        for i in s:
            if i == "(":
                if i not in dp:
                    dp[i] = 1
                else:
                    dp[i] += 1
                open_first.append("(")
            elif i == ")":
                if "(" not in dp:
                    flag+=1
                    continue
                if dp["("] == 0:
                    flag+=1
                    continue
                dp["("] -= 1
                if open_first[-1] != "(":
                    flag+=1
                    break
                open_first.pop()


            if i == "[":

                if i not in dp:
                    dp[i] = 1
                else:
                    dp[i] += 1

                open_first.append("[")
            elif i == "]":
                if "[" not in dp:
                    flag+=1
                    continue
                if dp["["] == 0:
                    flag+=1
                    continue
                dp["["] -= 1
                if open_first[-1] != "[":
                    flag+=1
                    break
                open_first.pop()


            if i == "{":

                if i not in dp:
                    dp[i] = 1
                else:
                    dp[i] += 1

                open_first.append("{")
            elif i == "}":
                if "{" not in dp:
                    flag+=1
                    continue
                if dp["{"] == 0:
                    flag+=1
                    continue
                dp["{"] -= 1
                if open_first[-1] != "{":
                    flag+=1
                    break
                open_first.pop()
        
        for i in dp.keys():
            if dp[i] > 0:
                flag+=1
                break
        
        
        if flag > 0:
            return False
        else:
            return True
          
