class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        import collections
        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        dp2 = {}
        def dfs(node):
            if node == destination:
                return 1
            if node in dp2:
                return 0
            y1=0
            for i in graph[node]:
                dp2[node] = 1
                y1+=dfs(i)

            return y1

        return(dfs(source)>=1)
