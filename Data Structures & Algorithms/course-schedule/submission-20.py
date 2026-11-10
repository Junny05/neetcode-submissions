class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        visited = set()

        for course, prereq in prerequisites:
            preMap[course].append(prereq)
            
        def dfs(course):
            if preMap[course] == []:
                return True
            
            if course in visited:
                return False
            
            visited.add(course)

            for neighbor in preMap[course]:
                if not dfs(neighbor):
                    return False
            visited.remove(course)
            preMap[course] = []
            return True
        
        for classes in range(numCourses):
            if not dfs(classes):
                return False
        return True