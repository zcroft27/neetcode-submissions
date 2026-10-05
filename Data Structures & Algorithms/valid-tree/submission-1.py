class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # connected, acyclic graph
        # 1)
        # make sure no loops
        # - count which u visit
        # then, if count < n:
        # return false

        adj = defaultdict(list)
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        
        visited = set()
        count_visited = 0
        def dfs(node, prev):
            if node in visited:
                return False
            nonlocal count_visited
            count_visited += 1
            visited.add(node)
            if adj[node] == []:
                return True
            
            for nei in adj[node]:
                if nei == prev:
                    continue
                if not dfs(nei, node): return False

            return True
        
        if not dfs(0, -1): return False
        if count_visited < n:
            return False
        
        return True