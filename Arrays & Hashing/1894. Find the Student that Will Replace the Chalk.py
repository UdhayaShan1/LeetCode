class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        remain = k % sum(chalk)
        if remain == 0:
            return(0)
        else:
            final = 0
            for i in range(len(chalk)):
                if remain < chalk[i]:
                    final = i
                    break
                remain -= chalk[i]
            return(final)
