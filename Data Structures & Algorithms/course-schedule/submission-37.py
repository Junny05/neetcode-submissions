class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = [[] for i in range(numCourses)]
        visited,cycle = set(), set()
        
        for crs, preq in prerequisites:
            pre[crs].append(preq)
        
        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True
            
            visited.add(course)
            cycle.add(course)
            for i in pre[course]:
                if not dfs(i):
                    return False
            cycle.remove(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
