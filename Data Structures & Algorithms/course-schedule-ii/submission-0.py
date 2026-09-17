class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        needs = defaultdict(list)
        courses = defaultdict(list)

        for c, r in prerequisites: 
            needs[r].append(c)
            courses[c].append(r)
        
        start = []
        for i in range(numCourses):
            if courses[i] == []:
                start.append(i)

        if len(start) == 0:
            return []

        res = []
        while start:
            course = start.pop()
            res.append(course)
            # print(res)
            # print(start)
            # print("dsf")

            for nextCourse in needs[course]:
                # print(course)
                # print(nextCourse)
                courses[nextCourse].remove(course)
                if courses[nextCourse] == []:
                    start.append(nextCourse)


        if len(res) == numCourses:
            return res
        return []


        