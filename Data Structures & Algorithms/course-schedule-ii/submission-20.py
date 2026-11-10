class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        prereq = {c: [] for c in range(numCourses)}
        
        for src, dst in prerequisites:
            prereq[src].append(dst)

        # visited, output
        output = []
        visited, cycle = set(), set()

        def dfs(course):
            if course in visited:
                return True
            if course in cycle:
                return False
            
            cycle.add(course)
            for neighbor in prereq[course]:
                if dfs(neighbor) == False:
                    return False
            cycle.remove(course)
            visited.add(course)
            output.append(course)
            return True

        for course in range(numCourses):
            if dfs(course) == False:
                return []
        return output
                