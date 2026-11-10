class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj = [[] for c in range(n)]

        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)
        
        visited = set()
        def dfs(node):
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        
        res = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                res += 1
        return res

        