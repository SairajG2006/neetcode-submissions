class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        graph = {i: [] for i in range(n)}

        for a, b in edges:

            graph[a].append(b)
            graph[b].append(a)
            
        
        visited = set()
        q = deque()

        def bfs(node):
            q.append(node)
            visited.add(node)

            while q:
                curr = q.popleft()

                for nei in graph[curr]:
                    if nei not in visited:
                        q.append(nei)
                        visited.add(nei)

        
        components = 0
        for node in range(n):
            if node not in visited:
                bfs(node)
                components += 1
        

        return components
        