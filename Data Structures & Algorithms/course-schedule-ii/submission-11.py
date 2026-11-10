class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj = [[] for i in range(numCourses)]
        in_degree = [0] * numCourses

        for src, dst in prerequisites: 
            in_degree[dst] += 1
            adj[src].append(dst)
        
        q = deque()

        for course in range(numCourses):
            if in_degree[course] == 0:
                q.append(course)

        result = []
        while q:
            node = q.popleft()
            result.append(node)

            for neighbor in adj[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    q.append(neighbor)
        
        return result[::-1] if len(result) == numCourses else []