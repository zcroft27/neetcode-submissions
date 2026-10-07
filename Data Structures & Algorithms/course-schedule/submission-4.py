class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        prereqs = {i : [] for i in range(numCourses)} # crs : [prereqs]
        # [[0,1],[1,0]]
        # {0:[1]}
        for crs, pq in prerequisites:
            prereqs[crs].append(pq)

        visited = set()

        def dfs(course):
            if course in visited:
                return False
            visited.add(course)
            for prereq in prereqs[course]:
                if not dfs(prereq):
                    return False
            
            visited.remove(course)
            prereqs[course] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True