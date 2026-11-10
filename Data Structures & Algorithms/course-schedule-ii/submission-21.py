class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        prereq = {c: [] for c in range(numCourses)}

        for src, dst in prerequisites:
            prereq[src].append(dst)
        
        visited,cycle = set(),set()
        res = []

        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True
            
            cycle.add(course)
            for c in prereq[course]:
                if dfs(c) == False:
                    return False
            cycle.remove(course)
            visited.add(course)
            res.append(course)
        
        for i in range(numCourses):
            if dfs(i) == False:
                return []
        return res
