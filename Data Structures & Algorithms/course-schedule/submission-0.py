class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = defaultdict(list) # c : [prqs]
        for course, prereq in prerequisites:
            prereqs[course].append(prereq)

        visited = set() # course number

        def dfs(course):
            if course in visited:
                return False
            if prereqs[course] == []:
                return True
            
            visited.add(course)
            for pre in prereqs[course]:
                if not dfs(pre): return False
            
            visited.remove(course)
            prereqs[course] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i): return False
        
        return True