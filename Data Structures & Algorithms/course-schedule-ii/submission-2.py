class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqs = defaultdict(list)
        for pre in prerequisites:
            prereqs[pre[0]].append(pre[1])
        
        topo_sort = []
        visited = set()
        def dfs(crs):
            if crs in visited:
                return False
            
            visited.add(crs)
            for pq in prereqs[crs]:
                if not dfs(pq):
                    return False

            visited.remove(crs)
            prereqs[crs] = []
            if crs not in topo_sort:
                topo_sort.append(crs)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return topo_sort