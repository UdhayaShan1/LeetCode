class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dp = {}
        for i in range(len(numbers)):
            if numbers[i] not in dp:
                dp[numbers[i]] = []
                dp[numbers[i]].append(i)
            else:
                dp[numbers[i]].append(i)

        for i in range(len(numbers)):
            diff = target - numbers[i]
            flag = 0
            list2 = []
            if diff in dp:
                for j in dp[diff]:
                    if j != i:
                        list2.append(i+1)
                        list2.append(j+1)
                        flag+=1
                        break
            if flag > 0:
                break

        return(list2)
