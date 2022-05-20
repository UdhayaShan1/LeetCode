class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        list1 = []
        for i in mat:
            list1.append(sum(i))

        dp = {}
        for i in range(len(list1)):
            if list1[i] not in dp:
                dp[list1[i]] = [i]
            else:
                dp[list1[i]].append(i)
                
        list1 = list(set(list1))
        list1.sort()
        count = 0
        row_final = []
        
        for i in range(len(list1)):
            if len(row_final) >= k:
                break
            row_final+=(dp[list1[i]])

        return(row_final[:k])
