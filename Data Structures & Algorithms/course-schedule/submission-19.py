class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        prerequisites.sort()

        courses = defaultdict(list)

        for c, r in prerequisites: 
            courses[c].append(r)


        visited = set()
        stack = [i for i in range(numCourses)]

        def dfs(i, visited): 
            print(i)
            nonlocal courses
            nonlocal stack
            if len(courses[i]) == 0:
                return True

            if i in visited: 
                return False
            visited.add(i)
            
            
            for prereq in courses[i].copy():
                if dfs(prereq, visited):
                    courses[i].remove(prereq)
                    continue
                else:
                    return False
            
            return True

        while stack: 
            course = stack.pop()
            if not dfs(course, visited):
                return False

        return True




