class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        adjList = [[]for i in range(numCourses)]
        indegree=[0]*numCourses
        
        for course, prereq in prerequisites:
            adjList[prereq].append(course)
            indegree[course] += 1

        queue=[]
        ans=[]
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
                
        while queue:
            node = queue.pop(0)  
            ans.append(node) 
            for nei in adjList[node]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    queue.append(nei)
                    
        if len(ans) == numCourses:
            return ans
        else:
            return []

        