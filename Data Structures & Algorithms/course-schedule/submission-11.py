from collections import defaultdict 

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        requirements = defaultdict(list)

        for course, prereq in prerequisites:
            
            requirements[course].append(prereq)

        print(requirements)
        seen = set()
        visiting = set()
        cleared = set()

        def dfs(course):
            if course in seen: 
                return False
            if course in cleared: 
                return True

            seen.add(course)
            prereqs = requirements[course]

            for c in prereqs: 
                res = dfs(c)

                if not res: 
                    return False
            seen.remove(course)
            cleared.add(course)
            return True

        for r in requirements.copy():
            if not dfs(r):
                return False

        return True
                
            
            
                

            


        return True


