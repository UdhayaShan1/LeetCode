class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        if dislikes == []:
            return True

        adj = {}
        for i in range(1,n+1):
            adj[i] = []

        for i in dislikes:
            if i[0] in adj:
                adj[i[0]].append(i[1])
            if i[0] not in adj:
                adj[i[0]] = []
                adj[i[0]].append(i[1])

            if i[1] in adj:
                adj[i[1]].append(i[0])
            if i[1] not in adj:
                adj[i[1]] = []
                adj[i[1]].append(i[0])

        dp2 = {}
        color_s = {}
        def dfs(color,node):
            if node in dp2:
                if color_s[node] == color:
                    return 0
                else:
                    return 1
            y1 = 0
            for i in adj[node]:
                if color == "RED":
                    dp2[node] = 1
                    color_s[node] = "RED"
                    y1 += dfs("BLUE",i)
                else:
                    dp2[node] = 1
                    color_s[node] = "BLUE"
                    y1 += dfs("RED",i)
            return y1

        for i in range(1,n+1):
            if i in color_s:
                if color_s[i] == "RED":
                    x=(dfs("RED",i))
                elif color_s[i] == "BLUE":
                    x=(dfs("BLUE",i))
            else:
                x=(dfs("RED",i))
            if x > 0:
                return False
        return True
