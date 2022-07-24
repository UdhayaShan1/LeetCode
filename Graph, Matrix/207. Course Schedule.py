class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dp2 = {}
        @functools.lru_cache(None)
        def dfs(want_take_course):
            if want_take_course in dp2:
                return 1

            y1 = 0
            for i in range(len(prerequisites)):
                if prerequisites[i][0] == want_take_course:
                    dp2[want_take_course] = 1
                    y1 += dfs(prerequisites[i][-1])
                    del dp2[want_take_course]
            return y1

        flag = 0
        for i in range(0,numCourses):
            if dfs(i) > 0:
                return False
        return True
