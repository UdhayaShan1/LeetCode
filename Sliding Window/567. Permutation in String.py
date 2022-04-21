class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return(False)
        else:
            dp_s1 = {}
            for i in s1:
                if i not in dp_s1:
                    dp_s1[i] = 1
                else:
                    dp_s1[i] += 1
            temp = []
            count = 0
            temp_dp = {}
            for i in range(len(s2)):
                temp.append(s2[i])
                if s2[i] not in temp_dp:
                    temp_dp[s2[i]] = 1
                else:
                    temp_dp[s2[i]] += 1
                if len(temp) == len(s1):
                    flag = 0
                    for i in temp_dp.keys():
                        if i not in dp_s1 and temp_dp[i] > 0:
                            flag += 1
                            break
                        elif i in dp_s1 and temp_dp[i] > 0:
                            if dp_s1[i] != temp_dp[i]:
                                flag+=1
                                break
                    if flag == 0:
                        return(True)
                    else:
                        temp_dp[temp[0]] -= 1
                        temp.pop(0)
            return(False)
