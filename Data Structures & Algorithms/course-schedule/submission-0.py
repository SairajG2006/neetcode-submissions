class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adjMap = {i : [] for i in range(numCourses)}
        for a, b in prerequisites:
            adjMap[a].append(b)
        
        visited = set()
        path = set()

        def dfs(course):

            if course in path:
                return False
            
            if course in visited:
                return True
            
            path.add(course)
            
            for pre in adjMap[course]:
                if not dfs(pre):
                    return False

            path.remove(course)
            visited.add(course)
            return True
        
        for course in adjMap:
            if not dfs(course):
                return False
        
        return True