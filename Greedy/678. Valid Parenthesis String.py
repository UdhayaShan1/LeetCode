class Solution:
    def checkValidString(self, s: str) -> bool:
        s2 = list(s)
        dp = {}
        b1 = False
        while b1==False:
            for i in "()":
                dp[i] = 0
            flag = 0
            last = -1
            for i in range(len(s2)):
                if s2[i] == "*":
                    continue
                if s2[i] == ")":
                    dp[s2[i]] += 1
                if s2[i] == "(":
                    dp[s2[i]] += 1
                    last = i
                if s2[i] == ")":
                    if dp["("] > 0:
                        dp["("] -= 1
                        dp[")"] -= 1
                        s2.pop(i)
                        s2.pop(last)
                        flag+=1
                        break
            if flag == 0:
                break

        b1 = False
        while b1==False:
            star = [i for i, x in enumerate(s2) if x == "*"]
            left = [i for i, x in enumerate(s2) if x == ")"]
            flag = 0
            for i in left:
                for j in star:
                    if i > j:
                        s2.pop(i)
                        s2.pop(j)
                        flag += 1
                        break
                if flag > 0:
                    break
            if flag == 0:
               break

        b1 = False
        while b1==False:
            star = [i for i, x in enumerate(s2) if x == "*"]
            right = [i for i, x in enumerate(s2) if x == "("]
            flag = 0
            for i in right:
                for j in star:
                    if i < j:
                        s2.pop(j)
                        s2.pop(i)
                        flag += 1
                        break
                if flag > 0:
                    break
            if flag == 0:
               break

        for i in s2:
            if i == ")" or i == "(":
                return False
        return True
      
