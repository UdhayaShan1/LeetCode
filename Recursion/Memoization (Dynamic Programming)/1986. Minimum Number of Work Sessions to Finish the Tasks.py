class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        import sys
        dp = {}
        def dfs(tasks,current_amt,count,prev):
            if current_amt > sessionTime:
                current_amt = prev
                count += 1
            if len(tasks) == 0:
                return count+1

            if (tuple(tasks),current_amt,count,prev) in dp:
                return dp[(tuple(tasks),current_amt,count,prev)]

            y1 = sys.maxsize
            for i in range(len(tasks)):
                x = dfs(tasks[0:i]+tasks[i+1:],current_amt+tasks[i],count,tasks[i])
                if x < y1:
                    y1 = x
            dp[(tuple(tasks),current_amt,count,prev)] = y1
            return y1

        return(dfs(tasks,0,0,0))
