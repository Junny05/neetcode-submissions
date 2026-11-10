class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj = [[] for i in range(numCourses)]
        in_degree = [0] * numCourses

        for src, dst in prerequisites:
            in_degree[dst] += 1
            adj[src].append(dst)
        
        q = deque()
        finish = 0

        for course in range(numCourses):
            if in_degree[course] == 0:
                q.append(course)
        
        while q:
            node = q.popleft()

            finish += 1
            for neighbor in adj[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    q.append(neighbor)
        
        return finish == numCourses

