class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        edg = [[] for c in range(n)]

        for src, dst in edges:
            edg[src].append(dst)
            edg[dst].append(src)
        
        visited =  set()
        def dfs(edge,parent):
            if edge in visited:
                return False
            
            visited.add(edge)
            for neighbor in edg[edge]:
                if neighbor == parent:
                    continue
                if dfs(neighbor, edge) == False:
                    return False
            return True
        
        return dfs(0,-1) and len(visited) == n