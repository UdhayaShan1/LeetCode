class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        global res
        global part
        res = []
        part = []
        dp = {}
        def combi(target,candidates):
            global res
            global part
            if target == 0:
                part2 = part.copy()
                part2.sort()
                if tuple(part2) not in dp:
                    res.append(part2)
                    dp[tuple(part2)] = 1
                return True
            if target < min(candidates):
                return False

            for i in range(len(candidates)):
                if target >= candidates[i]:
                    remain = target - candidates[i]
                    part.append(candidates[i])
                    combi(remain,candidates)
                    part.pop()

        combi(target,candidates)

        return(res)
