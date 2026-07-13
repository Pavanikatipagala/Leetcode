class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        adjList = [[] for i in range(numCourses)]
        indegree=[0] *numCourses
        
        for course,prereq in prerequisites:
            adjList[course].append(prereq)
            indegree[prereq]+=1
        
        queue=[]
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        count =0
        while queue:
            node = queue.pop(0)
            count+=1
            for nei in adjList[node]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    queue.append(nei)

        return count == numCourses 

        