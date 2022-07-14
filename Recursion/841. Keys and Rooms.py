class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        curr_keys = {}
        dp2={}
        import sys
        for i in rooms[0]:
            curr_keys[i] = 1

        rooms2 = rooms[:]
        import functools
        @functools.lru_cache(None)
        def dfs(count):
            if len(dp2.keys()) == len(rooms2)-1:
                return 1

            y1 = 0
            for i in range(len(rooms2)):
                if i == 0:
                    continue
                if i in dp2:
                    continue
                if i not in curr_keys:
                    continue
                dp2[i] = 1
                for j in rooms2[i]:
                    if j in curr_keys:
                        continue
                    curr_keys[j] = 1
                y1+=dfs(count+1)
                del dp2[i]
            return y1
        return(dfs(0))
            
