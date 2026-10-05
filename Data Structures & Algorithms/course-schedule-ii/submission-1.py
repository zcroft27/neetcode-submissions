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
            if prereqs[crs] == []:
                if crs not in topo_sort:
                    topo_sort.append(crs)
                return True
            
            visited.add(crs)
            
            for pre in prereqs[crs]:
                if not dfs(pre): return False
            
            visited.remove(crs)
            prereqs[crs] = []
            topo_sort.append(crs)
            return True
        
        for num in range(numCourses):
            if not dfs(num): return []

        return topo_sort